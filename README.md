# langchain-experiment

A [Langchain](https://python.langchain.com/en/latest/getting_started/getting_started.html) experiment.

Translates a prompt in Indonesian with [bloomz](https://huggingface.co/bigscience/bloomz), and queries a SQLite DB with output from [GPT-3.5](https://platform.openai.com/docs/models/gpt-3-5). The starting prompt is translated from an example on [langchain's documentation](https://python.langchain.com/en/latest/modules/chains/examples/sqlite.html).

## Installation

On a Python virtual environment, run

```bash
pip install -r requirements.txt
```

## Running it

1. Create a `.env` file based on the `example.env` file, filling it with your HuggingFace and OpenAI API keys
1. Run it with `python3 main.py`
