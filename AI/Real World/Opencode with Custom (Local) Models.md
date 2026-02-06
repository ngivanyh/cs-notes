**docs: https://opencode.ai/docs/**

Everything starts from the `opencode.jsonc`, stored in `~/.config/opencode/opencode.json`. Coding also takes up a lot of tokens, it's nice if you can get at least 60K context length.
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

> Note that a standard installation (`curl -fsSL https://ollama.com/install.sh | sh`) of `ollama` would have the `OLLAMA_CONTEXT_LENGTH` set to 4096 (tokens), since that installation automatically puts `ollama` as a `systemd` service, go to `/etc/system/systemd/ollama.service`, and do the following:

```
[Unit]
...
(Leave as is)

[Service]
Environment=OLLAMA_CONTEXT_LENGTH=XXXXX # Change "XXXXX" to something longer
ExecStart=/usr/local/bin ollama serve
...
(Leave as is)


[Install]
...
(Leave as is)
```

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