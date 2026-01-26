# Python Development Environment Setup Guide

## Prerequisites
- Python 3.8+ installed on your system
- Git installed
- GitHub account
- VS Code installed

---

## Step 1: Clone the Repository

```powershell
git clone https://github.com/YOUR-USERNAME/Hackerrank.git
cd Hackerrank
```

---

## Step 2: Create a Python Virtual Environment

### Option A: Using `venv` (Recommended)

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# If you get execution policy error:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Option B: Using `conda`

```powershell
conda create -n hackerrank python=3.11
conda activate hackerrank
```

---

## Step 3: Install Dependencies

```powershell
pip install -r requirements.txt
```

---

## Step 4: Configure VS Code

### 4.1 Open Project in VS Code

```powershell
code .
```

### 4.2 Install Recommended VS Code Extensions

Install the following extensions from the VS Code Marketplace:

1. **Python** (Microsoft)
   - ID: `ms-python.python`
   - Provides IntelliSense, debugging, and testing support

2. **Pylance** (Microsoft)
   - ID: `ms-python.vscode-pylance`
   - Advanced Python language support

3. **Black Formatter** (Microsoft)
   - ID: `ms-python.black-formatter`
   - Auto-format code to PEP 8 standards

4. **Flake8** (Microsoft)
   - ID: `ms-python.flake8`
   - Linting and style checking

5. **Pytest** (LittleFox Team)
   - ID: `littlefoxteam.vscode-python-test-adapter`
   - Test discovery and execution

6. **Git Graph** (mhutchie)
   - ID: `mhutchie.git-graph`
   - Visualize git history

7. **GitHub Copilot** (GitHub)
   - ID: `GitHub.copilot`
   - AI-assisted code completion

8. **Thunder Client** (Thunder Client)
   - ID: `rangav.vscode-thunder-client`
   - API testing (optional)

### 4.3 Select Python Interpreter

1. Press `Ctrl + Shift + P`
2. Type "Python: Select Interpreter"
3. Choose the interpreter from your `venv` folder

### 4.4 Configure VS Code Settings

Create or update `.vscode/settings.json`:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.formatting.provider": "black",
  "python.formatting.blackArgs": ["--line-length=88"],
  "python.linting.flake8Args": [
    "--max-line-length=88",
    "--extend-ignore=E203,W503"
  ],
  "[python]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.codeActionsOnSave": {
      "source.organizeImports": "explicit"
    }
  },
  "isort.args": ["--profile", "black"]
}
```

---

## Step 5: Configure Git and GitHub

### 5.1 Configure Git (if not already done)

```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 5.2 Create SSH Key (Recommended for Authentication)

```powershell
ssh-keygen -t ed25519 -C "your.email@example.com"
```

Add the public key to your GitHub account:
1. Go to GitHub Settings → SSH and GPG keys
2. Click "New SSH key"
3. Paste your public key content (from `~/.ssh/id_ed25519.pub`)

### 5.3 Test GitHub Connection

```powershell
ssh -T git@github.com
```

---

## Step 6: Common Workflow Commands

### Run Tests
```powershell
pytest
pytest --cov  # With coverage report
```

### Format Code
```powershell
black .
isort .
```

### Lint Code
```powershell
flake8 .
mypy .
```

### Commit Changes
```powershell
git add .
git commit -m "Your commit message"
git push origin main
```

### Pull Changes
```powershell
git pull origin main
```

---

## Step 7: Useful VS Code Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl + Shift + P` | Command Palette |
| `Ctrl + Backtick` | Toggle Terminal |
| `Ctrl + /` | Toggle Comment |
| `F5` | Start Debugging |
| `Ctrl + Shift + D` | Debug View |
| `Ctrl + Shift + T` | Reopen Closed Tab |
| `Alt + Shift + F` | Format Document |

---

## Troubleshooting

### Issue: Python interpreter not found
**Solution:** Ensure virtual environment is created and activated. Refresh VS Code.

### Issue: Module not found errors
**Solution:** Verify the virtual environment is activated and dependencies are installed:
```powershell
pip list
```

### Issue: Git command not recognized
**Solution:** Ensure Git is installed and added to system PATH. Restart terminal.

### Issue: Permission denied on PowerShell script
**Solution:** 
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## Next Steps

1. Create feature branches for each feature:
   ```powershell
   git checkout -b feature/your-feature-name
   ```

2. Write tests for your code
3. Use Black and Flake8 to maintain code quality
4. Create pull requests and request reviews
5. Merge to main after approval

---

## Resources

- [Python Docs](https://docs.python.org/)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [VS Code Python Guide](https://code.visualstudio.com/docs/languages/python)
- [Black Code Formatter](https://github.com/psf/black)
