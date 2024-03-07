# flask-todo

## Run locally

```
python app.py
```

## Command to run gunicorn

`python3 -m gunicorn -w 1 --bind 0.0.0.0:5001 wsgi:app --daemon`

Just 1 worker process because I only have 1 CPU on the virtual server

The `--daemon` starts it in the background
