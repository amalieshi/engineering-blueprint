# YAML Best Practices

**Applies to:** CI/CD pipelines, Docker Compose, Kubernetes manifests, dbt configurations, Airflow DAG configs, and all other YAML-driven tooling.

---

## 1. Core Principles

YAML's flexibility is its biggest liability. Configuration drift — where different environments diverge silently — is one of the most common root causes of production incidents in data pipelines. The rules below enforce legibility and traceability.

**The golden rule:** YAML is executable documentation. Treat it as code. It goes through code review, it is linted, and it is schema-validated.

---

## 2. Formatting Rules

| Rule | Rationale |
|---|---|
| Use 2-space indentation, never tabs | Tabs are not valid YAML in most parsers |
| Limit lines to 120 characters | Beyond this, readability collapses |
| Use lowercase keys | Mixed case is inconsistent across tooling |
| Use `_` (snake_case) for multi-word keys | Matches Python conventions; avoid `-` in keys |
| Prefer block style over flow style for structures | `{key: val}` is harder to diff than block form |
| Always quote strings that could be misinterpreted | `"true"`, `"1.0"`, `"null"` must be quoted if string-typed |

```yaml
# Correct
environment:
  database_host: "postgres.internal"
  max_connections: 20
  enable_ssl: true

# Incorrect — flow style, unquoted ambiguous values, mixed casing
environment: {DatabaseHost: postgres.internal, MaxConnections: 20, EnableSSL: True}
```

---

## 3. Comments are Mandatory for Non-Standard Values

Any key whose value is non-obvious must have an inline or preceding comment explaining the reason.

```yaml
resources:
  limits:
    memory: "512Mi"
    cpu: "500m"        # 0.5 vCPU — sized for burst processing, not sustained load
  requests:
    memory: "256Mi"
    cpu: "100m"

retry_delay_seconds: 300  # 5 minutes — matches the upstream API's rate-limit reset window
```

Do not comment self-evident values (`port: 5432  # postgres port`). Comment the *why*, not the *what*.

---

## 4. Schema Validation

Every YAML file with a defined schema must be validated in CI before merge. Use the appropriate tool for the domain:

| Domain | Validation tool |
|---|---|
| Kubernetes manifests | `kubeval` or `kubeconform` |
| GitHub Actions workflows | `actionlint` |
| JSON Schema-backed configs | `check-jsonschema` |
| dbt `schema.yml` | `dbt parse` or `dbt compile` |
| Docker Compose | `docker compose config` |
| Generic | `yamllint` for syntax; `check-jsonschema` for structure |

Add a pre-commit hook:

```yaml
# .pre-commit-config.yaml
- repo: https://github.com/adrienverge/yamllint
  rev: v1.35.1
  hooks:
    - id: yamllint
      args: [--config-file, .yamllint.yaml]

- repo: https://github.com/python-jsonschema/check-jsonschema
  rev: 0.29.4
  hooks:
    - id: check-github-workflows
    - id: check-github-actions
```

---

## 5. Secrets and Sensitive Values

**Never** commit plaintext secrets to YAML files. Use references to secrets managers or environment variable substitution.

```yaml
# Correct — reference injected at runtime
database:
  password: "${DB_PASSWORD}"          # env var injected by CI or secrets manager
  connection_string: "${DB_CONN_STR}"

# Incorrect — hardcoded credential
database:
  password: "my_prod_password_123"
```

For Kubernetes, reference `Secret` objects:

```yaml
env:
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: db-credentials
        key: password
```

---

## 6. Anchors and Aliases

Use YAML anchors (`&`) and aliases (`*`) to avoid repeating configuration blocks. Document the anchor clearly.

```yaml
# Shared resource allocation for lightweight services
x-small-resources: &small-resources
  limits:
    memory: "128Mi"
    cpu: "100m"
  requests:
    memory: "64Mi"
    cpu: "50m"

services:
  health-checker:
    image: myapp/health:latest
    resources: *small-resources

  metrics-exporter:
    image: myapp/metrics:latest
    resources: *small-resources
```

Do not abuse anchors to the point where the file requires mental deserialization to read. If the shared block is more than ~10 lines, consider whether a templating tool (Helm, Jinja2, jsonnet) is more appropriate.

---

## 7. GitHub Actions Specific Rules

- Pin third-party actions to a full SHA commit hash, not a mutable tag.
- Use `permissions:` blocks to apply least-privilege to each job.
- Extract repeated step sequences into reusable workflows.

```yaml
# Correct — pinned SHA prevents supply-chain injection
- uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683  # v4.2.2

# Incorrect — mutable tag, can be overwritten
- uses: actions/checkout@v4

jobs:
  build:
    permissions:
      contents: read       # only what this job needs
      packages: write
```

---

## 8. dbt YAML Rules

- Every source table must have a `description` and at minimum a `not_null` and `unique` test on the primary key.
- Column descriptions must be populated — use `doc()` blocks for reusable descriptions on shared columns (e.g., `updated_at`, `created_by`).
- Do not use the generic `schema.yml` filename. Name files by domain: `patients.yml`, `encounters.yml`.

```yaml
version: 2

models:
  - name: stg_patients
    description: "Cleaned and standardised patient demographics from the source EHR system."
    columns:
      - name: patient_id
        description: "Surrogate key — SHA-256 hash of source system patient MRN."
        data_tests:
          - not_null
          - unique
      - name: date_of_birth
        description: "Patient date of birth in ISO 8601 format (YYYY-MM-DD)."
        data_tests:
          - not_null
```

---

## 9. Linter Configuration

Place `.yamllint.yaml` at the repository root:

```yaml
extends: default

rules:
  line-length:
    max: 120
  comments:
    min-spaces-from-content: 2
  truthy:
    allowed-values: ["true", "false"]   # disallow Yes/No/On/Off
  indentation:
    spaces: 2
    indent-sequences: true
```
