# Introduction
This example deploys a horizontally scalable application.

# Instructions

1. We start with enabling the metrics server in minikube. By default it's turned off but it is neccessary to monitor the resources (like cpu and ram) a pod uses. A horizontalPodAutoscaler needs that information the decide whether it should scale up or down an application.
    ```
    minikube addons enable metrics-server
    ```

1. Check if the metrics-server is enabled.
    ```
    minikube addons list
    ```

1. Have a look at the `k8s-deployment/scaling/deployment.yaml` and `k8s-deployment/scaling/service.yaml` and apply them to the cluster.
    
    How many pods are created by the deployment?

1. Examine `k8s-deployment/scaling/hpa.yaml` and apply the HorizontalPodAutoscaler to the cluster.

    As you may notice, the deployment in the cluster now differece from the version you applied to the cluster.

1. Now we are going to increase the load to the pods of our deployment, and see how this effects the replicas. You can monitor the pods in your cluster with the kubernetes dashboard or on the command line.

    Increase the load:
    ```
    kubectl run -i --tty load-generator --rm --image=busybox:1.28 --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://php-apache; done"

    ```

    Decrease the load by interupting the command with `CTRL-C`.








# Links
* [hpa blogpost example](https://www.bogotobogo.com/DevOps/Docker/Docker-Kubernetes-Horizontal-Pod-Autoscaler.php)
* [kubernetes docs hpa example](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/)
