#!/bin/bash
set -euo pipefail

echo "Deploying flask-todo"

sudo ln -sf /home/brig/code/flask-todo/deploy/systemd.service /etc/systemd/system/flask-todo.service

sudo ln -sf /home/brig/code/flask-todo/deploy/nginx.conf /etc/nginx/conf.d/flask-todo.conf

sudo systemctl daemon-reload
sudo systemctl enable flask-todo.service
sudo systemctl restart flask-todo.service

sudo nginx -t
sudo systemctl reload nginx

echo "Deployment complete for flask-todo"
