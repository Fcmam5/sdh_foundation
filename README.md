## Setup

First clone this repository and install your requirements
```shell
git clone https://github.com/Fcmam5/sdh_foundation && cd sdh_foundation

pip install -r requirements.txt
```

Then create a python file called `config_secrets.py` under `sdh_foundation/` alongside `settings.py`

```python
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
#TODO Change this
EMAIL_HOST_USER = 'GMAIL ADDRESS'
EMAIL_HOST_PASSWORD = 'GMAIL APPLICATION CODE'
```

## Running this project for the first time
- [ ] Run `python manage.py makemigrations && python manage.py migrate --run-syncdb`
- [ ] Create super user
- [ ] Create search index
- [ ] Edit domain on `/admin` , change `example.com` to your domain

### SEO Checklist
- [ ] Create Google analytics and add me as an Admin

### To discuss
- [ ] Add image models to admin page for writing Alt text (for SEO & Web accessibility)
- [ ] Add description to Article model and display in a meta tag
