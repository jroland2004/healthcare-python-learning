# How to Continue Learning Across Chat Sessions

This guide ensures you can seamlessly continue your Python curriculum even if you need to start a new chat with Claude.

---

## Files to Keep in Your Repository

### 1. Curriculum Document
The complete `python-healthcare-backend-curriculum.md` contains your full 32-week roadmap. Keep this in your repository root.

### 2. Progress Tracker
Update `PROGRESS.md` after each learning session to track:
- Which exercise you're currently on
- What you've completed
- Skills you've learned
- Any notes or areas needing practice

---

## After Each Learning Session

Run these commands to save your progress:

```bash
cd ~/projects/healthcare-python
git add .
git commit -m "Complete [exercise name]"
git push
```

Update your `PROGRESS.md` file before committing:
- Check off completed exercises
- Update "Current Position"
- Add any notes about concepts learned

---

## Starting a New Chat

When you begin a new conversation with Claude, provide context like this:

> "I'm working through a Python backend developer curriculum focused on healthcare data. Here's my current status:
> 
> **Current position**: Week 2, Exercise 5 - Multi-patient vital signs tracker
> 
> **What I'm building**: A program that stores multiple patients in a list of dictionaries and flags abnormal vitals.
> 
> **Where I'm stuck** (if applicable): [describe the issue]
> 
> **My current code**:
> ```python
> [paste your code here]
> ```"

The more specific you are, the faster we can continue productively.

---

## What Claude Remembers

Claude's memory system retains key information about you across conversations:
- Your background (RN with IT leadership experience)
- Your development environment (Mac, VS Code, Python 3.12)
- Your learning goals (healthcare technology, backend development)
- Your GitHub repository name

You don't need to re-explain these basics in each new chat.

---

## Quick Reference: Your Setup

| Item | Value |
|------|-------|
| OS | macOS |
| IDE | VS Code |
| Python | 3.12.12 (via Homebrew) |
| Repository | healthcare-python-learning |
| Project folder | ~/projects/healthcare-python |

---

## If You Get Stuck Between Sessions

1. Check the curriculum document for guidance on your current topic
2. Review your completed code files for patterns you've already learned
3. Google the specific error message if you encounter one
4. Start a new chat with Claude and provide context as described above

---

## Recommended Session Workflow

1. **Start**: Review `PROGRESS.md` to remember where you left off
2. **Code**: Work through exercises, committing after each one
3. **End**: Update `PROGRESS.md`, commit, and push to GitHub

This keeps your work safe and makes resuming easy.
