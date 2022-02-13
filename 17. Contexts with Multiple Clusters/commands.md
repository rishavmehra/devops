##### all context commands
    kubectl config --help

##### show all contexts
    kubectl config get-contexts

##### show current context
    kubectl config current-context

##### switch to another context
    kubectl set-context context-name

##### change user or cluter name for any context
    kubectl config set-context --help
    kubectl config set-context context-name --user=user_name --cluster=cluster_name

##### change user or cluster for current context
    kubectl config set-context --current --user=user_name --cluster=cluster_name

##### change default namespace
    kubectl get pod
    kubectl config set-context --current --namespace=myapp
    kubectl get pod

