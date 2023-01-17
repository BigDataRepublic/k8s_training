# 1️⃣ Setup
### ZSH autocompletions
Add the two following lines at the end of your ~/.zshrc file then reopen a new terminal:
```
[[ $commands[kubectl] ]] && source <(kubectl completion zsh)
[[ $commands[minikube] ]] && source <(minikube completion zsh)
```

If you type minikube <TAB> or kubectl <TAB> it should give you a list of commands

Furthermore, install the dependencies using Poetry:
```
pip install poetry
poetry install
poetry shell
```

### VScode Extensions
Before you get started there are some key extensions we need for VSCode to make developing k8s a breeze 🥶. Make sure you have Kubernetes, Kubernetes templates, and YAML - all highlighted in the image below 👇.

![alt text](pictures/extensions.png)


# 2️⃣ Launching Minikube
The first step is to make sure that your Docker daemon is running. One way to do this is to start Docker Desktop on your machine. Then run the following command from your terminal:
```bash
minikube start
```

Starting minikube can take a few minutes. You should get the following message:
```bash
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
```

This means that you are now able to interact with the minikube cluster using `kubectl`. One thing that we can do is to inspect the cluster node:
```bash
kubectl get node
```

You should see something like:
```
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   76d   v1.25.2
```

# 3️⃣ Build and run docker images inside your cluster
❓ Use the following command to build and run docker image inside the `minikube` environment:
```bash
eval $(minikube docker-env)
```

See the [following](https://stackoverflow.com/questions/52310599/what-does-minikube-docker-env-mean) Stackoverflow page for a more elaborate explanation of this.

❓ Now build the Dockerfile against the docker inside Minikube, which is instantly accessible to Kubernetes cluster.
```
docker build -t app .
```

# 4️⃣ Create a K8s Service
❓ Create your own `service.yaml` and populate it with a `LoadBalancer` service, with name `fastapi-service` and selector app: `fastapi`. What port should you it target ?

<details>
  <summary markdown='span'> 💡 Target hint </summary>
    The target port should correspond to the port on which you are exposing your Fastapi application.
</details>
