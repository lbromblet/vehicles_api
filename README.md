# Vehicles API

## Setup Project

### Docker

The project can be run directly in a Docker environment with docker and docker-compose installed.

```bash
docker-compose up
```

Generate a local copy of ./vehicles_api/local_settings.py

```bash
cp local_settings_example.py local_settings.py
```

Set environment dependent settings in local_settings.py, by default the settings are configured to run in development environment.

- DEBUG 
- ALLOWED_HOSTS
- SECRET_KEY 
- CORS_ALLOW_ALL_ORIGINS
- CORS_ALLOWED_ORIGINS
- ACCESS_TOKEN_LIFETIME
- REFRESH_TOKEN_LIFETIME
- SLIDING_TOKEN_LIFETIME
- SLIDING_TOKEN_REFRESH_LIFETIME

Generate a local copy of .env

```bash
cp .env.example .env
```

Set environment dependent credentials in .env, by default the settings are configured to run in development environment.

- SECRET_KEY 
- MAIN_DATABASE_NAME
- MAIN_DATABASE_USER
- MAIN_DATABASE_PASSWORD
- MAIN_DATABASE_HOST
- MAIN_DATABASE_PORT

## Tests

Run tests in the docker container

```bash
docker exec -it vehicules_api bash
python manage.py test
```

## Documentation

A full working __swagger-ui__ view of this API specification can be found at ```/swagger/```

## Specifications

#### Users
* Anyone can create user.
* Deleting a user will delete related vehicles.
* A user can only delete his own account.
* After deleting an account don't forget to remove authorization header credentials or request will return *401 Error: Unauthorized*. Removing auth token is also normally what the client will do on logout or when the token refresh request response status code is not 200 (successful).

#### Vehicles
* Only authenticated user can create vehicles.
* Only owners of a vehicle can update/create/delete the vehicle.

#### Pagination
* Default pagination size is set to 5.
* API endpoint for ```/vehicles/``` (GET) include query parameter ```page_size``` that allows the client to set the page size on a per-request basis.
* Accept a page number in the request query parameters. url example : ```/api/vehicles/?page=1&page_size=10```.
* Default ordering is using created date value. Available keys for ordering are ```price``` and ```created```.
* Ordering is parameterizable with ```ordering``` query parameter. example : ```/api/vehicles/?ordering=-price```

#### Authentication
Usually, JWT can be used in RESTful APIs. For production it is highly recommended to use HTTPS with a valid SSL certificate.
Expected flow for creating/editing/deleting vehicle with __JWT authentication__ :
* Create a user, endpoint ```/users/``` (POST)
* Get access/refresh token ```/token/``` (POST). Default lifetime is 5 minutes but can be modified in /vehicles_api/local_settings.py config file of the project.
* Authorize POST, DELETE and PUT/PATCH requests types by adding the token value in the request header.
Format is : __Authorization: \<type\> \<credentials\>__ with type __Bearer__ (do not forget to include it !)

## Improvements

* Consider using foreign key for Vehicle Type instead of hard-coded choices.
