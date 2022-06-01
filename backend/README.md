# Backend

FastAPI

To create the virtual environment:
```
python -m venv venv
```

To activate the vm:
```
source venv/bin/activate
```

To deactivate the vm:
```
deactivate
```

To install the libraries:
```
pip install -r requirements.txt
```

To run the server:
```
uvicorn api.main:app --reload
```

### Alembic
To create the migration:
```
alembic revision --autogenerate -m "Message"
```

To run the migration:
```
alembic upgrade head
```