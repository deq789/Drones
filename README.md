# Drones
Musala Soft Practical Task

## Requirements 
* You should have Python installed (test with version 3.7.2). 

## Install 
Clone this repo, create and activate virtual env:
```console
git clone https://github.com/deq789/Drones.git
cd Drones
mkdir venv
python -m venv venv
venv\Scripts\activate.bat # Windows
source venv/bin/activate   # Linux
```

Setup dependencies:
```console
pip install -r requirements.txt
```


## Run migrate 
```console
python manage.py migrate
```


## Run the server 
```console
python manage.py runserver --noreload
```


## Load seed data 
```console
python manage.py loaddata data.json
```


## Tests 
```console
python manage.py test apps.core.tests
```

## Tests 
```console
python manage.py test apps.core.tests
```

## Endpoints
* List and create drones </br>
[GET, POST] http://localhost:8000/api/v1/drones/</br>
Post json sample:
```
{
    "serial_number": "serial-number-10",
    "model": "Middleweight",
    "weight_limit": "470",
    "battery_percentage": 40,
    "state": "LOADING"
}
```

* Load medication into drones 
*[POST] http://localhost:8000/api/v1/drones/load-medication</br>
*Json sample:
```
{
    "drone": "serial-number-10",
    "medications": [
        {
            "name": "m1",
            "weight": 10,
            "code": "CODE_1"
        },
        {
            "name": "m2",
            "weight": 400,
            "code": "CODE_2"
        }
    ]
}
```

* Check drone medication</br>
[GET] http://localhost:8000/api/v1/drones/check-medication/{drone_serial_number}</br>

* Drone detail</br>
*[GET] http://localhost:8000/api/v1/drones/{drone_serial_number}/</br>

