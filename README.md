# flask-todo

## Run locally

```
touch app.db
```

I don't have a script for it yet, but you'll also have to initialize the database before running the server.

```
python app.py
```

## Deploy to production

```
pm2 start pm2.json
```

Behind the scenes this runs `python3 -m gunicorn -w 1 --bind 0.0.0.0:5001 wsgi:app`. This runs the app with gunicorn on the right port, then pm2 manages it, handling automatic restarts. `-w 1` means just use 1 worker process (doing this because I have only 1 CPU on the virtual server). If you try to run gunicorn without pm2 and want it in the background, you'll need to add the `--daemon` flag.
