---
tags: [ai, ai/realworld]
title: Opencode with Custom (Local) Models
date created: Tuesday, January 27th 2026, 10:46:18 pm
date modified: Sunday, March 1st 2026, 6:23:33 pm
parent: Real World
grand_parent: AI
---
# Opencode with Custom (Local) Models
[**Docs**](https://opencode.ai/docs/)

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

> [!NOTE] 
> A standard installation (`curl -fsSL https://ollama.com/install.sh | sh`) of `ollama` would have the `OLLAMA_CONTEXT_LENGTH` set to 4096 (tokens), since that installation automatically puts `ollama` as a `systemd` service, go to `/etc/system/systemd/ollama.service`, and do the following:
> ```
>[Unit]
> ...
(Leave as is)
>
>[Service]
Environment=OLLAMA_CONTEXT_LENGTH=XXXXX # Change "XXXXX" to something longer
ExecStart=/usr/local/bin ollama serve
...
(Leave as is)
> 
> [Install]
...
(Leave as is)

> [!NOTE]
> To immediately see the the new context length in effect, run the command `sudo systemctl daemon-reload`

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

### `llama.cpp` (& other custom providers, like `vllm`)

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "PROVIDER NAME": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "DISPLAYED PROVIDER NAME",
      "options": {
        "baseURL": "http://127.0.0.1:PORT/v1"
      },
      "models": {
        "ACTUAL MODEL NAME (e.g. google/gemma-3n-e4b)": {
          "name": "DISPLAYED MODEL NAME (e.g. Gemma 3n e4b)"
        }
      }
    }
  }
}
```

It's really easy if you have an OpenAI API compatible server.

## Serving to other clients
### Server

```
$ opencode web --port PORT --hostname 0.0.0.0
```

There is an optional `--mdns` option, which gives it a domain name by default `opencode.local`; change that value via `--mdns-hostname`.

### Client
- **TUI**: `opencode attach HOSTNAME`
- **Web**: Visiting that URL

#ai #ai/realworld 