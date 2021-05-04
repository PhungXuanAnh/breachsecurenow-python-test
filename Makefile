run:
	cd app && python main.py

create-customer:
	curl -X POST http://127.0.0.1:8001/api/v1/customers \
		-H "Content-Type: application/json" \
		-d "{ \"name\": \"Alexander2\", \"email\": \"test2@gmail.com\"}"

get-customer:
	curl http://127.0.0.1:8001/api/v1/customers/1 


update-customer:
	curl -X PUT http://127.0.0.1:8001/api/v1/customers/1 \
		-H "Content-Type: application/json" \
		-d "{ \"name\": \"Alexander22\", \"email\": \"test22@gmail.com\"}"

delete-customer:
	curl -X DELETE http://127.0.0.1:8001/api/v1/customers/1

mysql-up:
	docker run -d --name test-mysql \
		-p 3306:3306 \
		-e MYSQL_ROOT_PASSWORD=passwd \
		-e MYSQL_USER=user \
		-e MYSQL_PASSWORD=passwd \
		-e MYSQL_DATABASE=db \
		mysql:5.7 \
		--character-set-server=utf8 \
		--collation-server=utf8_unicode_ci

mysql-down:
	docker rm -f test-mysql