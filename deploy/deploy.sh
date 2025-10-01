#!/bin/bash
set -euo pipefail

echo "Deploying flask-todo"

# nginx

sudo cp /home/brig/code/flask-todo/deploy/nginx.conf /etc/nginx/conf.d/flask-todo.conf

sudo nginx -t
sudo systemctl reload nginx

# systemd

sudo cp /home/brig/code/flask-todo/deploy/systemd.service /etc/systemd/system/flask-todo.service

sudo systemctl daemon-reload
sudo systemctl enable flask-todo.service
sudo systemctl restart flask-todo.service

echo "Deployment complete for flask-todo"
