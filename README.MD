## PUT, POST, and DELETE method match 'symbol' in coin database with 'symbol' in coincap api (execute in terminal)
## GET method match 'symbol' in coin database with 'symbol' in coincap api via flask app (execute when app is deployed)
## log out existing account 
Since HTTPBasicAuth() does not provide log out option, user has to mannually log off by typing "http://logoff@instance_external_ip:80/<current_symbol>" (For example, user query bitcoin, the current_symbol would be 'BTC'). In the scenario where user would like to reload current session, they have to press 'cancel' and restart the session "http://instance_external_ip:80/<current_symbol>". 

## serving app over HTTP in vm instance (__pycache__ not delete, co-exist with main.py, coin_dbase.py, coin_data)
1. Change host='0,0,0,0' and port=80 and remove debug parameter in app.run() in main.py 
2. Run "sudo python3 main.py" in terminal

----------------------------------------------------------------------------------------------------------
# DEVELOPMENT
## Post
### Entry created 201
 curl -i -H "Content-Type: application/json" -X POST -d '{"id":"balancer","symbol":"BAL"}' http://35.246.10.68:5000/add

### Bad request 400
curl -i -H "Content-Type: application/json" -X POST -d '{"id":balancer"","symbol":"BAL"}' http://35.246.10.68:5000/add

## DELETE
### Not found 
curl -X DELETE http://35.246.10.68:5000/delete/SUSHI

### Delete successfully 200
curl -X DELETE http://35.246.10.68:5000/delete/BAL

## PUT
### entry created if entry does not exist or updated if entry exists 201
curl -i -H "Content-Type: application/json" -X PUT -d '{"id":"sushiswap","symbol":"SUSHI"}' http://35.246.10.68:5000/update

------------------------------------------------------------------------------------------------------------


# DEPLOYMENT
## DELETE (coins database)
curl -u jay:Cf2sdf5qM -i -H "Content-Type: application/json" -X DELETE http://34.142.63.184:80/delete/SUSHI

RESPONSE:
-------------------------------------------------------------
HTTP/1.0 401 UNAUTHORIZED
Content-Type: application/json
Content-Length: 37
WWW-Authenticate: Basic realm="Authentication Required"
Server: Werkzeug/2.0.3 Python/3.6.9
Date: Tue, 13 Dec 2022 22:27:55 GMT

{
  "error": "Unauthorized access"
}
--------------------------------------------------------------

curl -u justin:fcc215qM -i -H "Content-Type: application/json" -X DELETE http://34.142.63.184:80/delete/BTC

RESPONSE:
-------------------------------------------------------------
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 31
Server: Werkzeug/2.0.3 Python/3.6.9
Date: Tue, 13 Dec 2022 22:28:14 GMT

{
  "success": "Deleted BTC"
}
--------------------------------------------------------------

curl -u ec22339@qmul.ac.uk:yhc239qM -i -H "Content-Type: application/json" -X DELETE http://34.142.63.184:80/delete/ETH

RESPONSE:
-------------------------------------------------------------
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 31
Server: Werkzeug/2.0.3 Python/3.6.9
Date: Tue, 13 Dec 2022 22:30:01 GMT

{
  "success": "Deleted ETH"
}
--------------------------------------------------------------

## POST (coins database)
curl -u jay:Cf2sdf5qm -i -H "Content-Type: application/json" -X POST -d '{"id":"sushiswap","symbol":"SUSHI"}' http://34.142.63.184:80/add

RESPONSE:
-------------------------------------------------------------
HTTP/1.0 401 UNAUTHORIZED
Content-Type: application/json
Content-Length: 37
WWW-Authenticate: Basic realm="Authentication Required"
Server: Werkzeug/2.0.3 Python/3.6.9
Date: Tue, 13 Dec 2022 22:31:01 GMT

{
  "error": "Unauthorized access"
}
--------------------------------------------------------------

curl -u justin:fcc215qM -i -H "Content-Type: application/json" -X POST -d '{"id":"bitcoin","symbol":"BTC"}' http://34.142.63.184:80/add

RESPONSE:
-------------------------------------------------------------
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 41
Server: Werkzeug/2.0.3 Python/3.6.9
Date: Tue, 13 Dec 2022 15:53:07 GMT

{
  "message": "new currency created."
}
--------------------------------------------------------------

curl -u ec22339@qmul.ac.uk:yhc239qM -i -H "Content-Type: application/json" -X POST -d '{"id":"'ethereum'","symbol":"ETH"}' http://34.142.63.184:80/add

RESPONSE:
-------------------------------------------------------------
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 41
Server: Werkzeug/2.0.3 Python/3.6.9
Date: Tue, 13 Dec 2022 15:54:15 GMT

{
  "message": "new currency created."
}
--------------------------------------------------------------

## PUT (coins database)
curl -u jay:Cf2sdf5qm -i -H "Content-Type: application/json" -X PUT -d '{"id":"sushisw","symbol":"SUSHI"}' http://34.142.63.184:80/update

