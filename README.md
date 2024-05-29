# Email Client

This Django Email Client uses **Django 5**, **HTML 5**, **CSS 3**, **Bootstrap 5**, **React**, **JavaScript**.


## Table of Contents 
- [Prerequisites](#prerequisites)

- [Installation](#installation)
- [Run the application](#run-the-application)
- [URL to View the website](#URl to view the-application)
- [Copyright and License](#copyright-and-license)


### Prerequisites

Install the following prerequisites:

1. [Python 3.11.0](https://www.python.org/downloads/)
<br> This project uses **Django v5.0.6**. In order for Django to work, you must install a correct version of Python on your machine. More information [here](https://django.readthedocs.io/en/stable/faq/install.html).
   
3. [Visual Studio Code](https://code.visualstudio.com/download) or [Pycharm](https://www.jetbrains.com/pycharm/) 


### Installation

#### 1. Create a virtual environment

From the **root** directory, run:

```bash
python -m venv venv
```

#### 2. Activate the virtual environment

From the **root** directory, run:

On macOS & Unix:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\scripts\activate
```

#### 3. Install required dependencies

From the **root** directory, run:

```bash
pip install -r requirements.txt
```

#### 4. Run migrations

From the **root** directory, run:

```bash
make migrations
or 
python manage.py makemigrations
```
```bash
make migrate
or 
python manage.py migrate

```


### Run the application

From the **root** directory, run:

```bash
python manage.py runserver

or
 
make runserver
```


### URL to View the application

Go to http://127.0.0.1:8000/ to view the application.



### Copyright

Copyright © 2024 TB-&-CW.