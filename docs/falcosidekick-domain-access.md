# Falcosidekick UI Domain Access

This guide exposes the Falcosidekick UI through the Cloudflare-managed hostname:

```text
falco.caremedix.net
```

The UI is currently available locally with:

```text
http://localhost:2802/login
```

After ingress and DNS are configured, it should be available at:

```text
http://falco.caremedix.net/login
```

## Architecture

```text
Browser
  -> Cloudflare DNS
  -> public AWS load balancer created by Kubernetes ingress
  -> Falcosidekick UI Service
  -> Falcosidekick UI Pod
```

Do not point public Cloudflare DNS at private addresses such as `192.168.x.x`, `10.x.x.x`, or `172.16.x.x`. Cloudflare must point to the public load balancer DNS name created by the Kubernetes ingress controller.

## Prerequisite

The EKS cluster must have an ingress controller that can create a public load balancer.

For AWS EKS, the expected controller is usually the AWS Load Balancer Controller. This project does not modify Terraform or install that controller automatically.

Check for an ingress controller:

```bash
kubectl get pods -A | grep -E 'aws-load-balancer-controller|ingress'
kubectl get ingressclass
```

## Helm Upgrade

The Falco Helm values enable ingress for the Falcosidekick UI host:

```text
falco.caremedix.net
```

Create the UI credential Secret before upgrading. The value must be in `username:password` format:

```bash
kubectl create secret generic falcosidekick-ui-auth \
  --namespace falco \
  --from-literal=FALCOSIDEKICK_UI_USER='<username>:<password>' \
  --dry-run=client -o yaml | kubectl apply -f -
```

Apply the Helm update manually:

```bash
helm upgrade --install falco falcosecurity/falco \
  --namespace falco \
  --values falco/helm/values.yaml \
  --set "falcosidekick.webui.redis.storageEnabled=false" \
  --set-file "customRules.custom-rules\\.yaml=falco/rules/custom-rules.yaml" \
  --wait
```

## Verify Kubernetes Ingress

Check the Falcosidekick UI service:

```bash
kubectl get svc -n falco falco-falcosidekick-ui
kubectl get endpoints -n falco falco-falcosidekick-ui
```

Check the ingress:

```bash
kubectl get ingress -n falco
kubectl describe ingress -n falco falco-falcosidekick-ui
```

Get the public load balancer DNS name:

```bash
kubectl get ingress -n falco falco-falcosidekick-ui \
  -o jsonpath='{.status.loadBalancer.ingress[0].hostname}{"\n"}'
```

The output should look similar to:

```text
k8s-falco-falcofal-1234567890.us-east-1.elb.amazonaws.com
```

If the output is empty, the ingress controller has not finished provisioning the load balancer or the ingress controller is missing/misconfigured.

## Cloudflare DNS

Create this DNS record in Cloudflare:

| Type | Name | Target | Proxy status |
| --- | --- | --- | --- |
| `CNAME` | `falco` | `<public-ingress-load-balancer-dns-name>` | `DNS only` for first validation |

Example:

```text
Type: CNAME
Name: falco
Target: k8s-falco-falcofal-1234567890.us-east-1.elb.amazonaws.com
Proxy status: DNS only
TTL: Auto
```

Use a `CNAME`, not an `A` record, because AWS load balancers provide DNS names and their backing IP addresses can change.

## Cloudflare Proxy Mode

Start with `DNS only` while validating ingress because it shows the direct AWS load balancer behavior and avoids Cloudflare masking origin errors.

Use `Proxied` only after you have a working HTTP/HTTPS origin and have decided how TLS should be handled:

- `DNS only`: Best for first setup, troubleshooting, and validating the AWS load balancer directly.
- `Proxied`: Use after validation if you want Cloudflare features such as CDN, WAF, access policies, and hidden origin DNS.

For production HTTPS, prefer Cloudflare SSL/TLS mode `Full (strict)` with a valid certificate on the ingress/load balancer. That usually means adding an ACM certificate to the AWS load balancer ingress or using another Kubernetes TLS approach. Do not use Cloudflare `Flexible` SSL for production security-sensitive access.

## Confirm Access

Wait for DNS to resolve:

```bash
dig +short falco.caremedix.net
```

Check the HTTP response:

```bash
curl -I http://falco.caremedix.net/login
```

Open the UI:

```text
http://falco.caremedix.net/login
```

Use the username and password stored in the `falcosidekick-ui-auth` Kubernetes Secret. Do not hardcode UI credentials in the repository.
