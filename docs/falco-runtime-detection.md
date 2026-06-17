# Falco Runtime Detection

Phase 3 prepares Falco and Falcosidekick for Kubernetes runtime threat detection on the EKS cluster.

This phase does not deploy automatically. Run the install script manually after `kubectl` is connected to the EKS cluster.

## Components

| Component | Purpose |
| --- | --- |
| Falco | Runs as a DaemonSet and detects suspicious runtime behavior from Linux system calls. |
| Falcosidekick | Receives Falco events and forwards or stores them for downstream integrations. |
| Falcosidekick UI | Provides a simple web UI for reviewing Falco events during demos and testing. |
| Custom rules | Adds project-specific detections for shell, file access, and exec-like activity. |

## Custom Detections

| Rule | What it detects | MITRE ATT&CK |
| --- | --- | --- |
| `AI Shell Spawned Inside Container` | Shell process started inside a container. | Execution: `T1059` |
| `AI Read Sensitive Shadow File` | Read attempt against `/etc/shadow`. | Credential Access: `T1003` |
| `AI Write Under Etc In Container` | Write attempt under `/etc`. | Persistence / Defense Evasion: `T1037` |
| `AI Suspicious Kubernetes Exec Activity` | Shell activity commonly associated with `kubectl exec`. | Execution: `T1059` |

## Install

Configure kubeconfig for the EKS cluster first:

```bash
aws eks update-kubeconfig --region us-east-1 --name ai-eks-threat-hunting-platform
```

Install Falco, Falcosidekick, and the Falcosidekick UI:

```bash
chmod +x scripts/install-falco.sh
./scripts/install-falco.sh
```

## Verify

Check that the Falco pods are running:

```bash
kubectl get pods -n falco
kubectl get svc -n falco
```

View Falco alerts and runtime logs:

```bash
kubectl logs -n falco -l app.kubernetes.io/name=falco -c falco --tail=100 -f
```

View Falcosidekick logs:

```bash
kubectl logs -n falco -l app.kubernetes.io/name=falcosidekick --tail=100 -f
```

Open the Falcosidekick UI locally:

```bash
kubectl port-forward -n falco svc/falco-falcosidekick-ui 2802:2802
```

Then browse to:

```text
http://localhost:2802
```

Default demo credentials:

```text
admin:admin
```

## Test Detections

Run the test script:

```bash
chmod +x scripts/test-detections.sh
./scripts/test-detections.sh
```

The script creates a temporary BusyBox pod and triggers:

- Shell spawned inside a container
- Read of `/etc/shadow`
- Write under `/etc`
- Kubernetes exec-like shell activity

Watch Falco logs while running tests:

```bash
kubectl logs -n falco -l app.kubernetes.io/name=falco -c falco --tail=100 -f
```

Clean up test resources:

```bash
kubectl delete namespace falco-test
```
