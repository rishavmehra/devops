### Set namespace to myapp
    kubectl config set-context --current --namespace=myapp
    kubectl get pod -o wide

### Before creating network policies

##### all of these works
    kubectl exec backend-7787844fc5-q2hkk -- sh -c 'nc -v db-ip-10.44.0.9 6379'
    kubectl exec frontend-7d7b95b577-6m7fp -- sh -c 'nc -v backend-ip-10.44.0.8 80'
    kubectl exec frontend-7d7b95b577-6m7fp -- sh -c 'nc -v db-ip-10.44.0.10 6379'
    kubectl exec database-7874cd5f45-jvr5z -- sh -c 'nc -v frontend-ip-10.44.0.6 3000'
    kubectl exec database-7874cd5f45-jvr5z -- sh -c 'nc -v backend-ip-10.44.0.8 80'

### After creating network policies

##### still works
    kubectl exec backend-7787844fc5-q2hkk -- sh -c 'nc -v db-ip-10.44.0.9 6379'
    kubectl exec frontend-7d7b95b577-6m7fp -- sh -c 'nc -v backend-ip-10.44.0.8 80'

##### don't work any more
    kubectl exec frontend-7d7b95b577-6m7fp -- sh -c 'nc -v db-ip-10.44.0.10 6379'
    kubectl exec database-7874cd5f45-jvr5z -- sh -c 'nc -v frontend-ip-10.44.0.6 3000'
    kubectl exec database-7874cd5f45-jvr5z -- sh -c 'nc -v backend-ip-10.44.0.8 80'
