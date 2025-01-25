# Screenshot Assistant

A Wayland screenshot assistant with LLM integration. Capture screenshots and analyze them using Ollama's LLaVA model.

## Installation

```bash
pip install screenshot-assistant
```

## Requirements

- Wayland compositor (Sway, Hyprland, or other wlroots-based)
- grim (screenshot utility)
- slurp (area selection)
- imv (image viewer)
- Ollama with LLaVA model installed

## Usage

You can run the assistant in two ways:

1. As a command:

```bash
screenshot-assistant
```

2. Using the provided run script:

```bash
./run
```

## Configuration

Create a `.env` file with the following options:

```env
OLLAMA_URL=http://localhost:11434/api/generate
OLLAMA_MODEL=llava
WINDOW_TITLE=Screenshot Assistant
SCREENSHOT_MODE=active  # Options: all, active, select
```

## Development

To set up for development:

```bash
git clone https://github.com/tcsenpai/screenshot-assistant.git
cd screenshot-assistant
uv venv .venv
uv pip install -e .
```
