#!/bin/bash

echo "Setting up AI Film Studio development environment..."

# Configure git to use GitHub CLI for authentication in Codespaces
if [ -n "$CODESPACE_NAME" ]; then
    echo "Detected GitHub Codespace environment"
    
    # Remove any existing credential helpers (both local and global)
    git config --global --unset-all credential.helper 2>/dev/null || true
    git config --local --unset-all credential.helper 2>/dev/null || true
    git config --local --unset credential.username 2>/dev/null || true
    
    # Configure git to use GitHub CLI credential helper globally
    git config --global credential.helper "!/usr/bin/gh auth git-credential"
    
    echo "Git authentication configured to use GitHub CLI"
fi

# Install Python dependencies if backend exists
if [ -d "backend" ]; then
    echo "Installing Python dependencies..."
    cd backend
    if [ -f "requirements.txt" ]; then
        pip install --user -r requirements.txt || echo "Failed to install some Python dependencies"
    fi
    cd ..
fi

# Install Node dependencies if frontend exists
if [ -d "frontend" ]; then
    echo "Installing Node.js dependencies..."
    cd frontend
    if [ -f "package.json" ]; then
        npm install || echo "Failed to install some Node.js dependencies"
    fi
    cd ..
fi

echo "Setup complete!"
