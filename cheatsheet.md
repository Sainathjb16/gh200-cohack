# ⚡ GH-200 CoHack — GitHub Actions Cheat Sheet
> **Trainer:** Himanshu Kumar | **Course:** GH-200: Automate Your Workflow with GitHub Actions | **Date:** ___________

---

## 🏗️ 1. Workflow Anatomy

```yaml
name: My Workflow           # Workflow name (displayed in Actions tab)
on: [push]                  # Event trigger
env:                        # Workflow-level variables
  APP: "my-app"
jobs:
  my-job:                   # Job ID
    runs-on: ubuntu-latest  # Runner
    needs: other-job        # Dependency
    if: success()           # Condition
    timeout-minutes: 10     # Timeout
    env:                    # Job-level variables
      STAGE: "build"
    steps:
      - uses: actions/checkout@v4   # Marketplace action
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
      - name: Run Command   # Step name
        env:                # Step-level variable
          MY_VAR: "value"
        run: echo "Hello $MY_VAR"
```

**5-Level Hierarchy:** `Workflow` → `Event` → `Job` → `Step` → `Action`

---

## 📖 2. Key Syntax Reference

| Keyword | Purpose | Example |
|---------|---------|--------|
| `name:` | Display name | `name: 🚀 CI Pipeline` |
| `on:` | Trigger(s) | `on: [push, pull_request]` |
| `runs-on:` | Runner OS | `runs-on: ubuntu-latest` |
| `uses:` | Marketplace action | `uses: actions/checkout@v4` |
| `run:` | Shell command(s) | `run: echo "hello"` |
| `with:` | Action inputs | `with:` `  version: '3.11'` |
| `env:` (workflow) | All jobs see it | `env:` `  APP: "myapp"` |
| `env:` (job) | All steps in job | `env:` `  PHASE: "build"` |
| `env:` (step) | This step only | `env:` `  TOKEN: ${{ secrets.T }}` |
| `needs:` | Job dependency | `needs: [build, test]` |
| `if:` | Run condition | `if: github.ref == 'refs/heads/main'` |
| `timeout-minutes:` | Max run time | `timeout-minutes: 10` |
| `concurrency:` | Prevent duplicates | `group: ${{ github.ref }}` |
| `outputs:` | Share step values | `outputs:` `  sha: ${{ steps.x.outputs.sha }}` |
| `secrets:` | Encrypted values | `${{ secrets.MY_KEY }}` |
| `strategy.matrix:` | Multi-config jobs | `matrix:` `  os: [ubuntu, windows]` |

---

## 🔔 3. Triggers Quick Reference

| Trigger | When it Fires | Key Options |
|---------|--------------|-------------|
| `push` | On commit push | `branches:`, `paths:`, `tags:` |
| `pull_request` | On PR events | `types: [opened, synchronize]`, `branches:` |
| `schedule` | On cron timer | `cron: '0 9 * * 1'` *(Mon 9 AM)* |
| `workflow_dispatch` | Manual (Run button) | `inputs:` with `type: choice/boolean/string` |
| `release` | On release event | `types: [published, created]` |
| `workflow_call` | Called by another workflow | `inputs:`, `secrets:`, `outputs:` |

**Cron Mnemonic:** `Minute Hour DayOfMonth Month DayOfWeek` → **M**y **H**amster **D**rinks **M**ilk **D**aily

| Skip Trigger | How | Note |
|-------------|-----|------|
| Skip workflow | Add `[skip ci]` to commit message | Native GitHub feature, no config needed |
| Ignore paths | `paths-ignore: ['**.md']` | Can't combine with `paths:` |
| Limit branch | `branches: [main, 'feature/**']` | Glob patterns supported |

---

## 🌐 4. GitHub Contexts  *(use inside `${{ }}` expressions)*

| Context | Key Properties | Example |
|---------|---------------|--------|
| `github` | `actor` · `sha` · `ref_name` · `event_name` · `run_number` · `repository` · `workflow` · `ref` | `${{ github.actor }}` |
| `runner` | `os` · `arch` · `temp` · `tool_cache` | `${{ runner.os }}` |
| `steps` | `<id>.outputs.<name>` · `<id>.outcome` · `<id>.conclusion` | `${{ steps.build.outputs.version }}` |
| `secrets` | `<SECRET_NAME>` · `GITHUB_TOKEN` *(auto)* | `${{ secrets.MY_API_KEY }}` |
| `needs` | `<job>.outputs.<name>` · `<job>.result` | `${{ needs.build.outputs.sha }}` |
| `inputs` | `<input_name>` *(workflow_dispatch/call)* | `${{ inputs.environment }}` |
| `env` | `<VAR_NAME>` | `${{ env.APP_NAME }}` |
| `job` | `status` | `${{ job.status }}` |

