#### If you get an error on creating ingress component related to "nginx-controller-admission" webhook, than manually delete the ValidationWebhook and try again. To delete the ValidationWebhook:
    kubectl get ValidatingWebhookConfiguration 
    kubectl delete ValidatingWebhookConfiguration {name}

[Link to a more detailed description of the issue](https://pet2cattle.com/2021/02/service-ingress-nginx-controller-admission-not-found)
