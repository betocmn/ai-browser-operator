# AI Browser Operator

A Python PoC using [Browser Use](https://docs.browser-use.com/) to create browser automation agents with LLMs.

## Setup

0. Install uv (required for dependency management):
See the [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/).

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

5. Set up your API keys and credentials in a `.env` file:
```
# Copy from example file
cp .env.example .env
# Then edit .env with your credentials
```

## Usage

### LLM Pricing Comparison Agent
Run the agent to compare LLM pricing:
```bash
python src/pricing_comparison_agent.py
```

### Hacker News Karma Checker
Run the agent to log in to Hacker News and check your karma:
```bash
python src/log_in_to_hacker_news_and_get_my_karma.py
```

For the Hacker News karma checker to work:
- Ensure your HN_USERNAME and HN_PASSWORD are set in the .env file
- The script will automatically close any running Chrome instances
- A new Chrome instance will be launched with a separate profile

## Documentation

For customization options, including:
- Supported models
- Agent settings
- Browser settings
- Output formats
- System prompts

Go to [Browser Use documentation](https://docs.browser-use.com/).
