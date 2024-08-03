# Fetch
/adivinar
POST
```javascript
const response = await fetch('http://localhost:8000/adivinar', {
	method: 'POST',
	headers: {
		'Content-Type': 'application/json',
	},
	body: JSON.stringify(data),
});
```
data:
```JSON
{
	"numero": 123
}
```