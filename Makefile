create-customer:
	curl -X POST http://127.0.0.1:8001/api/v1/customers \
		-H "Content-Type: application/json" \
		-d "{ \"name\": \"Alexander2\", \"email\": \"test2@gmail.com\"}"

get-customer:
	curl http://127.0.0.1:8001/api/v1/customers/6 


update-customer:
	curl -X PUT http://127.0.0.1:8001/api/v1/customers/6 \
		-H "Content-Type: application/json" \
		-d "{ \"name\": \"Alexander22\", \"email\": \"test22@gmail.com\"}"

delete-customer:
	curl -X DELETE http://127.0.0.1:8001/api/v1/customers/6