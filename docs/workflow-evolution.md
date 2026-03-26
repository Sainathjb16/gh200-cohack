# 📖 Workflow Evolution — Learning Journal

> Track the journey of `cohack-journey.yml` from a simple Hello World
> to a fully-featured, enterprise-grade GitHub Actions workflow.

---

## Enhancement 1 — Hello World
**Topics:** 1 (Create & Run Workflow), 2 (What are Actions)
**What was added:** A minimal `on: [push]` trigger with one job and one `run` step.
**Key Concepts:** Workflow file location, YAML syntax, triggers, `runs-on`, `steps`.
**Why it matters:** Every GitHub Actions workflow starts here. Understanding the anatomy
of a workflow file is the foundation of everything that follows.

---

## Enhancement 2 — Checkout Action
**Topics:** 3 (Core Components), 4 (Configure Checkout Action)
**What was added:** `actions/checkout@v4` step using `uses:` keyword.
**Key Concepts:** Marketplace actions, `uses` vs `run`, `$GITHUB_WORKSPACE`, actions/checkout.
**Why it matters:** Almost every real workflow needs to access repository code.
`checkout` is the most-used action on the entire GitHub Marketplace.

---

## Enhancement 3 — Multi-Line Commands & ASCII Art
**Topics:** 5 (Multi-Line Commands), 6 (Third-Party Libraries & ASCII Artwork Workflow)
**What was added:** Multi-line `run` block using `|`, `apt-get install figlet`, multiple `figlet` fonts.
**Key Concepts:** YAML block scalar (`|`), installing packages on ephemeral runners, `figlet` CLI tool.
**Why it matters:** Real automation often requires multi-step shell commands and
external tools. Runners are ephemeral — every run starts fresh.

---

## Enhancement 4 — Shell Script Execution
**Topics:** 7 (Executing Shell Scripts in Workflow)
**What was added:** `greet.sh` script with `chmod +x` and `./scripts/greet.sh` execution.
**Key Concepts:** `RUNNER_OS`, `GITHUB_ACTOR`, `GITHUB_SHA`, `GITHUB_REF_NAME`,
default environment variables, script permissions.
**Why it matters:** Complex logic belongs in scripts, not YAML. Separating concerns
makes workflows maintainable and testable locally.

---

## Enhancement 5 — Multiple Jobs & Sequential Execution
**Topics:** 8 (Multiple Jobs), 9 (Sequential Jobs with `needs`)
**What was added:** `build` and `test` jobs, `needs: setup` and `needs: build` chains.
**Key Concepts:** Parallel vs sequential execution, DAG (Directed Acyclic Graph),
`needs` keyword, job dependency chain.
**Why it matters:** Workflows model real pipelines. Jobs run independently on fresh
runners — `needs` is the only way to enforce order and share context.

---

## Enhancement 6 — Artifacts
**Topics:** 10 (Storing Workflow Data as Artifacts)
**What was added:** `actions/upload-artifact@v4` in build, `actions/download-artifact@v4` in test.
**Key Concepts:** Artifact storage, `retention-days`, cross-job data transfer,
artifact name uniqueness, zip packaging.
**Why it matters:** Jobs can't share a filesystem — artifacts are the bridge.
They also provide downloadable evidence of each build for auditing.

---

## Enhancement 7 — Variables & Secrets
**Topics:** 11 (Variables at Different Levels), 12 (Repository Level Secrets)
**What was added:** Workflow `env:`, job `env:`, step `env:`, `${{ secrets.MY_API_KEY }}`.
**Key Concepts:** Variable scope hierarchy (step < job < workflow < repo < org),
secret masking, `secrets` context, never hardcoding credentials.
**Why it matters:** Secure configuration management is critical in CI/CD.
GitHub automatically masks secret values in logs.

---

## Enhancement 8 — Rich Triggers
**Topics:** 13 (Triggering a Workflow), 24 (`workflow_dispatch` Inputs), 25 (Webhook Events)
**What was added:** `push` with `paths`, `pull_request` with `types`, `schedule` cron,
`workflow_dispatch` with `choice` and `boolean` inputs.
**Key Concepts:** Event types, activity types, path filters, cron syntax, input types.
**Why it matters:** Workflows should only run when relevant — over-triggering wastes
minutes and slows feedback loops.

---

## Enhancement 9 — Concurrency & Timeouts
**Topics:** 14 (Job Concurrency), 15 (Timeout for Jobs and Steps)
**What was added:** `concurrency` block with `cancel-in-progress: true`, `timeout-minutes`
at job and step level.
**Key Concepts:** Concurrency groups, run cancellation, preventing queue buildup,
runaway job protection.
**Why it matters:** Without concurrency controls, multiple rapid pushes create a
growing queue. Without timeouts, hung steps waste compute minutes forever.

---

## Enhancement 10 — Matrix Strategy
**Topics:** 16 (Matrix Strategy), 17 (Additional Matrix Configuration)
**What was added:** `strategy.matrix` with `os` and `python-version`, `exclude`,
`include`, `fail-fast: false`, `max-parallel`.
**Key Concepts:** Matrix dimensions, combinatorial job generation, selective
exclusion/inclusion, independent failure handling.
**Why it matters:** Testing across multiple environments catches compatibility issues
early — the matrix runs all combinations in parallel, saving time vs sequential runs.

---

## Enhancement 11 — Context & `if` Expressions
**Topics:** 18 (Access Workflow Context), 19 (`if` Expressions in Jobs)
**What was added:** `deploy` job with `if: github.event_name == 'push' && github.ref == ...`,
context echo steps, step-level `if: success()`, `if: failure()`, `if: always()`.
**Key Concepts:** `github`, `runner`, `steps` contexts, boolean expressions,
status check functions, conditional execution.
**Why it matters:** Context gives your workflow intelligence — run deployments only
on main, send alerts only on failure, always clean up resources.

---

## Enhancement 12 — Event Filters & Skipping
**Topics:** 20 (Workflow Event Filters & Activity Types), 21 (Cancelling & Skipping)
**What was added:** `paths-ignore`, branch name regex patterns, `types` activity filters,
`[skip ci]` commit message convention.
**Key Concepts:** Path filters, branch glob patterns, `[skip ci]` / `[skip actions]`,
`workflow_dispatch` manual cancel, `concurrency.cancel-in-progress`.
**Why it matters:** Fine-grained control prevents unnecessary runs — a README typo
fix shouldn't trigger a 30-minute test suite.

---

## Enhancement 13 — Debug Logging & REST API
**Topics:** 22 (Enable Step Debug Logging), 23 (Access Workflow Logs via REST API)
**What was added:** `RUNNER_DEBUG` echo, `ACTIONS_STEP_DEBUG` secret reference,
`curl` call to `github.com/repos/.../actions/runs/...` REST API endpoint.
**Key Concepts:** `ACTIONS_STEP_DEBUG` secret, `ACTIONS_RUNNER_DEBUG` secret,
`::debug::` workflow command, REST API authentication with `GITHUB_TOKEN`.
**Why it matters:** When workflows fail in production, debug logging and log
retrieval via API are essential for root-cause analysis and automation.
