# 📋 GH-200 CoHack Workshop Guide

> **Trainer:** Himanshu Kumar | **Format:** CoHack (Follow-Along + Team Projects)
> **Course:** GH-200: Automate Your Workflow with GitHub Actions

---

## 🎯 What is a CoHack?

A **CoHack** is a collaborative hackathon-style learning experience where:
- 🎤 The **trainer demos** each concept live (you watch & follow along)
- 💻 **Learners code** in real-time on their own forked repos
- 👥 **Teams collaborate** on capstone projects at the end
- 🏆 Teams **present & compete** for the highest score

### 📜 CoHack Rules
1. **Fork first** — always work on your own fork
2. **No copy-paste of final answers** — type it out, understand it
3. **Ask questions freely** — no silly questions in a CoHack!
4. **Help your team** — if you figure it out first, teach your teammates
5. **Commit often** — every enhancement = at least one commit
6. **Have fun** — the journey matters more than the destination! 🚀

---

## 🗓️ Day Schedule

| Time | Block | Description |
|------|-------|-------------|
| 09:30 – 10:00 | 🚀 Kickoff | Setup, fork repo, configure secrets |
| 10:00 – 11:30 | 📘 Module 1 | Enhancements 1–4 (Topics 1–7) |
| 11:30 – 11:45 | ☕ Break | — |
| 11:45 – 13:00 | 📙 Module 2 | Enhancements 5–7 (Topics 8–12) |
| 13:00 – 14:00 | 🍽️ Lunch | — |
| 14:00 – 15:30 | 📕 Module 3 | Enhancements 8–13 (Topics 13–26) |
| 15:30 – 15:45 | ☕ Break | — |
| 15:45 – 17:15 | 🏆 Projects | CoHack Projects 1 & 2 (Team time) |
| 17:15 – 17:30 | 🎤 Demo & Score | Teams present, scores announced |

---

## 🏆 Project 1: Dynamic GitHub Profile README

### 🎯 Objective
Build an automated GitHub Actions workflow that updates your profile README daily with live data.

### 📋 Requirements (must complete ALL for full marks)
- [ ] Workflow triggers on both `schedule` (daily) and `workflow_dispatch`
- [ ] `workflow_dispatch` has at least 2 inputs (e.g., theme + include_ascii)
- [ ] Uses `concurrency` to prevent duplicate runs
- [ ] Fetches live data using the GitHub REST API
- [ ] Uploads a stats file as an **artifact**
- [ ] Uses a **matrix strategy** to update different README sections
- [ ] Uses `needs` to enforce job sequence
- [ ] Uses `if` expression on at least one job
- [ ] Calls the **reusable notify workflow** on completion
- [ ] Uses the **custom ASCII banner action**
- [ ] Commits and pushes the updated README with `[skip ci]`

### 💡 Bonus Ideas
- Add GitHub Streak stats badge
- Display most recent commit message
- Add a motivational quote fetched from a public API
- Fancy table of your top repositories

### 📁 Key Files
```
.github/workflows/update-profile-readme.yml   ← Main workflow
.github/actions/ascii-banner/action.yml        ← Custom action
scripts/update-readme.sh                       ← Update script
README.md                                      ← Output file
```

---

## 🔄 Project 2: CI/CD Pipeline with Multi-Environment Deployment

### 🎯 Objective
Build a production-grade CI/CD pipeline that lints, tests, builds, and deploys a Python app
to staging and production environments with full governance controls.

### 📋 Requirements (must complete ALL for full marks)
- [ ] Workflow triggers on `push`, `pull_request`, `release`, and `workflow_dispatch`
- [ ] Uses `paths` filter so workflow only triggers on `src/` changes
- [ ] `workflow_dispatch` has `deploy_to` (choice) and `skip_tests` (boolean) inputs
- [ ] Uses `concurrency` with different behaviour for main vs feature branches
- [ ] **Lint job** runs flake8 on the Python code
- [ ] **Test job** uses matrix (2 OS × 2 Python versions, with 1 exclude)
- [ ] Test job uses `if: inputs.skip_tests != true`
- [ ] Test results uploaded as artifact with `if: always()`
- [ ] **Build job** creates a dist artifact
- [ ] **Deploy-staging** uses an `environment:` block and conditional `if:`
- [ ] **Deploy-production** uses an `environment:` block and conditional `if:`
- [ ] Calls the **reusable notify workflow** with `if: always()`
- [ ] At least one step uses `${{ github.sha }}` or another context value