---

## ✅ 5. Status Check Functions  *(use in `if:` conditions)*

| Function | Meaning | Best Used On |
|----------|---------|-------------|
| `success()` | All previous steps/jobs succeeded *(default)* | Deploy steps, publish steps |
| `failure()` | At least one previous step/job failed | Alert/notification steps |
| `always()` | Run regardless of outcome | Cleanup steps, teardown |
| `cancelled()` | Workflow was manually cancelled | Rollback steps |

```yaml
- name: Cleanup          # Runs no matter what
  if: always()
  run: echo "cleaning up"
- name: Alert on failure # Only on failure
  if: failure()
  run: echo "something broke!"
```

---

## 🌿 6. Default Environment Variables  *(available in every step)*

| Variable | Contains | Example Value |
|----------|----------|---------------|
| `GITHUB_ACTOR` | Username who triggered the run | `himanshu-kumar` |
| `GITHUB_SHA` | Full commit SHA | `abc123def456...` |
| `GITHUB_REF_NAME` | Branch or tag name | `main` |
| `GITHUB_REPOSITORY` | `owner/repo` | `org/gh200-cohack` |
| `GITHUB_WORKFLOW` | Workflow display name | `🚀 CoHack Journey` |
| `GITHUB_RUN_NUMBER` | Sequential run count | `42` |
| `GITHUB_RUN_ID` | Unique run identifier (for REST API) | `9876543210` |
| `GITHUB_EVENT_NAME` | Triggering event | `push` |
| `GITHUB_WORKSPACE` | Path to checked-out repo | `/home/runner/work/repo` |
| `GITHUB_TOKEN` | Auth token (auto-generated) | `ghp_xxx...` *(masked)* |
| `RUNNER_OS` | Runner operating system | `Linux` |
| `RUNNER_ARCH` | Runner CPU architecture | `X64` |

---

## 💬 7. Expression Syntax — When to Use What

| Syntax | Use For | Example |
|--------|---------|--------|
| `$VAR` | Shell/env variable in `run:` | `echo $GITHUB_ACTOR` |
| `${{ github.* }}` | GitHub context in `if:`, `run:`, `with:` | `${{ github.sha }}` |
| `${{ env.VAR }}` | Env var in expression context | `${{ env.APP_NAME }}` |
| `${{ secrets.NAME }}` | Encrypted secret | `${{ secrets.API_KEY }}` |
| `${{ inputs.NAME }}` | workflow_dispatch / workflow_call input | `${{ inputs.environment }}` |
| `${{ matrix.prop }}` | Matrix dimension value | `${{ matrix.os }}` |
| `${{ steps.ID.outputs.KEY }}` | Step output value | `${{ steps.build.outputs.ver }}` |
| `${{ needs.JOB.outputs.KEY }}` | Job output from dependency | `${{ needs.build.outputs.sha }}` |

> **⚠️ Rule:** `if:` at **job level** → no `${{ }}` needed. `if:` at **step level** → use `${{ }}` for complex expressions.

---

## 📦 8. Artifact Actions Quick Reference

```yaml
# UPLOAD (in producer job)
- uses: actions/upload-artifact@v4
  with:
    name: build-output       # Must match download name exactly
    path: dist/              # File or folder to upload
    retention-days: 5        # Default: 90 days

# DOWNLOAD (in consumer job — must have needs: producer)
- uses: actions/download-artifact@v4
  with:
    name: build-output       # Must match upload name exactly
    path: ./downloaded/      # Where to put it (optional)
```

---

## 🔢 9. Matrix Strategy Quick Reference

```yaml
strategy:
  fail-fast: false          # Don't cancel all if one fails
  max-parallel: 3          # Max concurrent jobs
  matrix:
    os: [ubuntu-latest, windows-latest]
    python: ['3.10', '3.11', '3.12']
    exclude:
      - os: windows-latest  # Skip windows + 3.10
        python: '3.10'
    include:
      - os: ubuntu-latest   # Add extra property to this combo
        python: '3.12'
        experimental: true
runs-on: ${{ matrix.os }}   # Reference matrix value
```

> **Formula:** `Total jobs = (rows × cols) - excludes + includes`

---

## ♻️ 10. Reusable Workflow vs Custom Action

