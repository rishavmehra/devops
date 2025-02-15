# K8s

## Kubeconfig file, GVK/GVR, K8s rest API

```bash
# Generate RSA Key
openssl genrsa -out rishav.key 2048

# Create Certificate Signing Request (CSR)
openssl req -new -key rishav.key -out developer.csr -subj "/CN=rishav"

# Base64 Encode CSR
cat developer.csr | base64 | tr -d '\n'
```

---

### CSR YAML Configuration

```yaml
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: rishav
spec:
  request: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0KTUlJQ1p6Q0NBVThDQVFBd0lqRVBNQTBHQTFVRUF3d0djMkZwZVdGdE1ROHdEUVlEVlFRS0RBWm5jbTkxY0RFdwpnZ0VpTUEwR0NTcUdTSWIzRFFFQkFRVUFBNElCRHdBd2dnRUtBb0lCQVFDOWRSLzhvcUl4R3Vsa0IxS2Q1aTJFClZpM0g1SkpmbjlZWk54WWRGMm41UUU0bFhvSmpwbmtzeEVrWWIwZUlKWkdHUXFYMzhIN2RQRi9UN3A2RVJDWWQKNmhJNHRxbFFRa0lFT202RnNKTVJUZ3p2VHdjNzFMSitnRVFXbkEwTVA5MUVqNzBGT0xFU1ZOb1lvd2huNllWTQpCbXhHTUdOWW1RRjVQRGw3VlBSNTFZenRsaHZvVkpKSnJoUXN1empVNGJnUGxGOURsaEZyQThXcHdEU2d2N2xLCkkwa25ZWjdVQkVFRnJweUU5VU9EMmlFVHFXMnlIaFc0Ym0rY0RMRFJQS3hrYytpaUlldjBqWVN4RzIyUUt0VE8KR1J0bS9LT1NkQTVZOG5DZ3JTZk9adGNFVExhMGc1RzlhNEtFRHNoK2wxTWNraVdPbS9oSUpsVDFUQnIxSm9qVgpBZ01CQUFHZ0FEQU5CZ2txaGtpRzl3MEJBUXNGQUFPQ0FRRUFDTmxkbkErcFdrZE1NNGV3Uk1LZXpvK0hwY215CnhOSjJ6OFJPMkQrZ2p6NXBZNjlRMlFaRFRKSkZnUTVpRnFVUGFQNDc4ZHdxSUMwTFVGMXh2Nkh5Z3d4aElWZkYKT3N0MzZhcTZIRCtFM1lCazNMRzhSbGlUMTh6UXUzYS9Nd3dGWVFxV0xCcGNhUU84ZUpPVlZ5Ty9URk82YWUrQQpzYzRJSlUvRDZUNjNWZS9NM3B2Qkd4cHRabnNPTC81cUhlL1p4MnhXMlU2Yksyb290cDBjQjZOaHFITVVwcGJ0ClEzYkRIbGl4dVV2TzI0cFVMeC9CZVA4SHV2R1RnUUpzemJIeGt4TDR5cDZkMDNRZm42RjdaeWFhTnlTMGtqamQKWWhqd0E2Q3FjQXdVOXFwWlJCdkVFYUpuTk5JMHlnUEs4M1ZRYnN5VEFoQk01YWZvYWpOb3h3OTVHQT09Ci0tLS0tRU5EIENFUlRJRklDQVRFIFJFUVVFU1QtLS0tLQo=
  signerName: kubernetes.io/kube-apiserver-client
  usages:
  - client auth
```

---

```bash
# Apply CSR
kubectl apply -f csr.yaml

# Approve CSR
kubectl certificate approve rishav

# Retrieve and Decode the Certificate
kubectl get csr rishav -o jsonpath='{.status.certificate}' | base64 --decode > rishav.crt
```

### Role and RoleBinding Configuration

```yaml
kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  namespace: default
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "watch", "list"]
---
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: read-pods
  namespace: default
subjects:
- kind: User
  name: rishav
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

```bash
# Apply Role and RoleBinding
kubectl apply -f role.yaml

# Set Credentials and Context
kubectl config set-credentials rishav --client-certificate=rishav.crt --client-key=rishav.key
kubectl config get-contexts
kubectl config set-context rishav-context --cluster=kubernetes --namespace=default --user=rishav
kubectl config use-context rishav-context

# Deploy nginx
kubectl run nginx --image=nginx
```

### GVR | GVK -> [Read Here](https://jamy.hashnode.dev/understanding-kubernetes-gvk-and-gvr-in-60-seconds)

### Merging Multiple KubeConfig Files

```bash
export KUBECONFIG=/path/to/first/config:/path/to/second/config:/path/to/third/config
```

---

### Deployment JSON Creation

```bash
kubectl create deployment nginx --image=nginx --dry-run=client -o json > deploy.json
kubectl run nginx --image=nginx --dry-run=client -o json
```

### Service Account (SA) Creation

```bash
kubectl create serviceaccount sam --namespace default
kubectl create clusterrolebinding sam-clusteradmin-binding --clusterrole=cluster-admin --serviceaccount=default:sam
kubectl create token sam

# Set Token and API Server
TOKEN=outputfromabove
APISERVER=$(kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}')

# List Deployments
curl -X GET $APISERVER/apis/apps/v1/namespaces/default/deployments -H "Authorization: Bearer $TOKEN" -k

# Create Deployment
curl -X POST $APISERVER/apis/apps/v1/namespaces/default/deployments \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d @deploy.json \
  -k

# List Pods
curl -X GET $APISERVER/api/v1/namespaces/default/pods \
  -H "Authorization: Bearer $TOKEN" \
  -k
```

---

## YAML, Pod, Pod lifecycle, init containers, sidecar containers




