
# Run locally



```
source .venv/bin/activate
noglob uv pip install -e .[test]
uv run mcp-server-code-assist
```


# Install uvx

```
uvx mcp-server-code-assist
```

# Build

```
noglob uv pip install -e .[test]
uv sync
uv pip install build twine
python -m build
python -m twine upload dist/*
```