# Python 2to3 API

> Keep it simple, stupid

Simple Flask API for converting Python 2 scripts to Python 3 using lib2to3.

## Usage

1. Build and run the Docker image:

   `docker build -t python-2to3-api .`

   `docker run -p 5000:5000 python-2to3-api`

3. Send a POST request to `http://localhost:5000/convert` containing the Python script to be converted.

   Example using curl:

   ```bash
   curl http://localhost:5000/convert -H "Content-Type: text/plain" -d 'print "Be careful not to fall off!"'
   ```

## Response

The API responds with status 200 and the converted script.

```python
print("Be careful not to fall off!")
```

If there's something wrong it'll return status 500 with an error

```
bad input: type=1, value='x', context=('', (1, 35))
```

Additionally there is a health check endpoint at `/health` which returns "OK" as the body and status 200
