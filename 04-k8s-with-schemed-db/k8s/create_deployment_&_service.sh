set -e

# cleanup
__dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source ${__dir}/cleanup.sh ## the same process

kubectl create -f ./secret.yaml
kubectl create -f ./deployment.yaml
kubectl wait --for=jsonpath='{.status.conditions[?(@.type=="Available")].status}'=True -f ./deployment.yaml
kubectl create -f ./service.yaml

echo
echo "stream logs (-f, --follow is for opening a stream):"
echo "# k logs -f -n test services/app-with-db"
echo
echo "CTRL+C to kill the tunnel process"
echo "hit 'curl 127.0.0.1:6666' in separate shell"
echo

kubectl port-forward service/app-with-db -n test 6666:5555
