# Project starts up FastAPI server, which can take data from anilist and do REST API on your own server.

# How install
_$ sudo apt-get update_

_$ git clone https://github.com/Max2288/fly_school_django.git_


# How run
Add .env file with your data in repo/education_modules/education_modules

Go to repo/education_modules and run commands:

_$ docker run -d\
    --name education_modules -p 5444:5432 \
    -v $HOME/postgresql/education_modules:/var/lib/postgresql/education_modules \
    -e POSTGRES_PASSWORD=0000 \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_DB=education_db \
    postgres:15.1_

_$ python3.10 -m venv ./venv_

_$ . ./venv/bin/activate_

_$ pip install -r requirements.txt_

_$ python3 manage.py makemigrations_

_$ python3 manage.py migrate_

_$ python3 manage.py runserver_

# After start


## POST request

You can post media on page /educational-modules (Postman recommended)

* Go to Postman
* Query example: _http://127.0.0.1:8000/educational-modules/_


Example of data that we send to post: 

    {
        "module_number": 1,
        "module_name": "test",
        "module_description": "test"
    }

It returns this module:

    {
        "id": "8f824479-cabf-4e01-a03f-9223ebfb7a9a",
        "module_number": 1,
        "module_name": "test",
        "module_description": "test"
    }


## PUT request

You can update media on page /educational-modules/id/ (Postman recommended)
in our case id = 8f824479-cabf-4e01-a03f-9223ebfb7a9a

* Go to Postman
* Query example: _http://127.0.0.1:8000/educational-modules/8f824479-cabf-4e01-a03f-9223ebfb7a9a/_


Example of data that we send to update: 

    {
        "module_number": 2,
        "module_name": "test_2",
        "module_description": "test_2"
    }

It returns this module:

    {
        "id": "8f824479-cabf-4e01-a03f-9223ebfb7a9a",
        "module_number": 2,
        "module_name": "test_2",
        "module_description": "test_2"
    }

## DELETE request

You can delete media from page /educational-modules/id/ (Postman recommended)

* Go to Postman
* Query example: _http://127.0.0.1:8000/educational-modules/8f824479-cabf-4e01-a03f-9223ebfb7a9a/_



# .env
## Below should be your data to project
    SECRET_KEY=django secret
    PG_HOST=database host
    PG_PORT=database port
    PG_USER=database user
    PG_PASSWORD=database password
    PG_DBNAME=database name

    You can take my secret:
    django-insecure-$4woh9*cyf(gr^rj#@5ak6r@zuz8u1!$s1k^qcfbv10p_tlr@z
