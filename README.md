<!-- Dynamic Profile README Placeholder — updated by GitHub Actions 🤖 -->
<!-- ╔══════════════════════════════════════════════════════╗ -->
<!-- ║  AUTO-UPDATED SECTION START (do not edit manually)  ║ -->
<!-- ╚══════════════════════════════════════════════════════╝ -->

# 🚀 GH-200 CoHack Starter Repository

[![CoHack Journey](https://github.com/<YOUR-USERNAME>/gh200-cohack/actions/workflows/cohack-journey.yml/badge.svg)](https://github.com/<YOUR-USERNAME>/gh200-cohack/actions/workflows/cohack-journey.yml)
[![CI/CD Pipeline](https://github.com/<YOUR-USERNAME>/gh200-cohack/actions/workflows/ci-cd-pipeline.yml/badge.svg)](https://github.com/<YOUR-USERNAME>/gh200-cohack/actions/workflows/ci-cd-pipeline.yml)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11-blue?logo=python)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GH-200](https://img.shields.io/badge/Course-GH--200-blue?logo=github)](https://learn.microsoft.com/en-us/training/courses/gh-200t00)

> **One-day CoHack workshop** for the GH-200: Automate Your Workflow with GitHub Actions course.
> Learn by doing — follow along, then build two real projects!

---

## 📋 Table of Contents

- [🎯 Workshop Overview](#-workshop-overview)
- [⚡ Getting Started](#-getting-started)
- [📁 Repository Structure](#-repository-structure)
- [📚 Topics Covered](#-topics-covered)
- [🏆 CoHack Projects](#-cohack-projects)
- [🔐 Required Secrets](#-required-secrets)
- [🔗 Quick Reference](#-quick-reference)

---

## 🎯 Workshop Overview

This starter repo is your companion for the **GH-200 CoHack** — a hands-on, follow-along workshop
where you and your team automate everything with GitHub Actions. The entire workshop builds **one
evolving workflow file** (`cohack-journey.yml`), adding one enhancement per topic.

| 📅 Duration | 🎓 Level | 🛠️ Format |
|---|---|---|
| 1 Day (8 hours) | Intermediate | CoHack — Follow-Along + Team Projects |

---

## ⚡ Getting Started

### Step 1 — Fork this repository
Click **Fork** at the top right → select your account → click **Create Fork**.

### Step 2 — Clone your fork
```bash
git clone https://github.com/<YOUR-USERNAME>/gh200-cohack.git
cd gh200-cohack
```

### Step 3 — Set up Python environment (local testing)
```bash
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt
pytest src/ -v
```

### Step 4 — Configure Repository Secrets
Go to **Settings → Secrets and Variables → Actions → New repository secret:**

| Secret Name | Description | Required |
|---|---|---|
| `MY_API_KEY` | Demo API key for secrets topic | ✅ |
| `STAGING_TOKEN` | Token for staging deploys | Optional |
| `PROD_TOKEN` | Token for production deploys | Optional |

### Step 5 — Enable GitHub Actions
Go to **Actions tab → Enable workflows** (if prompted).

### Step 6 — Make your first commit
```bash
echo "# My CoHack Journey" >> NOTES.md
git add NOTES.md
git commit -m "feat: start my GH-200 CoHack journey 🚀"
git push
```

---

## 📁 Repository Structure

```
gh200-cohack/
├── .github/
│   ├── workflows/
│   │   ├── cohack-journey.yml          # 🚀 Main evolving workflow (all 26 topics)
│   │   ├── reusable-notify.yml         # 🔔 Reusable notification workflow
│   │   ├── update-profile-readme.yml   # 🌟 Project 1: Profile README updater
│   │   └── ci-cd-pipeline.yml          # 🔄 Project 2: CI/CD with governance
│   └── actions/
│       └── ascii-banner/
│           └── action.yml              # 🎨 Custom composite action
├── scripts/
│   ├── greet.sh                        # 👋 Workshop greeting script
│   └── update-readme.sh               # 📝 README section updater
├── src/
│   ├── app.py                         # 🐍 Sample Python application
│   └── test_app.py                    # 🧪 Pytest test suite
├── docs/
│   └── workflow-evolution.md          # 📖 Learning journal (13 enhancements)
├── COHACK-GUIDE.md                    # 📋 Full CoHack guide & scoring
├── README.md                          # 📄 This file (auto-updated!)
├── requirements.txt                   # 📦 Python dependencies
└── .gitignore                         # 🙈 Standard ignores
```

---

## 📚 Topics Covered

| # | Topic | Enhancement | Workflow Location |
|---|-------|-------------|-------------------|
| 1 | Create and Run Workflow | 1 | `cohack-journey.yml` |
| 2 | What are Actions | 1 | `cohack-journey.yml` |
| 3 | GitHub Action Core Components | 2 | `cohack-journey.yml` |
| 4 | Configure Checkout Action | 2 | `cohack-journey.yml` |
| 5 | Multi-Line Commands | 3 | `cohack-journey.yml` |
| 6 | Third-Party Libraries + ASCII Art | 3 | `cohack-journey.yml` |
| 7 | Executing Shell Scripts | 4 | `cohack-journey.yml` |
| 8 | Workflow with Multiple Jobs | 5 | `cohack-journey.yml` |
| 9 | Sequential Jobs with `needs` | 5 | `cohack-journey.yml` |
| 10 | Storing Artifacts | 6 | `cohack-journey.yml` |
| 11 | Variables at Different Levels | 7 | `cohack-journey.yml` |
| 12 | Repository Level Secrets | 7 | `cohack-journey.yml` |
| 13 | Triggering a Workflow | 8 | `cohack-journey.yml` |
| 14 | Using Job Concurrency | 9 | `cohack-journey.yml` |
| 15 | Timeout for Jobs and Steps | 9 | `cohack-journey.yml` |
| 16 | Matrix Strategy | 10 | `cohack-journey.yml` |
| 17 | Additional Matrix Configuration | 10 | `cohack-journey.yml` |
| 18 | Access Workflow Context | 11 | `cohack-journey.yml` |
| 19 | Using `if` expressions in Jobs | 11 | `cohack-journey.yml` |
| 20 | Workflow Event Filters & Activity Types | 12 | `cohack-journey.yml` |
| 21 | Cancelling and Skipping Workflows | 12 | `cohack-journey.yml` |
| 22 | Enable Step Debug Logging | 13 | `cohack-journey.yml` |
| 23 | Access Workflow Logs via REST API | 13 | `cohack-journey.yml` |
| 24 | `workflow_dispatch` Input Options | 8 | All workflows |
| 25 | Webhook Events Configuration | 8 | `ci-cd-pipeline.yml` |
| 26 | Reusable Workflows | All | `reusable-notify.yml` |
| 27 | Creating Custom GitHub Actions | All | `ascii-banner/action.yml` |

---

## 🏆 CoHack Projects

### Project 1 — Dynamic GitHub Profile README
**Workflow:** `update-profile-readme.yml`
Auto-updates your GitHub profile README with live stats daily via scheduled workflow.

### Project 2 — CI/CD Pipeline with Multi-Environment Deployment
**Workflow:** `ci-cd-pipeline.yml`
A production-style pipeline: lint → test (matrix) → build → deploy (staging & production).

See **[COHACK-GUIDE.md](COHACK-GUIDE.md)** for full instructions, scoring, and tips!

---

## 🔗 Quick Reference

| Resource | Link |
|---|---|
| 📘 GH-200 Course | https://aka.ms/CourseGH-200 |
| 📖 GitHub Actions Docs | https://docs.github.com/actions |
| 🎓 GH-200 Study Guide | https://learn.microsoft.com/credentials/certifications/resources/study-guides/gh-200 |
| 🎬 YouTube Playlist | https://www.youtube.com/playlist?list=PLahhVEj9XNTd5N_seZDoRXVIn6N1qAp-_ |
| 🛠️ GH-200 Demos Org | https://github.com/GH-200-Demos |
| 🏪 Actions Marketplace | https://github.com/marketplace?type=actions |

---

<!-- ╔══════════════════════════════════════════════════════╗ -->
<!-- ║  AUTO-UPDATED SECTION END                           ║ -->
<!-- ╚══════════════════════════════════════════════════════╝ -->

*Happy automating! 🤖 — Trainer: **Himanshu Kumar** | GH-200 CoHack*
