import os

APP_ENV = os.environ.get('APP_ENV', 'development')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'admin')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'admin')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_PORT = os.getenv('DATABASE_PORT', '5432')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'postgres')
