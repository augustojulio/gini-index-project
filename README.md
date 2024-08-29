# gini-index-project

This project is a Python application that processes Gini Index data from the 1991 Census provided by IBGE and persists it in a PostgreSQL database. The application was developed using Flask, SQLAlchemy, and Docker.

## Project Structure

- `app/`: Contains the main application code.
  - `main.py`: Application entry point.
  - `config.py`: Application configuration.
  - `models.py`: Data model definitions.
  - `services/`: Business logic.
  - `controllers/`: API routes.
- `data/`: Directory where the `.xls` files should be placed.
- `migrations/`: Directory generated by Alembic for database migrations.
- `tests/`: Contains unit tests for the application.
- `.env`: Environment variables file.
- `docker-compose.yml`: Docker Compose configuration.
- `Dockerfile`: Docker image definition.
- `requirements.txt`: Project dependencies.
- `alembic.ini`: Alembic configuration.

## Features

- **File Processing**: The application reads `.xls` files containing Gini Index data and inserts them into a table in the PostgreSQL database.
- **REST API**: Provides a REST API to process files and retrieve data from the database.
- **Docker**: Uses Docker and Docker Compose for easy deployment and environment configuration.
- **Database Migrations**: Uses Alembic to manage changes in the database schema.
- **Unit Testing**: Includes unit tests to ensure code stability.

## Requirements

- Docker and Docker Compose
- Python 3.8+
- PostgreSQL

## How to Run the Application

1. **Clone the repository**:

   ```sh
   git clone https://github.com/augustojulio/gini-index-project.git
   cd gini-index-project
   ```
2. **Create a `.env` file** at the root of the project with the following environment variables:

   ```
   FLASK_ENV=development
   DATABASE_URL=postgresql+psycopg2://user:password@db:5432/gini_db
   ```
3. **Start the services with Docker Compose** :

   `docker-compose up --build`
4. **Access the application** :

   The application will be available at `http://localhost:5000`.

   Use an HTTP client like Postman or curl:

   `curl -X POST http://localhost:5000/gini/process`

## Running Tests

To run the unit tests:

`docker-compose exec web pytest`

## Database Migrations

Whenever you make changes to the models:

1. Generate a new migration:

   `docker-compose exec web alembic revision --autogenerate -m "Description of change"`
2. Apply the migration:

   `docker-compose exec web alembic upgrade head`

## License

This project is licensed under the [MIT License]().

## Contact

For more information, contact me via email: [augusto.juliogec@gmail.com]().
