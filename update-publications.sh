#!/bin/bash

set -e

echo "Ensuring submodules are initialized and updated..."
git submodule update --init
git submodule update --remote

python3 update-publications.py
