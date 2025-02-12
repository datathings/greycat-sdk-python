# Demos

## Python backend for GreyCat explorer

### Setup

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
mkdir -p data
python -m demo.generate_data
```

### Start server

```bash
python -m demo.server
```

### Test Python client

In another terminal:
```bash
python -m demo.client
```