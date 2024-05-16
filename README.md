# Theatre-API-Service

## Intro
**Theatre-API-Service** provides a robust platform for managing cinema functionalities such as ticket bookings, performance, and user authentication. This guide details how to set up and run the API locally.

## Features

- **JWT Authentication**
- **Admin Panel**
- **Swagger Documentation**: At `/api/doc/swagger/`.
- **Reservations Management**
- **Play Management**
- **Theatre Halls**
- **Performance Scheduling**

##  How to install

### Using Docker

Follow these steps:

```bash
git clone https://github.com/SysoevDmitro/Theatre-API-Service.git
cd Theatre-API-Service
docker-compose.yaml build
docker-compose.yaml up
```


### Using GitHub

Clone the repository and set up the environment:

```bash
git clone https://github.com/SysoevDmitro/Theatre-API-Service.git
cd Theatre-API-Service
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Apply migrations and run the server
python manage.py migrate
python manage.py runserver
