# RentalManagement
This project is generated with Django + Django REST framework(DRF)

## Environment setup guide  
apply virtual environment:  
`source myvenv/bin/activate`  
Install all required module:   
`pip install django`   
`pip install djangorestframework`  
`pip install django-cors-headers`  
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
