# x_pear_mnt

## Overview

`x_pear_mnt` is a REST API project developed using Django and Django REST Framework. This project serves as a demonstration of creating a simple yet functional API in Django, connecting to a PostgreSQL database, and deploying using Docker Compose.

## Components

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Django REST Framework**: A powerful and flexible toolkit for building Web APIs in Django.
- **PostgreSQL**: An advanced open-source relational database.
- **Docker Compose**: A tool for defining and running multi-container Docker applications.

## Features

- CRUD operations for entities: Actors, Transporters, Loads, and Storages.
- Connection to PostgreSQL database using Django ORM.
- Deployment setup using Docker Compose.
- RESTful API design, offering a modern approach to web server architecture.
- Use of Django's robust ORM for database interactions, ensuring efficient and secure data handling.

## Setup and Running

1. Clone the repository.
2. Navigate to the project directory.
3. Use `docker-compose up --build` to build and start the containers.
4. Use `python manage.py makemigrations` to prepare database migrations.
5. Use `python manage.py migrate` to affect the database structure.
6. Use `python manage.py runserver localhost:8000` to boot-up the service.
7. Access the API at `http://localhost:8000/`.

## API Endpoints

- `/api/actors/`: Manage actor data.
- `/api/transporters/`: Interact with transporter information.
- `/api/loads/`: Handle load details.
- `/api/storages/`: Access and modify storage data.

Each endpoint supports standard HTTP methods (GET, POST, PUT, DELETE) for full CRUD functionality.

## Other Endpoints

- `/`: a small welcoming html
- `/admin`: the default django admin page where you need to first create a user :)

## Personal Note:

First, I have to say that this is absolutely the first time in my life using python as a backend tool and im not disappointed. I'm sure such a service will perform slower than one written in GO but its worth having in my "magic hat".

As someone deeply invested in backend technologies, I find Python backend frameworks like Django quite fascinating. Django, with its comprehensive suite of tools and functionalities, makes it a robust choice for quick development. However, my experience also tells me to approach such powerful frameworks with caution.

In my initial run with Django, I noticed it exposed some sensitive environment data, a reminder that every tool, no matter how efficient, needs careful handling. Personally, I lean towards more traditional and proven back-end solutions like Java Spring, Quarkus, and even faster options like Go or C++. While I appreciate the innovation and ease Django brings to the table, my preference lies in the reliability and control offered by these "old school" technologies.
