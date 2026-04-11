---
tags: [python, python/features]
title: Project Management with uv
date created: Saturday, January 31st 2026, 9:31:44 pm
date modified: Saturday, April 11th 2026, 9:53:49 pm
parent: Python
nav_order: 7
---
# Project Management with uv
### Create a New Project

```
uv init
```

> [!NOTE]
> You don't have to initialize the `.venv` `uv` creates for you.

### Install/Remove Packages

```
uv add package
uv remove package
```

Add the `--dev` flag for development dependencies.

### Manage Python versions

```
uv python install version
uv python upgrade version
uv python uninstall version
```

But if you're updating the version of python inside your project, please remember to change both `pyproject.toml` AND `python-version`

### Run Things

```
uv run script.py
```

Since the virtual environment doesn't get initialized, you might need to use this to run your scripts properly.

#python #python/features 