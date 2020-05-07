*Looking for the [Dwellingly App front end?](https://github.com/codeforpdx/dwellingly-app)*

## Dwellingly App Backend

Set up Dwelling Flask Testing Backend (for the first time)
NOTE: Database is SQLite3 via SQLAlchemy 

+ Github Repo: { https://github.com/codeforpdx/dwellinglybackend }
+ Live Server: {https://dwellinglyapi.herokuapp.com/} 

### To Start Server

1. Clone the repo (`git clone https://github.com/codeforpdx/dwellinglybackend.git`)
2. Install Python ( https://realpython.com/installing-python/ )
3. Install pipenv: `pip3 install --user pipenv`
4. Install Python dependencies: `pipenv install`
5. Seed the database
    - Run: `pipenv run python seed_db.py`
      - To re-seed the database from scratch, delete data.db before running the script
    - Look for the file data.db to be created in the root directory

6. Start the server using the flask environment (required every time the project is re-opened):
    - Run: `pipenv run flask run`
    - Run + restart the server on changes:  `pipenv run flask run --reload`

Queries can be made with the Postman Collection link ( https://www.getpostman.com/collections/a86a292798c7895425e2 )

### Endpoints

How to contribute to this project. 
1. Set your origin to https://github.com/codeforpdx/dwellinglybackend.git
2. The Main Branch is Development 
```console
~$: git pull origin development 
```
3. Branch from Development 
```console
~$ git checkout -b <name of branch>
```
go to 


#### ENDPOINT: USER Model

| method | route                  | action                               |
| :----- | :--------------------- | :----------------------------------- |
| POST   | `/register/`           | Creates a new user                   |
| GET    | `/users/`              | Gets all users (dev only)            |
| GET    | `/users/:uid`          | Gets a single user (admin only)      |  
| PATCH  | `/users/:uid`          | Updates a single user                |  not implemented yet
| POST   | `/login     `          | Login a single user                  |
| POST   | `/user/archive/:uid`   | Archives a single user (admin only)  |
| DELETE | `/users/:uid`          | Deletes a single user (admin only)   |


### This Backend Uses JWT for authorization 

Authorization header format:
```javascript
Authorization Bearer < JWT access token >
```

### The database is seeded with 3 default users

```javascript
    [{
        "email": "user1@dwellingly.org",
        "password": "1234",
        "firstName": "user1",
        "lastName": "tester",
        "archived": "false",
        "role": "admin"
    },
    {
        "email": "user2@dwellingly.org",
        "password": "1234",
        "firstName": "user2",
        "lastName": "tester",
        "archived": "false",
        "role": "admin"
    },
    {
        "email": "user3@dwellingly.org",
        "password": "1234",
        "firstName": "user3",
        "lastName": "tester",
        "archived": "false",
        "role": "admin"
    }]
```


#### ENDPOINT: PROPERTIES

| method | route                        | action                                   |
| :----- | :--------------------------- | :--------------------------------------- |
| POST   | `/properties/`               | Creates a new property (admin only)      |
| GET    | `/properties/`               | Gets all properties                      |
| GET    | `/properties/:id`            | Gets a single property (admin only)      |
| PATCH  | `/properties/:id`            | Updates a single property                | not implemented
| PUT    | `/properties/:id`            | Updates a single property (admin only)   | 
| DELETE | `/properties/:id`            | Deletes a single property (admin only)   |
| POST   | `/properties/archive/:id`    | Archives a single property (admin only)  |


```javascript
     {
    "id": "property1",
    "name": "Garden Blocks",
    "address": "1654 NE 18th Ave.",
    "zipCode": "97218",
    "city": "Portland",
    "state": "OR",
    "archived": False
  },
```
#### ENDPOINT: EMAIL

| method | route                | action                     |
| :----- | :------------------- | :------------------------- |
| POST   | `/user/message`      | Send Message to a user     |


#### Example Request
```javascript
     {
    "userid": 1,
    "title": "Test email title",
    "body": "Dwellingly Test email body"
  },
