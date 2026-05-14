# Git Workflow Standards

**Applies to:** All repositories in this portfolio  
**Model:** Trunk-based development with short-lived feature branches

---

## 1. Branching Strategy

```
main                    ← always deployable, protected branch
├── feat/short-description
├── fix/issue-or-description
├── chore/description
└── docs/description
```

- `main` is the single trunk. No long-lived `develop` or `staging` branches.
- Feature branches are deleted immediately after merge.
- Branch names are lowercase, hyphen-separated, and prefixed with type.
- Maximum branch lifetime: **3 working days**. If a branch lives longer, it needs to be broken down or rebased.

### Branch Name Format

```
<type>/<short-description>

feat/add-hl7-parser
fix/patient-id-null-ref
chore/update-ruff-config
docs/api-authentication-guide
```

---

## 2. Commit Messages

Format: **Conventional Commits** (`conventionalcommits.org`)

```
<type>(<optional scope>): <subject>

<optional body>

<optional footer>
```

### Types

| Type | When to use |
|---|---|
| `feat` | A new feature or capability |
| `fix` | A bug fix |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `perf` | A code change that improves performance |
| `test` | Adding or modifying tests |
| `docs` | Documentation changes only |
| `chore` | Dependency updates, config changes, CI tweaks |
| `ci` | Changes to CI/CD pipeline definitions |

### Rules

- Subject line: imperative mood, lowercase, no trailing period, ≤72 characters.
- Body: explain *why*, not *what*. Reference issue numbers if applicable.
- Breaking changes: add `!` after the type/scope and include `BREAKING CHANGE:` in the footer.

```
# Correct
feat(ingest): add HL7v2 ADT message parser

Parses A01/A03/A08 admission and discharge events from the upstream feed.
Required for the patient census pipeline milestone.

Closes #42

# Incorrect
Added HL7 parser
Fixed the bug
WIP
```

---

## 3. Pull Requests

- Every change to `main` goes through a PR — no direct pushes, even for minor fixes.
- PRs must pass all CI checks before merge. No merging with failing tests or linting errors.
- PR title follows the same Conventional Commits format as commit messages.
- Self-review is acceptable for solo repositories, but the PR must still be created (for traceability and CI gate enforcement).

### PR Description Template

```markdown
## What

<!-- One paragraph: what does this change do? -->

## Why

<!-- Why is this change needed? Link to issue, ticket, or design doc. -->

## How

<!-- Brief description of implementation approach. Call out any non-obvious decisions. -->

## Testing

<!-- What tests exist or were added? How was this verified? -->

## Checklist

- [ ] Tests pass locally
- [ ] Linting passes (`ruff check .` / `dotnet format --verify-no-changes`)
- [ ] New public APIs have docstrings / XML doc comments
- [ ] CLAUDE.md and standards docs updated if applicable
```

---

## 4. Merge Strategy

- **Squash merge** for feature branches with messy intermediate commits.
- **Merge commit** for branches where the individual commit history is meaningful (e.g., a multi-commit refactor with distinct logical steps).
- **Never rebase onto main** after a PR is opened — it rewrites history and invalidates reviewer comments.

---

## 5. Pre-Commit Hooks

All repositories use `pre-commit`. The configuration lives at `.pre-commit-config.yaml`. See [templates/project_init/.pre-commit-config.yaml](../templates/project_init/.pre-commit-config.yaml).

Install once per clone:

```bash
uv run pre-commit install
```

Hooks run automatically on `git commit`. To run manually across all files:

```bash
uv run pre-commit run --all-files
```

CI also runs pre-commit hooks to catch cases where a developer bypassed them.

---

## 6. Tagging and Versioning

Use semantic versioning (`semver.org`): `MAJOR.MINOR.PATCH`

- `MAJOR` — breaking change
- `MINOR` — new backwards-compatible feature
- `PATCH` — backwards-compatible bug fix

Tags are applied to `main` after a PR merge:

```bash
git tag -a v1.2.0 -m "feat: add HL7 parser and patient census pipeline"
git push origin v1.2.0
```

---

## 7. What Goes in `.gitignore`

Always exclude:

- Environment files (`.env`, `.env.local`, `.env.*`)
- Virtual environments (`.venv/`, `venv/`)
- Build artifacts (`dist/`, `build/`, `*.egg-info/`)
- IDE directories (`.idea/`, `.vscode/` — user-specific settings only; shared workspace settings may be committed)
- OS artifacts (`.DS_Store`, `Thumbs.db`)
- Secrets or credential files (`*.pem`, `*.key`, `credentials.json`)

The canonical `.gitignore` template is at [templates/project_init/.gitignore](../templates/project_init/.gitignore).
