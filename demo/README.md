# Demos

## Python backend for GreyCat explorer

### Setup

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
mkdir -p data
python -m demo.generate_data
mkdir -p demo/js/webroot/web
curl -L https://get.greycat.io/files/sdk/web/dev/7.0/7.0.301-dev.js -o demo/js/webroot/web/greycat.js
```

### Start server

```bash
python -m demo.server
```

Demo is then accessible at http://localhost:5000
