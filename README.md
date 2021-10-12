# RentalManagement
This project is generated with Django + Django REST framework(DRF)

## Environment setup guide  
apply virtual environment:  
`source myvenv/bin/activate`  
Install all required module:   
`pip install django`   
`pip install djangorestframework`  
`pip install django-cors-headers`  
`pip install drf-jwt`  
`pip install djangorestframework_simplejwt`  

## Run server with terminal
`python3 manage.py migrate`  
`python3 manage.py runserver`  
## API Usage  
### Equipment:  
#### Get all equipment:  
GET:`localhost:8000/api/Equipment`  
#### Add to equipment:  
POST:`localhost:8000/api/Equipment`  
Json format:  
{  
    "category": "category",  
    "make": "make",  
    "model": "model",  
    "serial_no":"serial_no"  
}  
#### Delete all equipment:  
DELETE:`localhost:8000/api/Equipment`  
#### Get equipment per id:  
GET:`localhost:8000/api/Equipment/id`  
#### Update data in equipment per id  
PUT:`localhost:8000/api/Equipment/id`  
#### Delete equipment per id:  
DELETE:`localhost:8000/api/Equipment/id`  
### Rental Records:  
#### Get all retal records:  
GET:`localhost:8000/api/Rental`  
#### Add to rental records:  
POST:`localhost:8000/api/Rental`  
Json format:  
{  
"Equiptment" : ["Equiptment"],  
"Vendor" : "Vendor",  
"recieve_time":"2021-10-01 13:00",  
"return_time":"2021-10-01 13:00",  
"rental_rate":"rental_rate",  
"buy_rent": "True/False"  
}  
#### Delete all rental records:  
DELETE:`localhost:8000/api/Rental`  
#### Get rental records per id:  
GET:`localhost:8000/api/Rental/id`  
#### Update data in rental records per id  
PUT:`localhost:8000/api/Rental/id`  
#### Delete rental records per id:  
DELETE:`localhost:8000/api/Rental/id`  
### Vendor:  
#### Get all vendors:  
GET:`localhost:8000/api/Vendor`  
#### Add to vendors:  
POST:`localhost:8000/api/Vendor`  
Json format:  
{  
"sales_person" : "sales_person",  
"address":"address",  
"email":"email@gmail.com"  
}  
#### Delete all vendors:  
DELETE:`localhost:8000/api/Vendor`  
#### Get vendors per id:  
GET:`localhost:8000/api/Vendor/id`  
#### Update data in vendors per id  
PUT:`localhost:8000/api/Vendor/id`  
#### Delete vendors per id:  
DELETE:`localhost:8000/api/Vendor/id`
## JWT Feature:  
### Get access token  
POST:`localhost:8000/api/token/`  
Json format:  
{  
    "username": "user name",  
    "password": "password"  
}  
