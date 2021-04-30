# DevPort
This is a developer portfolio project made using Wagtail CMS.


#
Before local installation, please make sure that you have Python3.6+ and pipenv installed and running on your machine. 

In case you require help setting up pipenv, you can check out these [instructions](https://pipenv-fork.readthedocs.io/en/latest/install.html).
## Run Locally

- Clone the project

```bash
  git clone git@github.com:nickmwangemi/devport.git
```

- Go to the project directory

```bash
  cd devport
```


- Activate virtual environment

```bash
  pipenv shell
```

- Install dependencies

```bash
  pipenv install -r requirements.txt
```

- Build and populate database

```bash
  python manage.py makemigratons
  python manage.py migrate
```

- Create superuser account

```bash
  python manage.py createsuperuser
```

- Start the server

```bash
  python manage.py runserver
```

Crack open the local dev server at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

The admin page is accessible at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)



## Tech Stack

**Client/Server:** Wagtail CMS



## License

[MIT](https://choosealicense.com/licenses/mit/)
