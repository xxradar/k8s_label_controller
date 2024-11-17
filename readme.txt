docker build --push -t xxradar/quarantine-controller:latest .
docker push xxradar/quarantine-controller:latest



kubectl apply -f https://raw.githubusercontent.com/xxradar/kubernetes_learning/refs/heads/master/nginx-deployment.yaml

kubectl create ns hacking
kubectl apply -n hacking -f https://raw.githubusercontent.com/xxradar/kubernetes_learning/refs/heads/master/nginx-deployment.yaml



kubectl label -n hacking -l quarantine=true pods --overwrite quarantine-


conda activate kubecontroller






(base) philippebogaerts@Philippes-MacBook-Pro ~ % kubectl label -n hacking -l quarantine=true pods --overwrite quarantine- -v=8
I1116 20:01:03.712790   11006 loader.go:395] Config loaded from file:  /Users/philippebogaerts/.kube/config
I1116 20:01:03.716196   11006 round_trippers.go:463] GET https://127.0.0.1:6443/api/v1/namespaces/hacking/pods?labelSelector=quarantine%3Dtrue
I1116 20:01:03.716206   11006 round_trippers.go:469] Request Headers:
I1116 20:01:03.716211   11006 round_trippers.go:473]     Accept: application/json
I1116 20:01:03.716214   11006 round_trippers.go:473]     User-Agent: kubectl/v1.30.2 (darwin/arm64) kubernetes/3968350
I1116 20:01:03.728876   11006 round_trippers.go:574] Response Status: 200 OK in 12 milliseconds
I1116 20:01:03.728886   11006 round_trippers.go:577] Response Headers:
I1116 20:01:03.728890   11006 round_trippers.go:580]     Audit-Id: 92985f54-8b81-48e4-b49d-863e62621b77
I1116 20:01:03.728894   11006 round_trippers.go:580]     Cache-Control: no-cache, private
I1116 20:01:03.728896   11006 round_trippers.go:580]     Content-Type: application/json
I1116 20:01:03.728898   11006 round_trippers.go:580]     X-Kubernetes-Pf-Flowschema-Uid: d056a202-1397-42d4-9a66-352322ea83bd
I1116 20:01:03.728900   11006 round_trippers.go:580]     X-Kubernetes-Pf-Prioritylevel-Uid: 48118819-dcc9-45d0-b015-cf9649301180
I1116 20:01:03.728902   11006 round_trippers.go:580]     Date: Sat, 16 Nov 2024 19:01:03 GMT
I1116 20:01:03.729153   11006 request.go:1212] Response Body: {"kind":"PodList","apiVersion":"v1","metadata":{"resourceVersion":"2546450"},"items":[{"metadata":{"name":"nginx-deployment-6cfb64b7c5-b68x4","generateName":"nginx-deployment-6cfb64b7c5-","namespace":"hacking","uid":"229a7d29-8f34-4667-b41d-e276501484b7","resourceVersion":"2546426","creationTimestamp":"2024-11-16T18:54:18Z","labels":{"app":"nginx","pod-template-hash":"6cfb64b7c5","quarantine":"true"},"ownerReferences":[{"apiVersion":"apps/v1","kind":"ReplicaSet","name":"nginx-deployment-6cfb64b7c5","uid":"fe80ec67-8677-4014-adb6-2f85c5837603","controller":true,"blockOwnerDeletion":true}],"managedFields":[{"manager":"kube-controller-manager","operation":"Update","apiVersion":"v1","time":"2024-11-16T18:54:18Z","fieldsType":"FieldsV1","fieldsV1":{"f:metadata":{"f:generateName":{},"f:labels":{".":{},"f:app":{},"f:pod-template-hash":{}},"f:ownerReferences":{".":{},"k:{\"uid\":\"fe80ec67-8677-4014-adb6-2f85c5837603\"}":{}}},"f:spec":{"f:containers":{"k:{\"name\":\"nginx\"}":{".":{},"f:image":{},"f:imagePullPolicy": [truncated 13050 chars]
I1116 20:01:03.730687   11006 request.go:1212] Request Body: {"metadata":{"labels":{"quarantine":null}}}
I1116 20:01:03.730715   11006 round_trippers.go:463] PATCH https://127.0.0.1:6443/api/v1/namespaces/hacking/pods/nginx-deployment-6cfb64b7c5-b68x4?fieldManager=kubectl-label
I1116 20:01:03.730720   11006 round_trippers.go:469] Request Headers:
I1116 20:01:03.730725   11006 round_trippers.go:473]     Content-Type: application/merge-patch+json
I1116 20:01:03.730729   11006 round_trippers.go:473]     Accept: application/json
I1116 20:01:03.730731   11006 round_trippers.go:473]     User-Agent: kubectl/v1.30.2 (darwin/arm64) kubernetes/3968350
I1116 20:01:03.739818   11006 round_trippers.go:574] Response Status: 200 OK in 9 milliseconds
I1116 20:01:03.739856   11006 round_trippers.go:577] Response Headers:
I1116 20:01:03.739864   11006 round_trippers.go:580]     X-Kubernetes-Pf-Flowschema-Uid: d056a202-1397-42d4-9a66-352322ea83bd
I1116 20:01:03.739869   11006 round_trippers.go:580]     X-Kubernetes-Pf-Prioritylevel-Uid: 48118819-dcc9-45d0-b015-cf9649301180
I1116 20:01:03.739873   11006 round_trippers.go:580]     Date: Sat, 16 Nov 2024 19:01:03 GMT
I1116 20:01:03.739876   11006 round_trippers.go:580]     Audit-Id: 34c5b7b0-a98b-464c-9f35-d1809bcb2484
I1116 20:01:03.739878   11006 round_trippers.go:580]     Cache-Control: no-cache, private
I1116 20:01:03.739882   11006 round_trippers.go:580]     Content-Type: application/json
I1116 20:01:03.739939   11006 request.go:1212] Response Body: {"kind":"Pod","apiVersion":"v1","metadata":{"name":"nginx-deployment-6cfb64b7c5-b68x4","generateName":"nginx-deployment-6cfb64b7c5-","namespace":"hacking","uid":"229a7d29-8f34-4667-b41d-e276501484b7","resourceVersion":"2546451","creationTimestamp":"2024-11-16T18:54:18Z","labels":{"app":"nginx","pod-template-hash":"6cfb64b7c5"},"ownerReferences":[{"apiVersion":"apps/v1","kind":"ReplicaSet","name":"nginx-deployment-6cfb64b7c5","uid":"fe80ec67-8677-4014-adb6-2f85c5837603","controller":true,"blockOwnerDeletion":true}],"managedFields":[{"manager":"kube-controller-manager","operation":"Update","apiVersion":"v1","time":"2024-11-16T18:54:18Z","fieldsType":"FieldsV1","fieldsV1":{"f:metadata":{"f:generateName":{},"f:labels":{".":{},"f:app":{},"f:pod-template-hash":{}},"f:ownerReferences":{".":{},"k:{\"uid\":\"fe80ec67-8677-4014-adb6-2f85c5837603\"}":{}}},"f:spec":{"f:containers":{"k:{\"name\":\"nginx\"}":{".":{},"f:image":{},"f:imagePullPolicy":{},"f:name":{},"f:ports":{".":{},"k:{\"containerPort\":80,\"protocol\":\"TC [truncated 3465 chars]
pod/nginx-deployment-6cfb64b7c5-b68x4 labeled
I1116 20:01:03.740955   11006 request.go:1212] Request Body: {"metadata":{"labels":{"quarantine":null}}}
I1116 20:01:03.740986   11006 round_trippers.go:463] PATCH https://127.0.0.1:6443/api/v1/namespaces/hacking/pods/nginx-deployment-6cfb64b7c5-djkrz?fieldManager=kubectl-label
I1116 20:01:03.740991   11006 round_trippers.go:469] Request Headers:
I1116 20:01:03.740996   11006 round_trippers.go:473]     Accept: application/json
I1116 20:01:03.740999   11006 round_trippers.go:473]     Content-Type: application/merge-patch+json
I1116 20:01:03.741001   11006 round_trippers.go:473]     User-Agent: kubectl/v1.30.2 (darwin/arm64) kubernetes/3968350
I1116 20:01:03.747956   11006 round_trippers.go:574] Response Status: 200 OK in 6 milliseconds
I1116 20:01:03.747972   11006 round_trippers.go:577] Response Headers:
I1116 20:01:03.747977   11006 round_trippers.go:580]     Content-Type: application/json
I1116 20:01:03.747981   11006 round_trippers.go:580]     X-Kubernetes-Pf-Flowschema-Uid: d056a202-1397-42d4-9a66-352322ea83bd
I1116 20:01:03.747984   11006 round_trippers.go:580]     X-Kubernetes-Pf-Prioritylevel-Uid: 48118819-dcc9-45d0-b015-cf9649301180
I1116 20:01:03.747987   11006 round_trippers.go:580]     Date: Sat, 16 Nov 2024 19:01:03 GMT
I1116 20:01:03.747989   11006 round_trippers.go:580]     Audit-Id: 88ccff84-38b0-4c63-bbb9-007964503b08
I1116 20:01:03.747991   11006 round_trippers.go:580]     Cache-Control: no-cache, private
I1116 20:01:03.748041   11006 request.go:1212] Response Body: {"kind":"Pod","apiVersion":"v1","metadata":{"name":"nginx-deployment-6cfb64b7c5-djkrz","generateName":"nginx-deployment-6cfb64b7c5-","namespace":"hacking","uid":"80c974b7-294a-400f-b399-b819f69980d2","resourceVersion":"2546452","creationTimestamp":"2024-11-16T18:54:18Z","labels":{"app":"nginx","pod-template-hash":"6cfb64b7c5"},"ownerReferences":[{"apiVersion":"apps/v1","kind":"ReplicaSet","name":"nginx-deployment-6cfb64b7c5","uid":"fe80ec67-8677-4014-adb6-2f85c5837603","controller":true,"blockOwnerDeletion":true}],"managedFields":[{"manager":"kube-controller-manager","operation":"Update","apiVersion":"v1","time":"2024-11-16T18:54:18Z","fieldsType":"FieldsV1","fieldsV1":{"f:metadata":{"f:generateName":{},"f:labels":{".":{},"f:app":{},"f:pod-template-hash":{}},"f:ownerReferences":{".":{},"k:{\"uid\":\"fe80ec67-8677-4014-adb6-2f85c5837603\"}":{}}},"f:spec":{"f:containers":{"k:{\"name\":\"nginx\"}":{".":{},"f:image":{},"f:imagePullPolicy":{},"f:name":{},"f:ports":{".":{},"k:{\"containerPort\":80,\"protocol\":\"TC [truncated 3465 chars]
pod/nginx-deployment-6cfb64b7c5-djkrz labeled
I1116 20:01:03.748993   11006 request.go:1212] Request Body: {"metadata":{"labels":{"quarantine":null}}}
I1116 20:01:03.749025   11006 round_trippers.go:463] PATCH https://127.0.0.1:6443/api/v1/namespaces/hacking/pods/nginx-deployment-6cfb64b7c5-k8v2t?fieldManager=kubectl-label
I1116 20:01:03.749030   11006 round_trippers.go:469] Request Headers:
I1116 20:01:03.749035   11006 round_trippers.go:473]     User-Agent: kubectl/v1.30.2 (darwin/arm64) kubernetes/3968350
I1116 20:01:03.749039   11006 round_trippers.go:473]     Accept: application/json
I1116 20:01:03.749043   11006 round_trippers.go:473]     Content-Type: application/merge-patch+json
I1116 20:01:03.754328   11006 round_trippers.go:574] Response Status: 200 OK in 5 milliseconds
I1116 20:01:03.754338   11006 round_trippers.go:577] Response Headers:
I1116 20:01:03.754343   11006 round_trippers.go:580]     Content-Type: application/json
I1116 20:01:03.754347   11006 round_trippers.go:580]     X-Kubernetes-Pf-Flowschema-Uid: d056a202-1397-42d4-9a66-352322ea83bd
I1116 20:01:03.754350   11006 round_trippers.go:580]     X-Kubernetes-Pf-Prioritylevel-Uid: 48118819-dcc9-45d0-b015-cf9649301180
I1116 20:01:03.754353   11006 round_trippers.go:580]     Date: Sat, 16 Nov 2024 19:01:03 GMT
I1116 20:01:03.754355   11006 round_trippers.go:580]     Audit-Id: 451fd80b-2721-40e1-b550-23385a5244cb
I1116 20:01:03.754356   11006 round_trippers.go:580]     Cache-Control: no-cache, private
I1116 20:01:03.754398   11006 request.go:1212] Response Body: {"kind":"Pod","apiVersion":"v1","metadata":{"name":"nginx-deployment-6cfb64b7c5-k8v2t","generateName":"nginx-deployment-6cfb64b7c5-","namespace":"hacking","uid":"386e4685-0459-499e-a7fe-41c625d345dc","resourceVersion":"2546453","creationTimestamp":"2024-11-16T18:54:18Z","labels":{"app":"nginx","pod-template-hash":"6cfb64b7c5"},"ownerReferences":[{"apiVersion":"apps/v1","kind":"ReplicaSet","name":"nginx-deployment-6cfb64b7c5","uid":"fe80ec67-8677-4014-adb6-2f85c5837603","controller":true,"blockOwnerDeletion":true}],"managedFields":[{"manager":"kube-controller-manager","operation":"Update","apiVersion":"v1","time":"2024-11-16T18:54:18Z","fieldsType":"FieldsV1","fieldsV1":{"f:metadata":{"f:generateName":{},"f:labels":{".":{},"f:app":{},"f:pod-template-hash":{}},"f:ownerReferences":{".":{},"k:{\"uid\":\"fe80ec67-8677-4014-adb6-2f85c5837603\"}":{}}},"f:spec":{"f:containers":{"k:{\"name\":\"nginx\"}":{".":{},"f:image":{},"f:imagePullPolicy":{},"f:name":{},"f:ports":{".":{},"k:{\"containerPort\":80,\"protocol\":\"TC [truncated 3465 chars]
pod/nginx-deployment-6cfb64b7c5-k8v2t labeled
(base) philippebogaerts@Philippes-MacBook-Pro ~ %