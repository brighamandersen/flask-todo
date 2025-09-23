# flask-todo

### Installation

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
touch app.db
```

I don't have a script for it yet, but you'll also have to initialize the database before running the server.

### Virtual environment commands

Create virtual environment

```
python -m venv .venv
```

Activate virtual environment

```
source .venv/bin/activate
```

Deactivate virtual environment

```
deactivate
```

Update requirements.txt with currently installed dependencies

```
pip freeze > requirements.txt
```

Install dependencies listed in requirements.txt

```
pip install -r requirements.txt
```

### Usage locally

```
python app.py
```

### Usage/deployment to production

```
cd path/to/repo
./deploy.sh
```
