# forloop_rwanda_bucketlist_app
This repos contains the code and instruction we will be using during forloop rwanda bootcamp

We will be [the following](https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way) tutorial in order to build http://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/ 
a restfull api with python flask and may be the TDD way.

#### Make sure you have python, virtual environnement installed.
to check use:

```
python -version 
```

you should have python 3 

if you have both python2 and 3 installed you can check using 

```
python3 -version 
```

## First step is to create a project directory

```
mkdir bucketlist
```

and then cd :

```
cd  bucketlist
```


## Create a virtual environment :

using the following command :

```
 virtualenv -p python3 path/to/virtualenv
 ```
 and activate it with
 
 ```
 source path/to/virtualenv/bin/activate
 ```
 
 ## create the application folder structure :
 
 create the following directory:
 
 ```
 mkdir app instance
 ```
 
 and the following files :
 
 ```
 touch manage.py requirement.txt run.py test_buckeliist.py
 ```
 
 and this :
 
 ```
 touch app/__init__.py app/model.py instance/__init__.py instance/config.py
 ```

make sure we have the same application folder structure by doing 


```
tree
```

you should have the same directory structure as me 


```.
├── app
│   ├── __init__.py
│   └── model.py
├── instance
│   └── __init__.py
├── manage.py
├── requirement.txt
├── run.py
└── test_buckeliist.py

```
## Install Flask

After doing this, install Flask using pip.


```
pip install flask, flask_script
```

## Environment Configurations

we will write the code in instance config


## Export 

```
export SECRET="some-very-long-string-of-random-characters-CHANGE-TO-YOUR-LIKING"
```

```
export APP_SETTINGS="development"
```
## creating the api

edit the app/__init__file  and the run.py file  without application factory
and check hello world


run.py 

## Configuring the Database

Use postgres sql as shown in the tutorial

```

## Edit the app with application factiry

## Data Model

model.py

## Update the manager script


## api functionality



