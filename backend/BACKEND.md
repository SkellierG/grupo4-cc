# EndPoints
- http://localhost:8000/
	- GET
	- Root Directory (nothing)

- /adivinar
	- POST
	- req:
		```http
		content-type:application/json
		{
			numero: int
		}
		```
	- res:
		```http
		content-type:application/json
		{
			numberfinded: boolean
			attempts: int
			feedback: string
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