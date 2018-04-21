#!/bin/sh

# installing python and virtualenv
sudo apt-get update
sudo apt-get install python3.6 -y
sudo apt-get install python3-venv -y


# creating virtual enviroment
python3 -m venv .env
. .env/bin/activate

# installing requirements
pip install -r requirements.txt

# running migrations
python movie_API/manage.py --dev migrate
