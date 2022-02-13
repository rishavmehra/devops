### Debug pod

##### start busybox in interactive mode
    kubectl run debug-pod --image=busybox -it 

##### check service name can be resolved
    nslookup nginx-service.default.svc.cluster.local
    nslookup nginx-service

##### access service ip returned by nslookup
    ping service-ip 

### Execute commands in pod from master node

##### ping service
    kubectl exec -it pod-name -- sh -c "ping nginx-service"

##### print all envs
    kubectl exec -it pod-name -- sh -c "printenv"

##### print all running ports
    kubectl exec -it pod-name -- sh -c "netstat -lntp"


### Jsonpath output format
    kubectl get node -o json
    kubectl get pod -o json 

##### for single pod
    kubectl get pod -o jsonpath='{.items[0].metadata.name}'

##### print for all pods
    kubectl get pod -o jsonpath='{.items[*].metadata.name}'

##### multiple attributes
    kubectl get pod -o jsonpath="{.items[*]['metadata.name', 'status.podIP']}"
    kubectl get pod -o jsonpath="{.items[*]['metadata.name', 'status.podIP', 'status.startTime']}"

##### print multiple attributes on new lines
    kubectl get pod -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.podIP}{"\n"}{end}'
    kubectl get pod -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.podIP}{"\t"}{.status.startTime}{"\n"}{end}'

### Custom columns output
    kubectl get pods -o custom-columns=POD_NAME:.metadata.name,POD_IP:.status.podIP,CREATED_AT:.status.startTime


### Debugging kubelet
    service kubelet status
    sudo vim /etc/systemd/system/kubelet.service.d/10-kubeadm.conf
    sudo systemctl daemon-reload
    sudo systemctl restart kubelet
    service kubelet status
