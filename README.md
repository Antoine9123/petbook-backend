# API Documentation

This API provides access to pet data as well as authentication features via JWT for users.
# Authentication

Authentication is done via JSON Web Tokens (JWT). Users can obtain a JWT token by providing their username and password via the /auth/login/ endpoint. **This token MUST then be included** in the authentication header to access other API endpoints.

To obtain a new token (refresh the token), users can use the /auth/jwt/refresh/ endpoint with their current JWT token.
## Authentication Endpoints

    [POST] /auth/signup/: Create a new user account.
    [POST] /auth/login/: Obtain a JWT token for authentication.

###  /auth/signup/ [POST]

#### input (post)
```
{
    "username": "string",
    "email": "string",
    "password": "string"
}
```
###  /auth/login/ [POST]
#### input (post)
```
{
    "email": "string",
    "password": "string"
}
```
# Pet Routes
    [GET/POST] /api/pets/: Retrieve a list of all pets or add a new one.
    [GET/PUT/DELETE] /api/pets/<id>/: Retrieve, update, or delete a specific pet by ID.
    [GET] /api/pets/get-pets-from/<username>/: Retrieve a list of pets owned by a specific user.

### /api/pets/  [GET/POST]
#### input (post)
```
{
    "name": "string",
    "gender": "string",
    "birth": "date",
    "description": "string (optional)",
    "photo_url": "string"
}
```
#### output (get)
```
[
    {
        "id": "integer",
        "name": "string",
        "gender": "string",
        "birth": "date",
        "age": "string",
        "description": "string (optional)",
        "photo_url": "string"
    },
    ...
]
```

###  /api/pets/:id/ [GET/PUT/DELETE]
PUT and DELETE methods, access is restricted to the owner of the pet

#### input (put)
```
{
    "name": "string",
    "gender": "string",
    "birth": "date",
    "description": "string (optional)",
    "photo_url": "string"
}
```
#### output (get)
```
{
    "id": "integer",
    "name": "string",
    "gender": "string",
    "birth": "date",
    "age": "string",
    "description": "string (optional)",
    "photo_url": "string"
}
```

###  /api/pets/get-pets-from/:username/ [GET]
#### output (get)
```
[
    {
        "id": "integer",
        "name": "string",
        "gender": "string",
        "birth": "date",
        "age": "string",
        "description": "string (optional)",
        "photo_url": "string"
    },
    ...
]
```

# Post Routes
    [GET/POST] /api/posts/: Retrieve a list of all posts or add a new one.
    [GET/PUT/DELETE] /api/posts/<post_id>/: Retrieve, update, or delete a specific post by ID.
    [GET] get-post-from/<int:pet_id>/: Retrieve a list of posts for a specific pet ID.
    [GET] get-post-by/<str:category>/: Retrieve a list of posts for a specific pet category.

### /api/posts/  [GET/POST]
#### input (post)
```
{
    "description": "string",
    "photo_url": "string",
    "pet" : "integer(id)"
}
```
#### output (get)
```
[
    {
        "id": "integer",
        "description": "string",
        "photo_url": "string",
        "pet": 'integer(id)'
    },
    ...
]
```

###  /api/posts/:id/ [GET/PUT/DELETE]
PUT and DELETE methods, access is restricted to the owner of the post

#### input (put)
```
{
    "description": "string",
    "photo_url": "string",
    "pet" : "integer(id)"
}
```
#### output (get)
```
{
    "id": "integer",
    "description": "string",
    "photo_url": "string",
    "pet": 'integer(id)'
}
```

###  get-post-from/:pet_id/ [GET]
#### output (get)
```
[
    {
    "id": "integer",
    "description": "string",
    "photo_url": "string",
    "pet": 'integer(id)'
    },
    ...
]
```

###  get-post-by/:category/ [GET]
#### output (get)
```
[
    {
    "id": "integer",
    "description": "string",
    "photo_url": "string",
    "pet": 'integer(id)'
    },
    ...
]
```