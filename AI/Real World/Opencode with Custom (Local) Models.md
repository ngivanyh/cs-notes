**docs: https://opencode.ai/docs/**

Everything starts from the `opencode.jsonc`, stored in `~/.config/opencode/opencode.json`.
## Using Local/Custom Models
### Ollama

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": {
        "baseURL": "http://localhost:11434/v1"
      },
      "models": {
        "llama2": {
          "name": "Llama 2"
        }
      }
    }
  }
}
```

The `name` of the model can be custom, but the model name as the key in the `models` dictionary must be the correct name specified in `ollama`.

### LMStudio

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "lmstudio": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "LM Studio (local)",
      "options": {
        "baseURL": "http://127.0.0.1:1234/v1"
      },
      "models": {
        "google/gemma-3n-e4b": {
          "name": "Gemma 3n-e4b (local)"
        }
      }
    }
  }
}
```

Similar to `ollama`, just some value changes. (like in `models`, `name`, `baseURL`)

### `llama.cpp` (& other custom providers)



## Serving to other clients
### Server

### Client

#ai #ai/realworld 