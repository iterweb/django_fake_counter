# Fake Visitor Counter
[![Downloads](https://pepy.tech/badge/fake-count)](https://pepy.tech/project/fake-count)<br>Fake Counter is a simple Django app for displaying a random number based on the time of day.
### Quick start
* Install:<br> ```pip install django-fake-counter-0.1.tar.gz```<br>or<br>```pip install fake-count```
* Add ```fake_count``` to your **INSTALLED_APPS** setting like this:<br>
```python3
INSTALLED_APPS = (
        ...
        'fake_count',
    )
```
* Add these settings to ```settings.py``` file in your project:<br>
```python3
CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': os.path.join(BASE_DIR, 'fake_count_cache'),
        }
    }
    # optional
    MAX_COUNT_DAY = integer value # default 500
    MAX_COUNT_NIGHT = integer value # default 200
```
* Load ```{% fake_count_tmpl %}``` in your html template and use it like ```{% fake_counter %}```:<br>
```html
{% load fake_count_tmpl %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>
            <p>Some text</p>
            <p>{% fake_counter %}</p>
        </body>
    </html>
``` 
---
License: [The 3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause) <br>
Copyright (c) 2021, [Pro100git](https://github.com/pro100git)
