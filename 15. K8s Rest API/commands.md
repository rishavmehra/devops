### Access API through proxy
    kubectl proxy --port=8081 &
    curl http://localhost:8081/api/

### Access without kubectl proxy

##### create serviceaccount for myscript usage
    kubectl create serviceaccount myscript

##### create role with Deployment, Pod, Service permissions
    kubectl apply -f myscript-role.yml

##### add Binding for serviceaccount
    kubectl create rolebinding script-role-binding --role=script-role --serviceaccount=default:myscript

##### get config info from kubectl
    kubectl config view

##### set cluster location var
    APISERVER=https://172.31.44.88:6443

##### set token var from default token
    kubectl get serviceaccount myscript -o yaml
    kubectl get secret xxxxx -o yaml

    TOKEN=$(echo "token" | base64 --decode | tr -d "\n")


##### if we don't have the ca cert for curl, we can accept insecure, without providing curl client with ca certificate 
    curl -X GET $APISERVER/api --header "Authorization: Bearer $TOKEN" --insecure

##### if we don't want insecure connection, we can specify ca cert for curl providing curl with k8s ca certificate
    curl -X GET $APISERVER/api --header "Authorization: Bearer $TOKEN" --cacert /etc/kubernetes/pki/ca.crt


### Get data

##### main endpoint /api
    curl -X GET $APISERVER/api --header "Authorization: Bearer $TOKEN" --cacert /etc/kubernetes/pki/ca.crt

##### list all deployments
    curl -X GET $APISERVER/apis/apps/v1/namespaces/default/deployments --header "Authorization: Bearer $TOKEN" --cacert /etc/kubernetes/pki/ca.crt

##### list all services
    curl -X GET $APISERVER/api/v1/namespaces/default/services --header "Authorization: Bearer $TOKEN" --cacert /etc/kubernetes/pki/ca.crt

##### get a specific service or deployment
    curl -X GET $APISERVER/api/v1/namespaces/default/services/nginx-service --header "Authorization: Bearer $TOKEN" --cacert /etc/kubernetes/pki/ca.crt

##### get all pod names
    curl -X GET $APISERVER/api/v1/namespaces/default/pods/pod-name/logs --header "Authorization: Bearer $TOKEN" --cacert /etc/kubernetes/pki/ca.crt
