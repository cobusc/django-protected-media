# protected-media-prototype
Separate handling of protected media in Django, with X-Sendfile support


## Accessing the application via Nginx

### Configure `nginx`
Modify `demo_nginx.conf` to use suitable paths, then make it available:
```
sudo ln -s demo_nginx.conf /etc/nginx/sites-enabled/
sudu service nginx reload
```
Nginx should now be listening om port 8000.

### Start `uwsgi`
Start the `uwsgi` server which uses port 8001:
```
./venv/bin/uwsgi --ini demo.ini
```
