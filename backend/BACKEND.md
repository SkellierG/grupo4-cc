# EndPoints
## http://localhost:8000/
GET
Root Directory (nothing)

## /adivinar
POST
### req:
```http
POST /adivinar HTTP/1.1
Host: localhost:8080
Content-Type: application/json

{
	"numero": 50
}
```

### res:
```http
HTTP/1.1 200 OK
content-type: application/json
Content-Length: 67

{
	"numberfinded": false,
	"attempts": 2,
	"feedback": "the number is lower"
}
```
## /check and /retry
POST
### res:
```http
HTTP/1.1 200 OK
content-type: application/json
Content-Length: 67

{
	"ok": true,
}
```

# CORS
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```
