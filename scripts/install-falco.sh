#!/usr/bin/env bash
set -euo pipefail

NAMESPACE="${NAMESPACE:-falco}"
RELEASE_NAME="${RELEASE_NAME:-falco}"
CHART_NAME="${CHART_NAME:-falcosecurity/falco}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
VALUES_FILE="${REPO_ROOT}/falco/helm/values.yaml"
RULES_FILE="${REPO_ROOT}/falco/rules/custom-rules.yaml"

command -v helm >/dev/null 2>&1 || {
  echo "helm is required but was not found in PATH" >&2
  exit 1
}

command -v kubectl >/dev/null 2>&1 || {
  echo "kubectl is required but was not found in PATH" >&2
  exit 1
}

helm repo add falcosecurity https://falcosecurity.github.io/charts
helm repo update

kubectl create namespace "${NAMESPACE}" --dry-run=client -o yaml | kubectl apply -f -

helm upgrade --install "${RELEASE_NAME}" "${CHART_NAME}" \
  --namespace "${NAMESPACE}" \
  --values "${VALUES_FILE}" \
  --set "falcosidekick.webui.redis.storageEnabled=false" \
  --set-file "customRules.custom-rules\\.yaml=${RULES_FILE}" \
  --wait

echo
echo "Falco installed in namespace: ${NAMESPACE}"
echo "View Falco logs:"
echo "  kubectl logs -n ${NAMESPACE} -l app.kubernetes.io/name=falco -c falco --tail=100 -f"
echo
echo "Open Falcosidekick UI locally:"
echo "  kubectl port-forward -n ${NAMESPACE} svc/${RELEASE_NAME}-falcosidekick-ui 2802:2802"
echo "  http://localhost:2802"
