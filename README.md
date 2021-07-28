[![Build Status](https://travis-ci.com/KITHU/Cocktail_Api.svg?branch=develop)](https://travis-ci.com/KITHU/Cocktail_Api)
[![Coverage Status](https://coveralls.io/repos/github/KITHU/Cocktail_Api/badge.svg?branch=develop)](https://coveralls.io/github/KITHU/Cocktail_Api?branch=develop)

# **Cocktail-Api**
### **API Documentation**
- Click [here](https://cocktailapiv1.herokuapp.com/) to view swagger API documentation

## **Set Up Development Environment:**
- Clone the repo and cd into it:
  ```
- Install all Dependancies
  ```
   pipenv install 
  ```

- Make a copy of the .env.sample file and rename it to .env and update the variables accordingly
- Activate a virtual environment:
  ```
    pipenv shell
  ```
- Apply migrations:
  ```
    python manage.py migrate

  ```
- Run App
  ```
    python manage.py runserver
  ```

- Run Tests
  ```
    pytest
  ```

## **Endpoints:**
### Register

`POST /api/v1/auth/register/`

Example request body:
``` 
{
    "username":"doe",
    "email":"doe@gmail.com",
    "password":"1234"
}

```

### Login
`POST /api/v1/auth/login/`

Example request body:
``` 
{
    "email":"doe@gmail.com",
    "password":"1234"
}
```

## **Cocktails**
### create cocktail
`POST /api/v1/cocktail/create/`

Example request body:
``` 
{
    "name": "vodka",
    "price": 205.00
}
```
Authentication required, returns cocktail object.

### Retrieve user cocktails
`GET /api/v1/cocktail/retrieve/`

Authentication is required, return all  cocktails that belong to the signin user

### List all cocktails
`GET /api/v1/cocktail/list/`

Authentication isn't required, return a list of all available cocktails in the system
