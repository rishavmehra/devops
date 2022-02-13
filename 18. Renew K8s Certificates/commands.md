##### check certificate expirations dates of all k8s certificates with kubeadm
    kubeadm certs --help
    kubeadm certs check-expiration

##### check expiration date of a certificate with openssl
    openssl x509 -in /etc/kubernetes/pki/apiserver.crt -text -noout

##### filter resulting cert for validity attribute plus 2 following lines
    openssl x509 -in /etc/kubernetes/pki/apiserver.crt -text -noout | grep Validity -A2
