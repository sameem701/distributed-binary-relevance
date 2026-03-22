# GitHub Setup & Submission Guide

## Steps to Set Up Your GitHub Repository

### 1. Create New GitHub Repository

Visit [github.com/new](https://github.com/new) and:
- **Repository name**: `distributed-binary-relevance`
- **Description**: Binary Relevance Multi-Label Classification with Parallel Computing
- **Visibility**: Public (for sharing) or Private
- **Initialize with**: Skip (we'll push existing files)

### 2. Initialize Git Repository Locally

Navigate to your project directory:
```bash
cd "c:\Users\786 Computers\Desktop\distributed-binary-relevance"
```

Initialize git (if not already done):
```bash
git init
```

### 3. Add All Files to Git

```bash
# Stage all files
git add .

# View staged files
git status
```

**Expected output**:
```
On branch master

No commits yet

Changes to be committed:
  new file:   .gitignore
  new file:   README.md
  new file:   REPORT.md
  new file:   requirements.txt
  new file:   milestone1.py
  new file:   milestone1_optimized.py
  new file:   eurlex.csv
  new file:   eurlex_test.csv
  new file:   test_predictions.npy
```

### 4. Create Initial Commit

```bash
git commit -m "Initial commit: Binary Relevance implementation with parallel training - Milestone 1"
```

### 5. Set Remote Repository

Replace `YOUR_USERNAME` and `REPO_URL` with yours:

```bash
git remote add origin https://github.com/YOUR_USERNAME/distributed-binary-relevance.git

# Verify remote
git remote -v
```

### 6. Rename Branch (Optional)

To use 'main' instead of 'master':
```bash
git branch -M main
```

### 7. Push to GitHub

```bash
git push -u origin main
```

Or if using 'master':
```bash
git push -u origin master
```

---

## Alternative: Command-Line Quick Setup

```bash
cd "c:\Users\786 Computers\Desktop\distributed-binary-relevance"
git init
git add .
git commit -m "Initial commit: Binary Relevance implementation - Milestone 1"
git remote add origin https://github.com/YOUR_USERNAME/distributed-binary-relevance.git
git branch -M main
git push -u origin main
```

---

## File Organization for GitHub

Your repository will contain:

```
distributed-binary-relevance/
├── README.md                  ← START HERE (setup instructions)
├── REPORT.md                  ← Project documentation
├── requirements.txt           ← Dependencies
├── GitHub_Setup_Guide.md      ← This file
├── milestone1.py              ← Full implementation
├── milestone1_optimized.py    ← Quick start (recommended)
├── eurlex.csv                 ← Training data (~323 MB)
├── eurlex_test.csv           ← Test data (~83 MB)
├── test_predictions.npy      ← Model predictions output
└── .gitignore                ← Git exclusions
```

---

## Important Notes for GitHub

### Large Files
- `eurlex.csv` (323 MB) and `eurlex_test.csv` (83 MB) are large
- GitHub recommends files < 100 MB
- **Options**:
  1. Use [Git LFS](https://git-lfs.com/) for large files
  2. Upload data separately (provide download link in README)
  3. Keep only optimized version, provide original separately

### If Using Git LFS
```bash
# Install Git LFS if needed
git lfs install

# Track large files
git lfs track "*.csv"
git add .gitattributes
git add eurlex*.csv

git commit -m "Add large data files with Git LFS"
git push
```

### README in Repository
Your README.md will be displayed on GitHub homepage. Key sections:
- ✅ Project description
- ✅ Installation instructions
- ✅ How to run code
- ✅ Performance metrics
- ✅ Project structure
- ✅ Next steps and milestones

### Badges (Optional Enhancement)
Add to README.md:
```markdown
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)
```

---

## Verifying Your GitHub Repository

Once pushed, verify:
1. Visit your repository: `https://github.com/YOUR_USERNAME/distributed-binary-relevance`
2. Check file count and sizes
3. Verify README displays correctly
4. Click on files to view source code
5. Test download of requirements.txt and README.md

---

## Making Further Updates

### Add New Files
```bash
git add new_file.py
git commit -m "Add: description of changes"
git push
```

### Update Existing Files
```bash
git add modified_file.py
git commit -m "Update: description of changes"
git push
```

### Create Branches for New Features
```bash
git checkout -b feature/milestone-2
# Make changes
git add .
git commit -m "WIP: Implement Milestone 2 - Distributed Computing"
git push -u origin feature/milestone-2

# Then create Pull Request on GitHub
```

---

## GitHub Best Practices

### Commit Messages
✅ Good:
- "Add binary relevance implementation"
- "Fix: Handle imbalanced labels in training"
- "Optimize: Parallel training performance"

❌ Bad:
- "Update"
- "Fix bug"
- "asdfgh"

### Branch Strategy
```
main (stable)
├── feature/milestone-2
├── feature/gpu-optimization
└── bugfix/memory-leak
```

### Pull Request Template (Optional)
Create `.github/pull_request_template.md`:
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] New feature
- [ ] Bug fix
- [ ] Performance improvement

## Testing
Describe testing performed
```

---

## Sharing Your Repository

### For Collaboration
```
Share link: https://github.com/YOUR_USERNAME/distributed-binary-relevance
Clone command: git clone https://github.com/YOUR_USERNAME/distributed-binary-relevance.git
```

### For Assignment Submission
Include in submission:
1. Repository URL
2. Link to specific commit (if needed)
3. Link to README.md
4. Link to REPORT.md for detailed documentation

Example:
```
GitHub Repository: https://github.com/YOUR_USERNAME/distributed-binary-relevance

Key Files:
- Implementation: milestone1.py (full), milestone1_optimized.py (quick)
- Documentation: README.md (setup), REPORT.md (detailed report)
- Data: eurlex.csv, eurlex_test.csv
- Results: test_predictions.npy

To run:
1. pip install -r requirements.txt
2. python milestone1_optimized.py
```

---

## Troubleshooting

### Issue: "fatal: not a git repository"
**Solution**: Run `git init` first

### Issue: "fatal: 'origin' does not appear to be a 'git' repository"
**Solution**: Run `git remote add origin <URL>`

### Issue: "Everything up-to-date" but files not showing on GitHub
**Solution**: 
```bash
git log  # Verify commits exist
git branch -v  # Check branch is correct
git push -u origin main --force  # Force push if needed
```

### Issue: File too large (>100 MB)
**Solution**: Use Git LFS or split data files

### Issue: Forgot to add file before commit
**Solution**:
```bash
git add forgotten_file.py
git commit --amend -m "Add all files"
git push --force-with-lease
```

---

## What GitHub Shows Visitors

1. **README.md** - Auto-displayed at repository root
2. **File browser** - Click to view code
3. **Releases** - If you create tagged releases
4. **Issues** - Track bugs/features
5. **Pull Requests** - Collaboration history
6. **Insights** - Statistics and graphs

---

## Final Checklist

- [ ] Created GitHub repository
- [ ] Initialized local git: `git init`
- [ ] Added all files: `git add .`
- [ ] Created commit: `git commit -m "..."`
- [ ] Set remote: `git remote add origin ...`
- [ ] Verified remote: `git remote -v`
- [ ] Pushed to GitHub: `git push -u origin main`
- [ ] Verified files on GitHub website
- [ ] README.md displays correctly
- [ ] REPORT.md is readable
- [ ] Generated link to share

---

## Need Help?

- GitHub Documentation: https://docs.github.com
- Git Cheat Sheet: https://git-scm.com/docs
- Git LFS: https://git-lfs.com

---

**Last Updated**: March 22, 2026
