# DevOps

## Kubernetes

📄 **Reference:**  
- [📌 kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/quick-reference/)  
- [📘 Pods Documentation](https://kubernetes.io/docs/concepts/workloads/pods/)

---

## 🔧 Exercise 1: Working with Pods (Declarative Only)

### 🎯 Task:
> Create a **Pod** in the **default namespace** using a YAML file with the following specifications:
>
> - Use any **container image** of your choice.
> - The pod must have **2 containers**.
> - After applying the YAML, **verify** that the pod is running.

### 📂 Solution:
👉 [00. Exercises/Pod/Pod.yaml](00.%20Exercises/Pod/Pod.yaml)

---
# HELM
[Cheat Sheet](https://helm.sh/docs/intro/cheatsheet/)
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