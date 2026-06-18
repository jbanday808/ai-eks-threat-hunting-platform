# Software Supply Chain Security

Software supply chain security focuses on knowing what is in the codebase, what dependencies are included, and whether the final container image is safe enough to deploy.

## SBOM

The pipeline generates a CycloneDX SBOM as `sbom.json`. An SBOM helps teams identify software components and respond faster when a new vulnerability affects a package or base image.

## Dependency scanning

Trivy scans the repository filesystem for high and critical vulnerabilities. This catches dependency and configuration risk before the project builds a container image.

## Image scanning

The Docker image is scanned before it is pushed to Amazon ECR. If Trivy finds high or critical vulnerabilities, the push is blocked.

## Deployment trust

The deployment process improves trust by validating source code, generating an SBOM, scanning the container image, and only deploying an image that passed the configured checks.
