# Trading System (Technical Exam)
Pure REST API for simple trading system. User can buy stocks and make orders.

features:
- Token Authentication (Include in request header Authorization Ex. Bearer < Token >)
- Stock CRUD operation
- Order CRUD operation

Endpoints:
- "/api-auth/" POST (login)
- "/api/users/" GET, POST (Register)
- "/api/users/:id/" GET, PUT, DELETE
- "/api/stocks/" GET, POST
- "/api/stocks/:id/" GET, PUT, DELETE
- "/api/orders/" GET, POST
- "/api/orders/:id/" GET, PUT, DELETE
- "/api/portfolio/" GET

## Run in local
Recommended to have virtual environment active

- Install dependencies
`pip install -r requirements.txt`

- Run
`python manage.py runserver`