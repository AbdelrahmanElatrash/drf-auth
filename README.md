# drf-auth


## test token 
first way I'm using to test is create python client and make test using requests library for details
[python_client](./py_client/test_book.py)

another one using postman

-  send post method to (http://127.0.0.1:8000/api/token/)
-  add username and password into form
-  copy access token then added to authorization part

- test using post request to create new book without auth token
- test using post request to create new book with auth token

- test refresh token by send post requist to (http://127.0.0.1:8000/api/token/refresh/)
  add refresh key with refresh token ass a value 

[see the test collection](./test_api_token.postman_collection.json)





## docker 

run>>  `docker compose build`
run >>  `docker compose up`
from another terminal at the root dir run 
`docker compose run web python manage.py createsuperuser`
to create super user , no need to do migration , it implemented in the dockor compose file


