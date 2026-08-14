# Git Interview Questions

Version control interview questions and answers.

---

## 📝 Git Basics

### Q1: How do you initialize a Git repo?
```bash
git init
```
Creates a new `.git` directory in the current folder. Start tracking an existing project.

### Q2: How do you stage and commit changes?
```bash
git add <file>          # Stage a specific file
git add .               # Stage all changes in current directory
git commit -m "message" # Commit staged changes
```

### Q3: What does `git status` show?
```bash
git status
```
Shows which files are modified, staged, or untracked. Essential for checking before commit.

### Q4: How do you view commit history?
```bash
git log                 # Show all commits
git log --oneline       # Compact one-line format
git log --graph         # ASCII graph of branches
git log -n 5            # Show last 5 commits
git log --all --oneline --graph --decorate  # Full history
```

### Q5: How do you configure Git?
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global core.editor "code --wait"
```

---

## 📝 Branching & Merging

### Q1: How do you create and switch to a new branch?
```bash
git branch <branch-name>    # Create new branch
git checkout <branch-name>  # Switch to branch
git checkout -b <branch-name>  # Create and switch in one command
git switch <branch-name>    # Modern alternative (Git 2.23+)
git switch -c <branch-name> # Create and switch
```

### Q2: How do you merge one branch into another?
```bash
git checkout main          # Switch to target branch
git merge feature-branch   # Merge feature into main
```
- **Fast-forward merge:** If main hasn't diverged, just moves the pointer forward.
- **Three-way merge:** If both branches have new commits, creates a merge commit.

### Q3: What is `git rebase` and how is it different from `merge`?
```bash
git rebase main          # Reapply current branch commits on top of main
```
- **Merge:** Preserves history, creates a merge commit. Non-destructive.
- **Rebase:** Rewrites history, linearizes commits. Can be destructive (rewrites SHA).

**Interview tip:** "I use merge for shared branches (safety) and rebase for local feature branches (clean history). Never rebase public/shared branches."

### Q4: How do you resolve merge conflicts?
```bash
# 1. Git marks conflicted files with <<<<<<<, =======, >>>>>>> markers
# 2. Edit the file to keep the desired changes
# 3. git add <resolved-file>  # Mark as resolved
# 4. git commit               # Complete the merge
```

---

## 📝 Remote & GitHub

### Q1: How do you push to a remote repo?
```bash
git remote add origin <url>    # Add remote (first time)
git push -u origin main        # Push and set upstream
git push                      # Push committed changes
git push --force              # Force push (dangerous on shared branches)
```

### Q2: How do you pull from remote?
```bash
git pull origin main          # Fetch + merge remote changes
git pull --rebase origin main # Fetch + rebase (cleaner history)
```

### Q3: How do you fetch without merging?
```bash
git fetch origin              # Downloads objects + refs from remote
```
- `git fetch` gets data but doesn't change working files
- `git pull` = `git fetch` + `git merge`

### Q4: How do you rename a branch locally and remotely?
```bash
git branch -m old-name new-name     # Rename locally
git push origin :old-name new-name  # Delete old + push new remotely
# Or: git push origin old-name:new-name
```

---

## 📝 Advanced Git

### Q1: How do you undo changes?

| Command | Effect |
|---|---|
| `git restore <file>` | Restores working file from last commit (discards unstaged changes) |
| `git restore --staged <file>` | Unstages file (keeps content in index) |
| `git revert <commit>` | Creates a new commit that undoes the changes of the specified commit (safe for shared history) |
| `git reset --soft <commit>` | Moves HEAD, keeps staged changes |
| `git reset --mixed <commit>` (default) | Moves HEAD, unstages changes |
| `git reset --hard <commit>` | Moves HEAD, discards ALL changes (local only) |
| `git reflog` | Shows history of HEAD moves — recover from bad resets |

### Q2: How do you cherry-pick a commit?
```bash
git cherry-pick <commit-hash>
```
Applies a specific commit from one branch to current branch. Useful for hotfixes.

### Q3: What is `git reflog` and when do you use it?
```bash
git reflog
```
Shows all references' move history. Useful for recovering after `git reset --hard` or lost commits.

### Q3: How do you stash changes?
```bash
git stash           # Temporarily save uncommitted changes
git stash pop       # Apply stashed changes back
git stash list      # List all stashes
git stash drop      # Delete a stash
```
Useful when switching branches but not ready to commit.

---

## 📝 Git Workflows

### Q1: What is Gitflow?
```
Feature branches → Develop → Release → Hotfix → Master
```
- **Branches:** `main` (production), `develop` (integration), `feature/*`, `release/*`, `hotfix/*`
- **When to use:** Traditional release cycles, scheduled releases

### Q2: What is feature branch workflow?
```
main (stable) → feature/* → pull request/merge → main
```
- **When to use:** Simpler projects, continuous deployment, trunk-based development

### Q3: What is trunk-based development?
- Short-lived feature branches (hours, not days)
- All changes go through `main` via pull requests
- Feature flags for incomplete work
- **When to use:** CI/CD, high-performing teams, daily deployments

---

## Related

- [Java Developer Index](../00%20-%20Index.md)
- [Git Commands Cheat Sheet](Git-Commands-Cheat-Sheet.md)