# Inventory Database Part : Backend
<img src="https://github.com/slepp22/inventory_database_arduino/blob/main/logo.png?raw=true" alt="Logo" width="30%" />

## Introduction

This project is a collaboration between Centria and Hochschule Darmstadt to develop 
a Locker/Renting/Charging System for universities. 
This repository contains the Backend part, it is based on:
- FastAPI
- SQLAlechemy / alembic

The other repository can be found here :
-  Frontend: https://github.com/kekkeller/inventory_database_frontend/
-  Arduino: https://github.com/slepp22/inventory_database_arduino

## Setting up your local dev-environment
The following steps are based on the assumption you're using PyCharm, some part can differ for other IDEs
### Pre-requisites
- Postgres Database
- Python 
- pip (included in Python since 3.4)
### Set-Up
#### Database
Make sure your local Postgres Database is running, I used this configuration, but you can also use your own as we will 
custom environment variables later on anyway:
```
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'admin')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'admin')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_PORT = os.getenv('DATABASE_PORT', '5432')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'postgres')
```
#### Setup in PyCharm
First thing we need to do, is to Clone the Repository. 
After that we need to create the required environment variables in our Run configuration:

Edit Configuration:
<br><img src="./images/env_1.png" style="width: 300px">

Open List:
<br><img src="./images/env_2.png" style="width: 500px">

Add Environment Variables:
<br><img src="./images/env_3.png" style="width: 500px">

After setting up the environment variables, the next step will be to generate and activate the virtual environment.
There run following command in the terminal:
1) This will generate a virtual environment with the name venv
```bash
python -m venv venv
```
2) Activate the virtual environment
```bash
Windows:
venv\Scripts\activate

MacOS:
source venv/bin/activate 
```
3) Install dependencies
```bash
pip install -r requirements.txt 
```

**Now the development environment is setup and you can start the application by clicking on "Run"**
You should see this message if the setup was successfull:

<img src="./images/app_startup_successfull.png" style="width: 500px">

## Deployment
### Database
The Postgres Database is setup on Google Cloud SQL (Postgres 15)
Please be aware that you cant just connect with to the database Public IP with the credentials. Your own network must 
be added in the Google Cloud Web Interface, so it only allows connection from known networks.

### FastAPI Container
The backend is hosted on Google Cloud Run. To deploy a new version following pre-requisites are needed:
- Google Cloud Run CLI
- Google Cloud Run User with Project Permissions and Authenticated in CLI
- Docker


To deploy a new version a docker please follow these steps:
1) Create new Docker image
```bash
docker buildx build -t sleppp/inventory-backend --platform linux/amd64 .
```
2) Tag image for Google Cloud Run
```bash
docker tag sleppp/inventory-backend gcr.io/inventory-database-420916/inventory-backend
```

3) Push image for Google Cloud Run
```bash
docker push gcr.io/inventory-database-420916/inventory-backend:latest
```

If you encounter any errors during the deployment process, make sure you are authenticated with Google Cloud CLI 
(gcloud auth login) and have the necessary permissions to push images to Google Container Registry. For troubleshooting 
tips or common errors, refer to the Google Cloud Run documentation.


<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeIBbxDL8IrOPwuaB3jFH2bx_lcdh7UUzGndN6Kd6m&s" alt="Alt text" style="width: 300px;" align="left">
<!-- Insert a blank line here -->
<img src="https://www.tha.de/Binaries/Binary19462/Logo-Centria.webp" alt="Alt text" style="width: 300px;" align="center">

