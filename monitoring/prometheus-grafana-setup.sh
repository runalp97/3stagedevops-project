helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install monitor prometheus-community/kube-prometheus-stack
kubectl --namespace default port-forward svc/monitor-grafana 3000:80 &
