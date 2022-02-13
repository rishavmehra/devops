##### print all pods with resource requests and limits 

    kubectl get pod -o jsonpath="{range .items[*]}{.metadata.name}{.spec.containers[*].resources}{'\n'}"
