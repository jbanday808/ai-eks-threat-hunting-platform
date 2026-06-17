#!/usr/bin/env bash
set -euo pipefail

NAMESPACE="${NAMESPACE:-falco-test}"
POD_NAME="${POD_NAME:-falco-detection-test}"

command -v kubectl >/dev/null 2>&1 || {
  echo "kubectl is required but was not found in PATH" >&2
  exit 1
}

kubectl create namespace "${NAMESPACE}" --dry-run=client -o yaml | kubectl apply -f -

kubectl delete pod "${POD_NAME}" -n "${NAMESPACE}" --ignore-not-found=true

kubectl run "${POD_NAME}" \
  --namespace "${NAMESPACE}" \
  --image=busybox:1.36 \
  --restart=Never \
  --command -- sh -c "sleep 300"

kubectl wait --for=condition=Ready "pod/${POD_NAME}" -n "${NAMESPACE}" --timeout=90s

echo "Triggering shell spawned inside container..."
kubectl exec -n "${NAMESPACE}" "${POD_NAME}" -- sh -c "echo shell-test"

echo "Triggering /etc/shadow read..."
kubectl exec -n "${NAMESPACE}" "${POD_NAME}" -- sh -c "cat /etc/shadow >/dev/null 2>&1 || true"

echo "Triggering write under /etc..."
kubectl exec -n "${NAMESPACE}" "${POD_NAME}" -- sh -c "echo falco-test > /etc/falco-phase3-test"

echo
echo "Detection test commands completed."
echo "View Falco logs:"
echo "  kubectl logs -n falco -l app.kubernetes.io/name=falco -c falco --tail=100 -f"
echo
echo "Clean up the test pod:"
echo "  kubectl delete namespace ${NAMESPACE}"
