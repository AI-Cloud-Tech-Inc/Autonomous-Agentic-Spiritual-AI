# GitHub Codespace Setup Guide

## Problem: Unable to Commit and Push from Codespace

If you're experiencing issues with git commit and push operations in GitHub Codespaces, you may see errors like:

```
remote: Invalid username or token. Password authentication is not supported for Git operations.
fatal: Authentication failed for 'https://github.com/...'
```

## Solution

This repository now includes a `.devcontainer` configuration that automatically fixes this issue.

### Automatic Fix (Recommended)

When you create a new Codespace, the setup will automatically:

1. Configure git to use GitHub CLI for authentication
2. Install project dependencies
3. Set up the development environment

**No manual action required!**

### Manual Fix (If Needed)

If you're in an existing Codespace or need to manually configure git authentication:

1. Run the setup script:
   ```bash
   bash .devcontainer/setup.sh
   ```

2. Or manually configure git:
   ```bash
   git config --global credential.helper ""
   git config --global credential.helper "!/usr/bin/gh auth git-credential"
   ```

### Verify the Fix

Test that git operations work:

```bash
# Check git credential configuration
git config --get credential.helper
# Should output: !/usr/bin/gh auth git-credential

# Check GitHub CLI authentication
gh auth status
# Should show you're logged in

# Test with a commit
echo "test" > test.txt
git add test.txt
git commit -m "Test commit"
git push

# Clean up test
git reset HEAD~1
rm test.txt
```

## Why This Works

GitHub Codespaces automatically provides authentication through the GitHub CLI (`gh`). By configuring git to use `gh` as the credential helper, git operations automatically use the Codespace's built-in GitHub token.

The previous configuration tried to use a `GITHUB_TOKEN` environment variable that wasn't available in the Codespace environment.

## Development Workflow

After the fix, you can use git normally:

```bash
# Make changes
git add .
git commit -m "Your commit message"
git push

# Create new branches
git checkout -b feature/new-feature
git push -u origin feature/new-feature

# Pull changes
git pull
```

## Additional Resources

- [GitHub Codespaces Documentation](https://docs.github.com/en/codespaces)
- [GitHub CLI Authentication](https://cli.github.com/manual/gh_auth_login)
- [Dev Container Specification](https://containers.dev/)

## Support

If you continue to experience issues:

1. Check `.devcontainer/README.md` for troubleshooting steps
2. Open an issue on GitHub
3. Contact support@ai-cloud-tech.com
