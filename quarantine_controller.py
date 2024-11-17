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
    Create a NetworkPolicy to block all ingress and egress traffic
    for pods labeled with "quarantine=true".
    """
    network_policy_manifest = {
        "apiVersion": "networking.k8s.io/v1",
        "kind": "NetworkPolicy",
        "metadata": {
            "name": "quarantine-block-all",
            "namespace": namespace
        },
        "spec": {
            "podSelector": {
                "matchLabels": {
                    QUARANTINE_LABEL: QUARANTINE_VALUE
                }
            },
            "policyTypes": ["Ingress", "Egress"]
        }
    }

    networking_api = kubernetes.client.NetworkingV1Api()
    try:
        networking_api.create_namespaced_network_policy(
            body=network_policy_manifest,
            namespace=namespace
        )
        logging.info(f"Created network policy 'quarantine-block-all' in namespace {namespace}.")
    except ApiException as e:
        if e.status == 409:
            logging.info(f"Network policy 'quarantine-block-all' already exists in namespace {namespace}.")
        else:
            logging.error(f"Failed to create network policy: {e}")

# Ensure network policy is created whenever a quarantine resource is handled
@kopf.on.create("quarantine.example.com", "v1", "quarantine")
@kopf.on.update("quarantine.example.com", "v1", "quarantine")
def ensure_network_policy(spec, **kwargs):
    namespace = spec.get("namespace", NAMESPACE_DEFAULT)
    create_quarantine_network_policy(namespace)
    return



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
