# AI Browser Operator

A Python PoC using [Browser Use](https://docs.browser-use.com/) to create browser automation agents with LLMs.

## Setup

1. Create a virtual environment:
```bash
uv venv --python 3.11
```

2. Activate the environment:
```bash
# For zsh/bash:
source .venv/bin/activate

# For fish shell:
source .venv/bin/activate.fish
```

3. Install dependencies:
```bash
uv pip install browser-use
```

4. Install playwright:
```bash
uv run playwright install
```

5. Set up your API keys in a `.env` file:
```
OPENAI_API_KEY=your_openai_api_key
```

## Usage

Run the agent:
```bash
python agent.py
```

## Documentation

For customization options, including:
- Supported models
- Agent settings
- Browser settings
- Output formats
- System prompts

Go to [Browser Use documentation](https://docs.browser-use.com/).
