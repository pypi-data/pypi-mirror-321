#!/usr/bin/env bash

set -ex

# Check LLDB
lldb --version

# Check Rust
rustc --version
cargo --version
rust-lldb --version

# Check Python
uv --version
uvx --version
uv run python --version

# Check Node.js
volta --version
node --version
npm --version
gitmoji --version
