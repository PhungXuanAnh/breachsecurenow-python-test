- [1. Explain source code](#1-explain-source-code)
- [2. Deploy on local](#2-deploy-on-local)
	- [2.1. Setup mysql server](#21-setup-mysql-server)
	- [2.2. Configure mysql server in source code](#22-configure-mysql-server-in-source-code)
	- [2.3. Run project](#23-run-project)
	- [2.4. Test](#24-test)
- [3. ERD diagram](#3-erd-diagram)


# 1. Explain source code

[app/main.py](app/main.py) : contain api endpoints

[app/mysql_ulities.py](app/mysql_utilities.py) : all logic related to mysql here. Because you told me do not over use libraries and do not use an ORM, so I choose `pymysql` library with raw SQL.

[app/enums.py](app/enums.py) : define types of Vehicle

[Makefile](Makefile) contain all commands for deploy and test this project

# 2. Deploy on local

## 2.1. Setup mysql server

Setup directly mysql to your computer or using docker. Here, I use docker with below configurations :

```shell
docker run -d --name test-mysql \
	-p 3306:3306 \
	-e MYSQL_ROOT_PASSWORD=passwd \
	-e MYSQL_USER=user \
	-e MYSQL_PASSWORD=passwd \
	-e MYSQL_DATABASE=db \
	mysql:5.7 \
	--character-set-server=utf8 \
	--collation-server=utf8_unicode_ci
```

## 2.2. Configure mysql server in source code

Change mysql configuration in method `create_connection()` in this file : [app/mysql_ulities.py](app/mysql_ulities.py)

## 2.3. Run project

Environment:

	ubuntu 20
	python 3.8.0


Run below command:

```shell
pip install requirements.txt
cd app
python main.py
```

## 2.4. Test

Test using curl or postman

Create customer

```shell
curl -X POST http://127.0.0.1:8001/api/v1/customers \
        -H "Content-Type: application/json" \
        -d "{ \"name\": \"Alexander2\", \"email\": \"test2@gmail.com\"}"
# output
{
  "email": "test2@gmail.com", 
  "id": 1, 
  "name": "Alexander2"
}
```

Change customer id base on output that you recieved from above command

Get customer

```shell
curl http://127.0.0.1:8001/api/v1/customers/1
# output
{
  "email": "test2@gmail.com", 
  "id": 1, 
  "name": "Alexander2"
}
```

Update customer

```shell
curl -X PUT http://127.0.0.1:8001/api/v1/customers/1 \
        -H "Content-Type: application/json" \
        -d "{ \"name\": \"Alexander22\", \"email\": \"test22@gmail.com\"}"
# output
{
  "email": "test22@gmail.com", 
  "id": 1, 
  "name": "Alexander22"
}
```

Delete customer

```shell
curl -X DELETE http://127.0.0.1:8001/api/v1/customers/1
# output
null
```

# 3. ERD diagram

![ERD.png](ERD.png)

If you don't see image, please open file [ERD.png](ERD.png) in this project.

SQL which implements above ERD is in file : [app/mysql_utilities.py](app/mysql_utilities.py)
