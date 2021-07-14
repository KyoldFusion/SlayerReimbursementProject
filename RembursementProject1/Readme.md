# Slayer Reimbursement System

## Project Description

Here goes your awesome project description!

## Technologies Used

* Javascript
* HTML - HTML 5
* CSS - BootStrap
* SQL - PostgreSQL
* Python - 3.8
* Flask - 1.1.1
* Postman 

## Features

List of features ready and TODOs for future development
* Sessions to track the user who is logged in passed to the back-end.
* Clean minimal UI for users for easy navigation and appeal of website aesthetic.
* Statistics for managers using chart.js along with table data.

To-do list:
* Create pop up registration box for new users and password reset potentially
* Create further restrictions on users changing reimburement with double confirmation pop-up.

## Getting Started

(Clone link for Repo project to be dropped in git bash http)   
git clone https://gitlab.com/RyanTyler/finalp1.git

(Clone link for Repo project to be dropped in git bash SSH)  
git clone git@gitlab.com:RyanTyler/finalp1.git


- Required Tools/Services to begin working on the project via google

Git: We'll be using Git as a version control tool during the course of this program. Not only will you use Git to track changes to your projects, but you'll also use it to collaborate with your trainer and with your fellow associates.

Link: https://git-scm.com/downloads

PostgreSQL 10 (Optional): PostgreSQL is an open source relational database. We will leverage this technology in order to persist and organize data. Though you are expected to use AWS' Relational Database Service to host your database for projects in their production environments, you are welcome to download Postgres to your local host while working with your application in a development environment.

Once your database is setup using localhost create your tables using

```
CREATE TABLE valorant_employees (
	employee_id bigserial PRIMARY KEY,
	first_name varchar  not null,
	last_name varchar  not null,
	tiers varchar not null,
	employee_password varchar  not null,
	employee_username varchar  not null unique,
	email varchar  not null
)

CREATE TABLE valorant_reinbursements(
	reimbursement_id bigserial,
	agent_id int,
	economy money not null,
	purpose varchar not null,
	transaction_time date not null,
	status varchar DEFAULT 'pending',
	manager_id int,
	primary key (reimbursement_id),
	foreign key (agent_id)
	REFERENCES valorant_employees(employee_id)
)
```

Link: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

Python: We will be using Python 3 as one of our primary languages for the duration of the program. This Python installation will provide the standard library, preferred installer program, and several other components that make building and running Python applications possible.

Link: https://www.python.org/downloads/

PostgreSQL ODBC Driver: When building Python applications, we will utilize pyodbc, a PyPI module that makes accessing ODBC databases easy. As such, you'll need to download and configure a Postgres-specific ODBC driver.

Link: https://www.postgresql.org/ftp/odbc/versions/

PyCharm: We will be using PyCharm as our integrated development environment for Python. Again, an IDE is not required, but it is useful for rapid development.

Link: https://www.jetbrains.com/pycharm/


## System variable notes
If you are using System environment variables the following link is how to set up your variables for access in the code after downloading 			drivers: https://www.youtube.com/watch?v=bEroNNzqlF4

System variables used:
	db_url
	db_username
	db_password
	db_name
	
## Usage

> Here, you instruct other people on how to use your project after they’ve installed it. This would also be a good place to include screenshots of your project in action.


## License

This project uses the following license: [MIT license](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt).
