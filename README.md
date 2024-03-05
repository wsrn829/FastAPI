### This is a brand new FastAPI CRUD application that uses a PostgreSQL database for me to practice FastAPI.

- Being a "minimal" web-framework, FastAPI doesn't have built-in authentication, a database ORM, templating, or HTML form handling like Django.
- However, it has different features that make it very pleasant to work with and you can bolt on all those other features that Django has if you really need them.


- routers(goes to the database): add more endpoints
- queries(FastAPI endpoints): write sql to interact with databases
(We separate folders instead of putting all endpoints inside main.py just for good code organization)

Putting pydantic models in queries is an easier way.

### pydantic models vs Djangdo models

Pydantic Models:

- Pydantic is a data validation library that uses Python type annotations. Pydantic models (or schemas) are classes where each attribute is a field with an optional type annotation. They are primarily used for data validation, serialization, and deserialization. Pydantic is often used with FastAPI or other Python-based web frameworks.
- Pydantic models are not tied to databases. They are used for input validation and data serialization/deserialization.
- Pydantic models use Python type annotations for validation.
- Pydantic models can be nested, allowing complex hierarchical data structures.
- Pydantic models are not ORM (Object-Relational Mapping) models, so they don't have methods for database operations.

Django Models:

- Django models are a part of Django's ORM. They serve as the single, definitive source of information about your data. Each attribute represents a database field.
- Django models are tied to databases. They define the structure of the database tables and provide methods to query the database.
- Django models use fields (like CharField, IntegerField, etc.) to define the type of data each attribute can hold.
- Django models can have relationships with other models (like foreign keys for one-to-many relationships, many-to-many fields, etc.).
- Django models come with a built-in admin interface for CRUD operations.

Similarities:

- Both Pydantic and Django models use classes to define data structures.
- Both can use type information to perform data validation.
- Both can be used to define and validate complex data structures.

Differences:

- Django models are tied to a database and provide ORM capabilities, while Pydantic models are not tied to a database.
- Django models are used with Django, while Pydantic models can be used with any Python code, but are often used with FastAPI.
- Pydantic uses Python type annotations for validation, while Django uses specific field types.
- Django models come with a built-in admin interface, while Pydantic does not.
