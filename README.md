# Movies API #

### Clonation of repository ###
$ git clone https://github.com/antobarbero/movies_API.git

________________________________________________________________________


### How do I get set up? ###

Just run the following command for setup (Tested on Ubuntu 17.10)

```
$ sh setup_project.sh
```
* It will create a virtual environment, install the requirements and run the migrations.



#### Or manually follow these steps: ####


1. install python and python venv

```
$ sudo apt-get update

$ sudo apt-get install python3.6 -y

$ sudo apt-get install python3-venv -y

```

2.  create a virtual environment and activate it.

```
$ python3 -m venv .env

$ . .env/bin/activate
```


3. install the project requirements (with the virtual environment activated)

```
$ pip install -r requirements.txt
```

4. Run the database migrations

```
$ ./movies_API/manage.py migrate
```

________________________________________________________________________

### Activate python virtual environment ###

```
$ . .env/bin/activate
```
________________________________________________________________________

### Run the server ###

```
$ ./movies_API/manage.py runserver
```
________________________________________________________________________


### Login at: ###

http://127.0.0.1:8000/api-auth/login/

________________________________________________________________________

### API documentation at home ###

http://127.0.0.1:8000

________________________________________________________________________

### How to run tests ###
```
$ ./movies_API/manage.py test movies_API
```

________________________________________________________________________

### Used libraries and frameworks ###

* Django==2.0.4
* djangorestframework==3.8.2
* coreapi==2.3.3
* flake8==3.5.0
* isort==4.3.4
