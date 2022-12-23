# Kubernetes training


## Dag 0
ter voorbereiding
* alvast door de basics van kubernetes, als je zin hebt


## Dag 1

* Theorie 
  * inleiding k8s
  * desired state vs current state
  * workloads: pods, deployments, statefullset, deamonset, Job, CronJob.
  * Deployment methodes, rolling update etc.
  * autoscaling / loadbalancer
  * Services (Expose app publicly)

* Handson
  * cronjob - voor trainen model
  * deployment – je eigen prediction API (Op een public cloud)
  * spelen met kubeapi
  * expose app publicly
  * Horizontal pod autoscaler
  * Deployment zonder downtime

## Dag 2

Theorie
* componenten: kubeapi, etcd, nodes, operators, ...
* namespaces
* configmaps
* volumes
* Kubernetes in het werkveld.
  * Sven bij Eneco
  * Bol.com
  * Politie


* Handson
    * statefullset - Postgres – database
    * connecten met API





## Mogelijke onderwerpen
* security
  * hoe kan je pods afschermen? 
  * ingres

* geavanceerdere exercise 
* secrets
* vault

## inspiratie
- https://kubernetes.io/docs/tutorials/services/
- https://kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/cluster-interactive/