| | Reusable Workflow | Custom Action |
|--|-------------------|---------------|
| **File location** | `.github/workflows/*.yml` | `.github/actions/<name>/action.yml` |
| **Trigger** | `on: workflow_call` | `uses: ./.github/actions/<name>` |
| **How called** | `uses: ./.github/workflows/notify.yml` | `uses: ./.github/actions/banner` |
| **Inputs** | `inputs:` under `workflow_call` | `inputs:` in `action.yml` |
| **Secrets** | `secrets:` under `workflow_call` | Inherited from parent workflow |
| **Best for** | Entire job sequences (lint+test+deploy) | Single reusable step logic |
| **Types** | N/A | `composite`, `javascript`, `docker` |

---

## 🐛 11. Common Errors & Fixes

| ❌ Error / Symptom | 🔍 Likely Cause | ✅ Fix |
|-------------------|-----------------|--------|
| `Invalid workflow file` / YAML parse error | Tabs used instead of spaces, or wrong indentation level | Use 2 spaces; validate at [yaml.lint](https://www.yamllint.com) |
| Workflow not triggering at all | Branch name doesn't match `branches:` filter, or `paths:` filter excludes the changed file | Check `on:` block; remove `paths:` filter temporarily to test |
| `workflow_dispatch` Run button missing | Workflow file is not on the **default branch** | Merge the workflow file to `main` first |
| `No such file or directory` in run step | `actions/checkout` step is missing | Add `uses: actions/checkout@v4` as first step |
| Artifact download fails | Name mismatch between `upload-artifact` and `download-artifact` | Ensure `name:` is **exactly** the same (case-sensitive) |
| Secret value appears in plain text in logs | Secret assigned to workflow-level `env:` | Move secret to **step-level** `env:` only |
| Job shows as **skipped** (grey) | `if:` condition evaluated to `false` | Echo the condition value first to debug: `run: echo ${{ github.ref }}` |
| `needs: circular dependency` error | Job A needs B, and B needs A | Review dependency chain; break the cycle |
| `apt-get: command not found` | Running on `windows-latest` or `macos-latest` runner | Use `ubuntu-latest` for apt-get commands |
| `[skip ci]` not working | Commit message format wrong | Must be exactly `[skip ci]` or `[skip actions]` in the commit message |
| Matrix not creating expected jobs | Syntax error inside `matrix:` block | Check indentation; `exclude:`/`include:` must be at same level as matrix keys |
| Job times out unexpectedly | `timeout-minutes` set too low for the actual task duration | Increase timeout; check if a step is hanging |
| `Context access might be invalid` warning | Typo in context property name | Check [docs.github.com/actions/contexts](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/accessing-contextual-information-about-workflow-runs) |

---

## 🔄 12. Concurrency & Timeout Patterns

```yaml
# Safe pattern: cancel feature branches, protect main
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: ${{ github.ref != 'refs/heads/main' }}

# Timeout at job AND step level
jobs:
  build:
    timeout-minutes: 15     # Entire job limit
    steps:
      - name: Slow network call
        timeout-minutes: 3  # This step specifically
        run: curl https://api.example.com/data
```

---

## 🏆 13. Golden Rules

1. 🗂️ **Workflow files live in `.github/workflows/`** — filename must end in `.yml` or `.yaml`
2. ↔️ **Indentation = 2 spaces** — never tabs; YAML will silently break
3. 📥 **Always checkout first** — runners have no repo files by default
4. 🔐 **Secrets at step-level only** — never at workflow `env:` level
5. 🔗 **Each job = fresh runner** — jobs can't share files without artifacts
6. 📌 **Pin action versions** — use `@v4` not `@latest` in production
7. ⛔ **[skip ci] in commit message** — skips the run natively, no config needed
8. 🧪 **`fail-fast: false` in matrix** — see ALL failures, not just the first

---

## 🎓 14. Certification & Resources

| Resource | URL |
|----------|-----|
| 📘 GH-200 Course Page | https://aka.ms/CourseGH-200 |
| 📖 GitHub Actions Docs | https://docs.github.com/actions |
| 🎓 GH-200 Study Guide | https://learn.microsoft.com/credentials/certifications/resources/study-guides/gh-200 |
| 🎬 GH-200 YouTube Series | https://www.youtube.com/playlist?list=PLahhVEj9XNTd5N_seZDoRXVIn6N1qAp-_ |
| 🛠️ GH-200 Demos Org | https://github.com/GH-200-Demos |
| 🛒 Actions Marketplace | https://github.com/marketplace?type=actions |
| ✅ YAML Linter | https://www.yamllint.com |
| ⏱️ Cron Validator | https://crontab.guru |

---
*🤖 GH-200 CoHack | Trainer: Himanshu Kumar | github.com/GH-200-Demos*
