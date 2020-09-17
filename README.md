# My first flask app

## Summary

This app my first attempt to write a web application with the [python flask framework](https://pypi.org/project/Flask/).

The app has a database backend storing a simple list of users.

Users can be added, removed, updated from a simple HTML table.

## Requirements

- Python 3.8+
- Flask (install with `pip install flask`)

## Database Setup

Install MySQL and create a simple database with one table called `users` and the following table structure :

| column | datatype | constraints |
| ------ | -------- | ----------- |
| id | INT | AUTO_INCREMENT PRIMARY KEY |
| username | VARCHAR(255) | NOT NULL |

## How to Run

- Execute the following command : `python flask_app.py` 
- Start you browser at the following URL : `http://localhost:5000`

## Contributions

Feel free to submit changes and issues on this github repository
