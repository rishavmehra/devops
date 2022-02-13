### Provision Infrastructure 

##### move private key to .ssh folder and restrict access
    mv ~/Downloads/k8s-node.pem ~/.ssh
    chmod 400 ~/.ssh/k8s-node.pem

##### ssh into ec2 instance with its public ip
    ssh -i ~/.ssh/k8s-node.pem ubuntu@35.180.130.108


### Configure Infrastructure
    sudo swapoff -a

##### set host names of nodes
    sudo vim /etc/hosts

##### get priavate ips of each node and add this to each server 
    45.14.48.178 master
    45.14.48.179 worker1
    45.14.48.180 worker2

##### we can now use these names instead of typing the IPs, when nodes talk to each other. After that, assign a hostname to each of these servers.

##### on master server
    sudo hostnamectl set-hostname master 

##### on worker1 server
    sudo hostnamectl set-hostname worker1 

##### on worker2 server
    sudo hostnamectl set-hostname worker2


### Initialize K8s cluster
    sudo kubeadm init

### Check kubelet process running 
    service kubelet status
    systemctl status kubelet

### Check extended logs of kubelet service
    journalctl -u kubelet

### Access cluster as admin
    mkdir -p $HOME/.kube
    sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    sudo chown $(id -u):$(id -g) $HOME/.kube/config

### Kubectl commands

##### get node information
    kubectl get node

##### get pods in kube-system namespace
    kubectl get pod -n kube-system

##### get pods from all namespaces
    kubectl get pod -A

##### get wide output
    kubectl get pod -n kube-system -o wide


### Install pod network plugin

##### download the manifest
    wget "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')" -O "weave.yaml"

##### check weave net status
    kubectl exec -n kube-system weave-net-1jkl6 -c weave -- /home/weave/weave --local status

### Join worker nodes

##### create and execute script
    vim install-containerd.sh
    chmod u+x install-containerd.sh
    ./install-containerd.sh

##### on master
    kubeadm token create --help
    kubeadm token create --print-join-command

##### copy the output command and execute on worker node as ROOT
    sudo kubeadm join 172.31.43.99:6443 --token 9bds1l.3g9ypte9gf69b5ft --discovery-token-ca-cert-hash sha256:xxxx

##### start a test pod
    kubectl run test --image=nginx


