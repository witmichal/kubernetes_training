# ArgoCD in minikube Installation
```shell
# ArgoCD requires a namespace with its name
kubectl create ns argocd

# apply ArgoCD manifest installation file from ArgoCD github repository
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v3.1.7/manifests/install.yaml
```

### Verify installation
```shell
kubectl get all -n argocd
```

### Access web UI
```shell
kubectl port-forward svc/argocd-server -n argocd 8888:443
```

### Retrieve password from k8s secret
```shell
ARGO_PASS=$(kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo -n | xargs)
```

# ArgoCD CLI

### Install - MAC (m1 - ARM)
```shell
ARGO_VERSION="v3.1.7"
curl -sSL -o argocd https://github.com/argoproj/argo-cd/releases/download/$ARGO_VERSION/argocd-darwin-arm64
sudo install -m 555 argocd /usr/local/bin/argocd
rm argocd
```

### create an Application in ArgoCD

1. make the repository public in GH (https://github.com/witmichal/kubernetes_training)
2. execute `argocd app create`
```shell
argocd app create app-with-db \
--repo 'https://github.com/witmichal/kubernetes_training.git' \
--dest-namespace test \
--dest-server https://kubernetes.default.svc \
--path 04-k8s-with-schemed-db/k8s
```
