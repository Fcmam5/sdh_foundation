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
- [ ] Create `groupes` on your `Django-admin`

### SEO Checklist
- [ ] Create Google analytics and add me as an Admin

### To discuss
- [ ] Create privacy policy and Terms of service pages
- [ ] Create a good 404 Page
- [ ] Put CSS inside CustomCSS block and CSS libraries inside their box, check `base.html` and use page-specific CSS afer including the main/shared css

## Extra Services (Out of service)
أمور خارج عقدنا هذا، نقترح عليكم خدمات إضافية منها
- [ ] Linking to your Social media (Creating accounts, Link website to them for SEO & Engagment), social buttons ?
- [ ] Prepare articles for printing (Print Article page)
- [ ] Add sponsors to events
- [ ] Add captcha to contact and registration form for avoid spams
