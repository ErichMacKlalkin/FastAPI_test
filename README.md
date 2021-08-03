# FastAPI_test
FAST-API service + Postgres DB allow handling HTTP requests and saving received data.
The service can create a document entity, return it by ID, delete by Id, modify it completely or partially.
The ID field is with autoincrement.
All services work locally and in Docker containers as well. 
To deploy the app with db, please, run the command 'docker-compose up'.
After the containers are up, please, visit http://127.0.0.1:8000/docs to test the functionality.
