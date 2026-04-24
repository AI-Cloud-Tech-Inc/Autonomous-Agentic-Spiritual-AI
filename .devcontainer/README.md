# GitHub Codespaces Configuration

This directory contains the configuration for GitHub Codespaces development environment.

## Files

- **devcontainer.json**: Main configuration file for the dev container
- **setup.sh**: Post-create setup script that runs when the Codespace is created

## Git Authentication Fix

The setup script automatically configures git authentication in GitHub Codespaces using GitHub CLI as the credential helper. This fixes the issue where git push operations would fail with authentication errors.

### What it does:

1. Detects if running in a GitHub Codespace environment
2. Clears any existing git credential helpers
3. Configures git to use GitHub CLI (`gh`) for authentication
4. GitHub CLI automatically uses the Codespace's built-in GitHub token

### Manual Configuration (if needed):

If you need to manually configure git authentication in Codespace, run:

```bash
git config --global credential.helper ""
git config --global credential.helper "!/usr/bin/gh auth git-credential"
```

## Features Included

- Python 3.11
- Node.js 18
- Git
- GitHub CLI (gh)
- VS Code extensions for Python and JavaScript development

## Development Setup

When a Codespace is created, the setup script automatically:

1. Configures git authentication
2. Installs Python dependencies from `backend/requirements.txt` (if exists)
3. Installs Node.js dependencies from `frontend/package.json` (if exists)

## Troubleshooting

### Git push still fails

If git push still fails after the Codespace is created:

1. Check if you're in a Codespace:
   ```bash
   echo $CODESPACE_NAME
   ```

2. Verify git credential helper:
   ```bash
   git config --get credential.helper
   ```
   Should output: `!/usr/bin/gh auth git-credential`

3. Test GitHub CLI authentication:
   ```bash
   gh auth status
   ```

4. Re-run the setup script manually:
   ```bash
   bash .devcontainer/setup.sh
   ```

### Dependencies installation failed

If dependencies fail to install during setup:

- For Python: `cd backend && pip install -r requirements.txt`
- For Node.js: `cd frontend && npm install`