### 💡 Bonus Ideas
- Add a code coverage report artifact
- Add a Slack/Teams notification step
- Implement a canary deployment step
- Add environment protection rules in GitHub Settings

### 📁 Key Files
```
.github/workflows/ci-cd-pipeline.yml          ← Main workflow
.github/workflows/reusable-notify.yml          ← Reusable workflow
src/app.py                                     ← Application code
src/test_app.py                               ← Test suite
```

---

## 🏅 Scoring Card (100 Points)

| Criterion | Points | Notes |
|-----------|--------|-------|
| Workflow runs successfully end-to-end ✅ | 20 pts | No red X marks! |
| `needs` used for correct job sequencing | 10 pts | DAG is correct |
| Matrix strategy implemented | 10 pts | At least 2 dimensions |
| Artifacts uploaded AND downloaded | 10 pts | Both directions |
| Secrets used correctly (masked in logs) | 10 pts | Not hardcoded |
| `if` expressions on jobs AND steps | 10 pts | At least 3 conditions |
| Reusable workflow called correctly | 10 pts | With inputs & secrets |
| Custom action used in at least one step | 5 pts | ascii-banner action |
| Creative README / unique extra feature 🎨 | 10 pts | Surprise us! |
| Clean YAML formatting & comments | 5 pts | Readable code |
| **Total** | **100 pts** | |

---

## 💡 Tips & Tricks

### 🐛 Debugging Tips
- Set `ACTIONS_STEP_DEBUG` secret to `true` for verbose logs
- Use `echo "::debug::Your message"` for debug-only output
- Use `echo "::warning::Message"` and `echo "::error::Message"` for annotations
- Check the **Actions tab → select run → expand steps** for full output

### ⚡ Common Gotchas
- **YAML indentation matters!** Use spaces, never tabs
- `needs:` can be a string or a list: `needs: build` or `needs: [build, test]`
- Context expressions use `${{ }}`, shell vars use `$VAR`
- `if:` expressions don't need `${{ }}` wrapper at the job level
- `workflow_call` workflows can't trigger other `workflow_call` workflows

### 🔑 Most Used Contexts
```yaml
${{ github.actor }}        # Who triggered the workflow
${{ github.sha }}          # Commit SHA
${{ github.ref_name }}     # Branch or tag name
${{ github.run_number }}   # Sequential run number
${{ runner.os }}           # ubuntu, Windows, macOS
${{ job.status }}          # success, failure, cancelled
${{ steps.<id>.outputs.<name> }}  # Output from a step
```

---

## 🔗 Quick Reference Links

| Resource | URL |
|---|---|
| 📘 GH-200 Course Page | https://aka.ms/CourseGH-200 |
| 📖 GitHub Actions Workflow Syntax | https://docs.github.com/actions/writing-workflows/workflow-syntax-for-github-actions |
| 🏪 Actions Marketplace | https://github.com/marketplace?type=actions |
| 🎓 GH-200 Study Guide | https://learn.microsoft.com/credentials/certifications/resources/study-guides/gh-200 |
| 🎬 GH-200 YouTube Series | https://www.youtube.com/playlist?list=PLahhVEj9XNTd5N_seZDoRXVIn6N1qAp-_ |
| 🛠️ GH-200 Demos Org | https://github.com/GH-200-Demos |
| 🔧 GitHub Context Reference | https://docs.github.com/actions/writing-workflows/choosing-what-your-workflow-does/accessing-contextual-information-about-workflow-runs |
| 🔐 Secrets Documentation | https://docs.github.com/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions |
