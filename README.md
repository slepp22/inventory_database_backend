# Inventory Database Part : Backend
<img src="https://github.com/slepp22/inventory_database_arduino/blob/main/logo.png?raw=true" align="right" alt="Logo" width="30%" />

This project is a collaboration between Centria and Hochschule Darmstadt to develop a Locker/Renting/Charging System for universities. This repository contains the Backend part.
## Introduction

This project is a collaboration between Centria and Hochschule Darmstadt to develop 
a Locker/Renting/Charging System for universities. 
This repository contains the Backend part, build with the help of FastAPI.

The other repository can be found here :
-  Frontend: https://github.com/kekkeller/inventory_database_frontend/
-  Arudino: https://github.com/slepp22/inventory_database_arduino

## Features
- Login API

## Installation process for further development

1. Clone the Repository
```console
git clone https://github.com/slepp22/inventory_database_backend
```
Perform the folliwing steps in Pycharms Terminal:
2. Create a Virtual Environment: Create a virtual environment using: 
```console
python -m venv command 
```
3. Activate the Virtual Environment by using: 
```console
source venv/bin/activate 
```
4. Install Dependencies listed in the requirements.txt file using:
```console
pip install -r requirements.txt
```

## Database
### Alembic
Used for managing database schema migrations, such as creating, modifying, and reverting database schema changes
Create Migration File (Versions)
```console
alembic revision --autogenerate
```
Migrate changes to Database
```console
alembic upgrade head
```

## Deployment Process

Will be displayed with the Release of the Beta Version

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeIBbxDL8IrOPwuaB3jFH2bx_lcdh7UUzGndN6Kd6m&s" alt="Alt text" style="width: 300px;" align="left">
<!-- Insert a blank line here -->
<img src="https://www.tha.de/Binaries/Binary19462/Logo-Centria.webp" alt="Alt text" style="width: 300px;" align="center">
