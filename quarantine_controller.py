import kopf
import logging
import kubernetes.client
from kubernetes.client.rest import ApiException

# Setup logging
logging.basicConfig(level=logging.INFO)

QUARANTINE_LABEL = "quarantine"
QUARANTINE_VALUE = "true"
NAMESPACE_DEFAULT = "default"


def create_quarantine_network_policy(namespace):
    """
    Creates a NetworkPolicy that blocks all traffic for pods labeled with quarantine=true.
    """
    api = kubernetes.client.NetworkingV1Api()
    network_policy_name = "quarantine-policy"

    # Define the NetworkPolicy
    network_policy = kubernetes.client.V1NetworkPolicy(
        metadata=kubernetes.client.V1ObjectMeta(
            name=network_policy_name,
            namespace=namespace,
        ),
        spec=kubernetes.client.V1NetworkPolicySpec(
            pod_selector=kubernetes.client.V1LabelSelector(
                match_labels={QUARANTINE_LABEL: QUARANTINE_VALUE}
            ),
            ingress=[],
            egress=[],
            policy_types=["Ingress", "Egress"],
        ),
    )

    # Check if the policy already exists; if not, create it
    try:
        api.create_namespaced_network_policy(namespace=namespace, body=network_policy)
        logging.info(f"Created quarantine NetworkPolicy {network_policy_name} in namespace {namespace}.")
    except ApiException as e:
        if e.status == 409:
            logging.info(f"Quarantine NetworkPolicy {network_policy_name} already exists.")
        else:
            logging.error(f"Failed to create quarantine NetworkPolicy: {e}")



@kopf.on.create("quarantine.example.com", "v1", "quarantine")
@kopf.on.update("quarantine.example.com", "v1", "quarantine")
def handle_quarantine_resource(spec, **kwargs):
    """
    Handles the Quarantine CRD and labels all pods associated with the specified deployment.
    """
    deployment_name = spec.get("deploymentName")
    namespace = spec.get("namespace", NAMESPACE_DEFAULT)

    if not deployment_name:
        logging.error("Quarantine resource must specify a deploymentName.")
        return

    core_api = kubernetes.client.CoreV1Api()
    apps_api = kubernetes.client.AppsV1Api()

    try:
        # Fetch the deployment to get the label selector
        deployment = apps_api.read_namespaced_deployment(name=deployment_name, namespace=namespace)
        selector = deployment.spec.selector.match_labels
        logging.info(f"Deployment selector: {selector}")

        # List all pods that match the selector
        pods = core_api.list_namespaced_pod(
            namespace=namespace,
            label_selector=",".join([f"{k}={v}" for k, v in selector.items()])
        )
        logging.info(f"Matching pods: {[pod.metadata.name for pod in pods.items]}")

        # Add the quarantine label to each pod
        for pod in pods.items:
            try:
                if not pod.metadata.labels:
                    pod.metadata.labels = {}
                pod.metadata.labels[QUARANTINE_LABEL] = QUARANTINE_VALUE
                core_api.patch_namespaced_pod(
                    name=pod.metadata.name,
                    namespace=namespace,
                    body={"metadata": {"labels": pod.metadata.labels}}
                )
                logging.info(f"Labeled pod {pod.metadata.name} with {QUARANTINE_LABEL}={QUARANTINE_VALUE}.")
            except ApiException as e:
                logging.error(f"Failed to label pod {pod.metadata.name}: {e}")
    except ApiException as e:
        logging.error(f"Failed to label pods for deployment {deployment_name}: {e}")
