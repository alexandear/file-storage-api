# File Storage API

Simple web server to upload, download and get info about files.

## Getting started

Install dependencies:
```commandline
pip install -r requirements.txt
```

Start an application:
```commandline
uvicorn --factory app.main:create_app --reload
```

# Development

Create and activate virtual environment with [.python-version](.python-version):

```commandline
python -m venv venv
source venv/bin/activate
```

Install dev dependencies:
```commandline
pip install -r requirements-dev.txt
```

Initialize [pre-commit](https://pre-commit.com) hook:
```commandline
pre-commit install
```

Run tests:
```commandline
python -m pytest test
```
