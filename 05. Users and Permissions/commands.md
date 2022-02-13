### Create client certificate

##### create 2048-bit RSA key
    openssl genrsa -out dev-tom.key 2048

##### create user Certificate Signing Request
    openssl req -new -key dev-tom.key -subj "/CN=tom" -out dev-tom.csr 

##### get the base64 encoded value of the csr file
    cat dev-tom.csr | base64 | tr -d "\n"

##### create CSR in k8s
    kubectl apply -f dev-tom-csr.yaml

##### review CSR
    kubectl get csr

##### approve CSR
    kubectl certificate approve dev-tom

##### get dev-tom's signed certificate
    kubectl get csr dev-tom -o yaml

##### save decoded cert to dev-tom.crt file

##### connect to cluster as dev-tom user
    kubectl --server={api-server-address} \
    --certificate-authority=/etc/kubernetes/pki/ca.crt \
    --client-certificate=dev-tom.crt \
    --client-key=dev-tom.key \
    get pods

##### create cluster role & binding
    kubectl create clusterrole dev-cr --dry-run=client -o yaml > dev-cr.yaml
    kubectl create clusterrolebinding dev-crb --dry-run=client -o yaml > dev-crb.yaml

##### check user permissions as dev-tom
    kubectl auth can-i get pod

##### check user permissions as admin
    kubectl auth can-i get pod —-as {user-name}


### Create Service Account with Permissions
    kubectl create serviceaccount jenkins-sa --dry-run=client -o yaml > jenkins-sa.yaml

    kubectl create role cicd-role

    kubectl create clusterrolebinding cicd-binding \
    --clusterrole=cicd-role \
    --serviceaccount=default:jenkins

### Access with service account token

    kubectl options

    kubectl --server $server \
    --certificate-authority /etc/kubernetes/pki/ca.crt \
    --token $token \
    --user jenkins \
    get pods
