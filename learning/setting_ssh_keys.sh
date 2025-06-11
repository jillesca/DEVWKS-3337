#!/bin/bash
set -e

# handy script to setup ssh keys for the sandbox VM for workshop
# set environment variables
# SSH_KEY_PATH=
# SANDBOX_USER=
# SANDBOX_IP=

echo "=== Setting up SSH key for the sandbox VM ==="
echo "Using SSH key path: $SSH_KEY_PATH"
if [ ! -f "$SSH_KEY_PATH" ]; then
    echo "Creating new SSH key..."
    # Ensure directory exists
    mkdir -p "$(dirname "$SSH_KEY_PATH")"
    yes y | ssh-keygen -t rsa -b 4096 -C "sandbox@built.com" -f "$SSH_KEY_PATH" -N ""
    ssh-copy-id -f -i "$SSH_KEY_PATH.pub" "$SANDBOX_USER@$SANDBOX_IP"
else
    echo "SSH key already exists. Using existing key."
fi

echo -e "\033[32m=== SSH setup completed successfully! ===\033[0m" 