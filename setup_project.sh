#!/bin/sh

# installing python and python venv
sudo apt-get update
sudo apt-get install python3.6 -y
sudo apt-get install python3-venv -y


# creating virtual environment
python3 -m venv .env
. .env/bin/activate

# installing requirements
pip install -r requirements.txt

# running migrations
./movies_API/manage.py migrate
