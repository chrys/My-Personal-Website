bind = "unix:/run/fasolaki.sock"
workers = 3
errorlog = "/var/log/gunicorn/error.log"
accesslog = "/var/log/gunicorn/access.log"
loglevel = "warning"