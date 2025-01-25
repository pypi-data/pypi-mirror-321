FROM mcr.microsoft.com/devcontainers/base:debian-12

ENV DEBIAN_FRONTEND=noninteractive

SHELL ["/bin/bash", "-c"]

RUN apt update && \
    apt install -y \
    curl \
    git \
    # To open in a browser on the host
    xdg-utils \
    # LLDB
    lldb-19 && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

USER vscode
ENV HOME="/home/vscode"
RUN echo '' >> ~/.bashrc && \
    echo '################################################################################' >> ~/.bashrc && \
    echo '# Environment variables' >> ~/.bashrc && \
    echo '################################################################################' >> ~/.bashrc && \
    echo '' >> ~/.bashrc && \
    echo '# LLDB' >> ~/.bashrc && \
    echo 'export PATH="/usr/lib/llvm-19/bin:$PATH"' >> ~/.bashrc && \
    echo '' >> ~/.bashrc

ENV RUST_VERSION="1.84.0"
ENV PATH="$HOME/.cargo/bin:$PATH"
RUN echo '# Rust' >> ~/.bashrc && \
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && \
    rustup install "$RUST_VERSION" && \
    rustup default "$RUST_VERSION" && \
    echo '' >> ~/.bashrc

ENV PATH="$HOME/.local/bin:$PATH"
RUN echo '# Python' >> ~/.bashrc && \
    curl -LsSf "https://astral.sh/uv/0.5.21/install.sh" | sh && \
    uv python install 3.9.21 && \
    echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc && \
    echo 'eval "$(uvx --generate-shell-completion bash)"' >> ~/.bashrc && \
    echo '' >> ~/.bashrc

ENV PATH="$HOME/.volta/bin:$PATH"
RUN echo '# Node.js' >> ~/.bashrc && \
    curl https://get.volta.sh | bash && \
    volta install \
    node@22.13.0 \
    npm@11.0.0 \
    gitmoji-cli@5.3.0 && \
    echo '' >> ~/.bashrc

RUN echo '# Aliases' >> ~/.bashrc && \
    echo 'alias ll="ls -a -p -lh"' >> ~/.bashrc && \
    echo '' >> ~/.bashrc

WORKDIR /work
