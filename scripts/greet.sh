#!/bin/bash
# ══════════════════════════════════════════════════════════════
# greet.sh — GH-200 CoHack Workshop Greeting Script
# Topic 7: Executing Shell Scripts in Workflow
# ══════════════════════════════════════════════════════════════

echo "╔═══════════════════════════════════════════════════╗"
echo "║   🎉 Welcome to the GH-200 CoHack Workshop!      ║"
echo "╚═══════════════════════════════════════════════════╝"
echo ""
echo "📅 Date & Time   : $(date)"
echo "🖥️  Runner OS     : $RUNNER_OS"
echo "🏃 GitHub Actor  : $GITHUB_ACTOR"
echo "📦 Repository    : $GITHUB_REPOSITORY"
echo "🔑 Commit SHA    : $GITHUB_SHA"
echo "🌿 Branch / Ref  : $GITHUB_REF_NAME"
echo "🔢 Run Number    : $GITHUB_RUN_NUMBER"
echo ""
echo "✅ Shell script executed successfully via GitHub Actions!"
