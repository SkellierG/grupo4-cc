# INFO

![EVENTO](EVENTO.md)

# Caracteristicas
## Arquitectura:
REST API http protocol
**Backend: **Python fastapi
**Frontend: ** Static web

## Comandos
### Host Backend
#### Python
```bash
pip install uvicorn
```

```bash
cd ./backend
```

```bash
uvicorn main:app --host localhost --port 8000
```

### Host Frontent
#### Python
version: 3.x
```bash
cd ./frontend
```

```bash
python -m http.server -p HTTP/1.1 8080 --bind localhost
```

#### NPM
node package manager
```bash
npm install -g http-server
```

```bash
cd ./frontend
```

```bash
http-server -a localhost -p 8080
```

# Frontend

![FRONTEND](FRONTEND.md)

# Backend

![BACKEND](BACKEND.md)