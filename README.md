# Movies API #

### Clonation of repository ###
$ git clone https://github.com/antobarbero/movies_API.git

________________________________________________________________________


### How do I get set up? ###

Just run the following command for setup (Tested on Ubuntu 17.10)

```
$ sh setup_project.sh
```
* It will create a virtual enviroment, install the requirements and run the migrations.



#### Or manually follow these steps: ####


1. install python and virtualenv

```
$ sudo apt-get update

$ sudo apt-get install python3.6 -y

$ sudo apt-get install python3-venv -y

```

2.  create a virtual enviroment and activate it.

```
$ python3 -m venv .env

$ . .env/bin/activate
```


3. install the project requirements (with the virtual enviroment activated)

```
$ pip install -r requirements.txt
```

4. Run the database migrations

```
$ python movie_API/manage.py --dev migrate
```

________________________________________________________________________

### Run the server ###

```
$ ./movies_API/manage.py runserver
```

### Create a super user ###

```
$ ./movies_API/manage.py createsuperuser
```
________________________________________________________________________

### API documentation at home ###

http://127.0.0.1:8000

________________________________________________________________________

### How to run tests ###
```
$ ./movies_API/manage.py test movies_API
```
