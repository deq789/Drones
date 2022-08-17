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
source env/bin/activate   # Linux
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
