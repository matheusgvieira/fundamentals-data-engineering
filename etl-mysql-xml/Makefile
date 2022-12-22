MYSQL_USER=root
MYSQL_PASSWORD=MySql2019!
MYSQL_SERVER=mysqlsrv
MYSQL_DATABASE=testedb
MYSQL_PORT=3306

export MYSQL_USER MYSQL_PASSWORD MYSQL_SERVER MYSQL_DATABASE MYSQL_PORT

prettier:
	black *.py
	isort *.py

check:
	black *.py
	flake8 *.py
	pylint *.py
	isort *.py
	mypy *.py
	