# Kubernetes training


## Dag 0
ter voorbereiding
* installatie minikube
* installatie extensies
* installeren poetry dependencies lokaal?

stap 1 en 2 en 3 van de readme

stuur een week van tevoren op de vrijdag (nodig) 



## Dag 1

* Theorie
  * inleiding k8s
  * desired state vs current state - declaratief (overlap met terraform)
  * workloads: pods, deployments, statefullset, deamonset, Job, CronJob.
  * Deployment methodes, rolling update etc.
  * Services (Expose app publicly)
  * loadbalancer
  * cronjob

* Handson
  * cronjob - voor trainen model
  * deployment – je eigen prediction API (Op een public cloud)
  * spelen met kubeapi
  * Deployment zonder downtime

## Dag 2

Theorie
* componenten: kubeapi, etcd, nodes, operators, ...
* namespaces
* configmaps
* volumes
* autoscaling + metrics - afhankelijk van voorbeeld
* secrets
* helm
* argocd - gaan we niet gebruiken in hands-on



* Kubernetes in het werkveld.
  * Sven bij Eneco
  * Bol.com
  * Politie


* Handson
    * statefullset - Postgres – database
    * connecten met API
    * Horizontal pod autoscaler - bjorn


## inspiratie
- https://kubernetes.io/docs/tutorials/services/
- https://kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/cluster-interactive/
