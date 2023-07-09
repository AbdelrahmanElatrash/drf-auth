import requests
from test_get_jwt import access_token , headers

import requests


# create 
end_point='http://127.0.0.1:8000/api/v1/books/'  

data={'title': 'book 1',
      'auther_name':'auther',
       'release_date':"1990-01-01",
       'img_url':'https://media.licdn.com/dms/image/C560BAQHMnA03XDdf3w/company-logo_200_200/0/1519855918965?e=2147483647&v=beta&t=J3kUMZwIphc90TFKH5oOO9Sa9K59fimgJf-s_okU3zs',
       'description':'book description',
       'user':1}
response=requests.post(end_point,headers=headers, json=data)


########################################################################################
# list view
end_point='http://127.0.0.1:8000/api/v1/books/'   


response=requests.get(end_point,headers=headers)

print(response.json())

######################################################################################

# details view 

end_point='http://127.0.0.1:8000/api/v1/books/1'

response=requests.get(end_point,headers=headers)

print(response.json())




