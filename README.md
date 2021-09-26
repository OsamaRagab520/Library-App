# Library-App
### Description
Library app, a web app via which you can manage the interaction between the students and library's books.

this is the first version which implement the necessary features __only__.

### Code style
All backend code follows [**PEP8 style guidelines**](https://www.python.org/dev/peps/pep-0008/)

### Pre-requisites and Local Development
Developers using this project should already have Python3, pip and sqlite installed on their local machines.

To configure the environment we will use `pipenv`:

    $ pip install --user pipenv
    $ pipenv sync
    $ pipenv shell
    $ python manage.py runserver

The application is run on `http://127.0.0.1:5000/` by default.

### Project Structure
    │   db.sqlite3
    │   manage.py
    │   Pipfile
    │   Pipfile.lock
    │
    ├───accounts
    │   │   admin.py
    │   │   apps.py
    │   │   forms.py
    │   │   models.py
    │   │   tests.py
    │   │   urls.py
    │   │   views.py
    │   │   __init__.py
    │   │
    │   └───migrations
    │         0001_initial.py
    │         __init__.py
    │
    ├───config
    │       asgi.py
    │       settings.py
    │       urls.py
    │       wsgi.py
    │       __init__.py
    │
    ├───library
    │   │   admin.py
    │   │   apps.py
    │   │   forms.py
    │   │   models.py
    │   │   tests.py
    │   │   urls.py
    │   │   views.py
    │   │   __init__.py
    │   │
    │   ├───migrations
    │   │       0001_initial.py
    │   │       0002_auto_20210920_1130.py
    │   │       0003_alter_comment_article.py
    │   │       __init__.py
    │   │
    │   └───templates
    │       └───library
    │               book_borrow.html
    │               book_delete.html
    │               book_detail.html
    │               book_edit.html
    │               book_list.html
    │               book_new.html
    │               student_detail.html
    │               student_edit.html
    │               student_list.html
    │
    ├───pages
    │   │   admin.py
    │   │   apps.py
    │   │   models.py
    │   │   tests.py
    │   │   urls.py
    │   │   views.py
    │   │   __init__.py
    │   │
    │   └───migrations
    │         __init__.py
    │   
    │
    └───templates
        │   base.html
        │   home.html
        │
        └───registration
                login.html
                password_change_done.html
                password_change_form.html
                password_reset_complete.html
                password_reset_confirm.html
                password_reset_done.html
                password_reset_form.html
                signup.html

## Class diagram
![Class](https://github.com/osamaragab520/Library-App/blob/main/static/class_diagram.png)

## Acknowledgements & Final words
This is the project of ITI summer training with some personal touches. Of course there will be imperfections, flaws that might need some more work.

thanks Eng.Noha Shehab for your time & effort.