RESPONSE:
-------------------------------------------------------------
HHTTP/1.0 401 UNAUTHORIZED
Content-Type: application/json
Content-Length: 37
WWW-Authenticate: Basic realm="Authentication Required"
Server: Werkzeug/2.0.3 Python/3.6.9
Date: Tue, 13 Dec 2022 15:18:25 GMT

{
  "error": "Unauthorized access"
}
--------------------------------------------------------------

### modify entry (id 'bitcoin' > id 'bin')
curl -u justin:fcc215qM -i -H "Content-Type: application/json" -X PUT -d '{"id":"bin","symbol":"BTC"}' http://34.142.63.184:80/update

RESPONSE:
-------------------------------------------------------------
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 41
Server: Werkzeug/2.0.3 Python/3.6.9
Date: Tue, 13 Dec 2022 22:43:30 GMT

{
  "success": "Modified name for BTC"
}
--------------------------------------------------------------

### create new entry (new id, new symbol)
curl -u justin:fcc215qM -i -H "Content-Type: application/json" -X PUT -d '{"id":"bin","symbol":"BT"}' http://34.142.63.184:80/update

RESPONSE:
-------------------------------------------------------------
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 45
Server: Werkzeug/2.0.3 Python/3.6.9
Date: Tue, 13 Dec 2022 22:45:55 GMT

{
  "success": "Created new record for BT"
}
--------------------------------------------------------------

### create new entry (existing id, new symbol)
curl -u justin:fcc215qM -i -H "Content-Type: application/json" -X PUT -d '{"id":"bitcoin","symbol":"BC"}' http://34.142.63.184:80/update

RESPONSE:
-------------------------------------------------------------
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 45
Server: Werkzeug/2.0.3 Python/3.6.9
Date: Tue, 13 Dec 2022 22:46:07 GMT

{
  "success": "Created new record for BC"
}
--------------------------------------------------------------

### modify entry (id 'ethereum' > id 'ethe')
curl -u ec22339@qmul.ac.uk:yhc239qM -i -H "Content-Type: application/json" -X PUT -d '{"id":"ethe","symbol":"ETH"}' http://34.142.63.184:80/update

RESPONSE:
-------------------------------------------------------------
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 41
Server: Werkzeug/2.0.3 Python/3.6.9
Date: Tue, 13 Dec 2022 22:47:22 GMT

{
  "success": "Modified name for ETH"
}
--------------------------------------------------------------

### create new entry (new id, new symbol)
curl -u ec22339@qmul.ac.uk:yhc239qM -i -H "Content-Type: application/json" -X PUT -d '{"id":"ethe","symbol":"EH"}' http://34.142.63.184:80/update

RESPONSE:
-------------------------------------------------------------
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 45
Server: Werkzeug/2.0.3 Python/3.6.9
Date: Tue, 13 Dec 2022 22:50:52 GMT

{
  "success": "Created new record for EH"
}
--------------------------------------------------------------

### create new entry (existing id, new symbol)
curl -u ec22339@qmul.ac.uk:yhc239qM -i -H "Content-Type: application/json" -X PUT -d '{"id":"ethereum","symbol":"ET"}' http://34.142.63.184:80/update

RESPONSE:
-------------------------------------------------------------
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 45
Server: Werkzeug/2.0.3 Python/3.6.9
Date: Tue, 13 Dec 2022 22:51:13 GMT

{
  "success": "Created new record for ET"
}
--------------------------------------------------------------

## POST (users database)
curl -u ec22339@qmul.ac.uk:yhc239qM -i -H "Content-Type: application/json" -X POST -d '{"userID":"takana", "pw":"tg9lo2k", "role":"moderator"}' http://34.142.63.184:80/add_user

RESPONSE:
-------------------------------------------------------------
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 36
Server: Werkzeug/2.0.3 Python/3.6.9
Date: Tue, 13 Dec 2022 22:53:17 GMT

{
  "message": "new user created"
}
--------------------------------------------------------------

curl -u justin:fcc215qM -i -H "Content-Type: application/json" -X POST -d '{"userID":"tin", "pw":"fcc21df5qM", "role":"moderator"}' http://34.142.63.184:80/add_user

RESPONSE:
-------------------------------------------------------------
HTTP/1.0 401 UNAUTHORIZED
Content-Type: application/json
Content-Length: 37
WWW-Authenticate: Basic realm="Authentication Required"
Server: Werkzeug/2.0.3 Python/3.6.9
Date: Tue, 13 Dec 2022 22:53:24 GMT

{
  "error": "Unauthorized access"
}
--------------------------------------------------------------

curl -u jay:Cf2sdf5qM -i -H "Content-Type: application/json" -X POST -d '{"userID":"tin", "pw":"fcc21df5qM", "role":"moderator"}' http://34.142.63.184:80/add_user

RESPONSE:
-------------------------------------------------------------
HTTP/1.0 401 UNAUTHORIZED
Content-Type: application/json
Content-Length: 37
WWW-Authenticate: Basic realm="Authentication Required"
Server: Werkzeug/2.0.3 Python/3.6.9
Date: Tue, 13 Dec 2022 22:52:05 GMT

{
  "error": "Unauthorized access"
}
--------------------------------------------------------------