# Kubernetes
---
### HELM
```
// Install a chart from a local directory
helm create mychart
helm install mychartrelease mychart

// Uninstall a release
helm uninstall mychartrelease

// List releases
helm list -a

// upgrade the the helm chart
helm upgrade mychartrelease mychart

// rollback to a previous version
helm rollback mychartrelease 1

// debug
helm install --dry-run --debug mychartrelease mychart

// helm template
helm template mychart


// helm lint
helm lint mychart

```