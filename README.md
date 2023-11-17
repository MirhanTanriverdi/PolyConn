# PolyConn: Local Cafe and Event Discovery Platform


## Project Overview

PolyConn is a Django-based web application designed to connect users with local cafes and events in their districts. It enables users to discover events, manage profiles, participate in community activities, and interact with local cafes.

## Getting Started

These instructions will guide you through setting up PolyConn on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3
- pip (Python package manager)
- PostgreSQL
- Virtualenv (optional, but recommended)

### Installation

1. **Clone the Repository**
```
git clone https://github.com/MirhanTanriverdi/PolyConn.git 
```

2. **Set Up a Virtual Environment (Optional)**
```
virtualenv venv
source venv/bin/activate  
```

On Windows, 
```
use venv\\Scripts\\activate
```

3. **Install Dependencies**
```
pip install -r requirements.txt
```

4. **Database Setup**
- Make sure PostgreSQL is installed and running on your system.
- Create a new PostgreSQL database named `polyconn_db`.
- Update the `DATABASES` configuration in your `settings.py` file with your database credentials.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'polyconn_db',
        'USER': '[Your Database Username]',
        'PASSWORD': '[Your Database Password]',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

### Run Database Migrations

```
python manage.py makemigrations

python manage.py migrate

```


### Start the Development 

```
python manage.py runserver
```

1. After Running the localhost, you can access the mock data of Users, Districts, and Cafes  by using the paths in urls.py

```
distirct/ 
user/
cafe/
```

## ER Model Documentation

Refer to `ERD.png` in the project's `docs` directory for a detailed Entity-Relationship Diagram of the database.

## Contributing

Please read `CONTRIBUTING.md` for details, You can review the file in `docs` directory. 

## Data Layer Demonstration

Please read `DATALAYERDEMON.md` for details, You can review the file in `docs` directory. 

## User Cases

Please read `USECASE.md` for details, You can review the file in `docs` directory. Plus, Entity-Relational Diagram can be found as PNG and A link in `USECASE.md`. 