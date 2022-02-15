# High Fidelity Prototype

The High Fidelity prototype is a web application that illustrates how the authentication system will function in yardwrk

## Required Technologies

Make sure you have python installed on your computer

pip install the following python modules using your terminal and the commands belows

```
pip install django
```
```
pip install django-crispy-forms
```

## Build Instructions

Open the `djangoProject` directory in your terminal

Run the following commands to prepare the app to be ran

```
python manage.py makemigrations
```
```
python manage.py migrate
```

## Running the app

Again, open the `djangoProject` directory in your terminal

To run the application, run the command below

```
python manage.py runserver
```

The web application is reachable at the following link

```
http://localhost:8000/accounts/home
```