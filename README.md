Based on ['Python Django Dev To Deployment course'](https://learning.oreilly.com/videos/python-django-dev/9781838641283)



_________

WORK FLOW:

Project:
1. **Create project** - django-admin startproject real_estate
2. **Add gitignore & readme**

Pages app:
1. **Create app _pages_** - python manage.py startapp pages
2. **Add _pages_ to real_estate/settings.py INSTALLED_APPS list**
3. **Create pages/urls.py**
4. **Include pages/urls.py to real_estate/urls.py**
5. **Create views in pages/views.py to return index.html & about.html**

Static files:
1. **Create real_estate/static with /css, /img, /js, /webfonts**
2. **Update real_estate/settings.py to add STATIC_ROOT, STATICFILES_DIRS**

Templates:
1. **Create /templates**
2. **Update real_estate/settings.py to lead to /templates in TEMPLATES->DIRS**
3. **Create base.html, pages/index.html & pages/about.html** - base.html contains nav bar, header & footer references, 
index and about - extend base and have only content
4. **Create /partials with _navbar.html, _topbar.html, _footer.html**
5. **Point to static img inside of htmls with {% static 'name' %} and to correct url page with {% url 'name' %}**

Listings & Realtors apps:
1. **Create app _listings_** - python manage.py startapp listings
2. **Create app _realtors_** - python manage.py startapp realtors
3. **Add _listings_ and _realtors_ to real_estate/settings.py INSTALLED_APPS list**
4. **Create templates/listings with listings.html, listing.html, search.html** - not for realtors, 
they wouldn't have separate realtors page (will be only as part of existing pages)
5. **Create listings/urls.py** - not for realtors, same reason as above
6. **Include listings/urls.py to real_estate/urls.py**
7. **Create views in listings/views.py to return listings.html, listing.html, search.tml**

Connect Postgres:
1. **Create new db**
2. **Install psycopg2 (Postgres adapter)** - pip install psycopg2, pip install psycopg2-binary
3. **Update real_estate/settings.py DATABASES section**
4. **Run init migration** - python manage.py migrate
5. **Create superuser** - python manage.py createsuperuser

Create models:
1. **Create listings/models.py with Listing model**
2. **Create realtors/models.py with Realtor model**
3. **Create migrations** - python manage.py makemigrations
4. **Run migrations** - python manage.py migrate

Admin:
1. **Register Listing in listings/admin.py**
2. **Register Realtor in realtors/admin.py**
