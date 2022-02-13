### Create shortcuts
    alias k=kubectl
    export do="--dry-run=client -o yaml"

### Imperative commands

##### create pod
    kubectl run mypod --image=nginx

##### create deployment 
    kubectl create deployment nginx-deployment --image=nginx --replicas=2

##### create service for your pod
    kubectl expose deployment nginx-deployment --type=NodePort --name=nginx-service

##### generate service config
    kubectl create service clusterip myservice --tcp=80:80 --dry-run=client -o yaml > myservice.yaml

##### with shortcut for dry output
    kubectl create service clusterip myservice --tcp=80:80 $do > myservice.yaml 
