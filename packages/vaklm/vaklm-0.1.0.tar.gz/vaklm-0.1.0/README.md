# vaklm

Easy interaction with OpenAI-compatible LLM endpoints.

No more `client.chat.completions.create` verbosity!

## Installation

```bash
pip install vaklm
```

## Usage

```python
from vaklm import vaklm

# Non-streaming example
response_data = vaklm(
    endpoint="http://localhost:11434/v1/chat/completions",
    model_name="llama2",
    user_prompt="Write a short story about a cat.",
    system_prompt="You are a creative writer.",
    api_key="YOUR_ACTUAL_API_KEY" # can be any value of local LLM
)
if response_data:
    print("API Response:")
    print(response_data)

# Streaming example
vaklm(
    endpoint="http://localhost:11434/v1/chat/completions",
    model_name="llama2",
    user_prompt="Write a short story about a cat.",
    system_prompt="You are a creative writer.",
    api_key="YOUR_ACTUAL_API_KEY",
    stream=True
)
```
