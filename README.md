# My first flask app

## Summary

This app my first attempt to write a web application with the [python flask framework](https://pypi.org/project/Flask/).

The app has a database backend storing a simple list of users.

Users can be added, removed, updated from a simple HTML table.

## Requirements

- Python 3.8+
  - Required packages are listed in `requirements.txt`. 
  - Use the following command to install these requirements : `pip install -r requirements.txt`

FOR WINDOWS, install manually the package in lib/win10 and then uncomment 'MySQL-python' from the requirements.txt file.
We recommend the use of pip virtual environment to install the required python packages.

- MariaDB or MySQL database server (see [downloads](https://downloads.mariadb.org/mariadb/10.5.5/))


## Database Setup

- Install MySQL or MariaDB and create a blank database
- Run the scripts from the `.\sql` folder to create the required database objects

## How to Run

- Execute the following command : `python flask_app.py` 
- Start you browser at the following URL : `http://localhost:5000`

## Contributions

Feel free to submit changes and issues on this github repository
