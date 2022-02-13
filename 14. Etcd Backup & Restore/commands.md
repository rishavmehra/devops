### Install ectdctl
    sudo apt  install etcd-client

### Backup 

##### snapshot backup with authentication
    ETCDCTL_API=3 etcdctl snapshot save /tmp/etcd-backup.db \
    --cacert /etc/kubernetes/pki/etcd/ca.crt \
    --cert /etc/kubernetes/pki/etcd/server.crt \
    --key /etc/kubernetes/pki/etcd/server.key

##### check snapshot status
    ETCDCTL_API=3 etcdctl --write-out=table snapshot status snapshotdb


### Restore

##### create restore point from the backup
    ETCDCTL_API=3 etcdctl snapshot restore /tmp/etcd-backup.db --data-dir /var/lib/etcd-backup

##### the restored files are located at the new folder /var/lib/etcd-backup, so now configure etcd to use that directory:
    vim /etc/kubernetes/manifests/etcd.yaml
