# EndPoints
- http://localhost:8000/
	- GET
	- Root Directory (nothing)

- /adivinar
	- POST
	- req:
		```http
		POST http://localhost:8000/adivinar HTTP/1.1
		Content-Type: application/json
		
		{
		    "numero": 50
		}
		```
	- res:
		```http
		content-type:application/json
		{
			numberfinded: false
			attempts: 2
			feedback: "the number is lower"
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