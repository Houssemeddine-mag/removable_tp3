# Django University Management System

This is a Django REST API equivalent to the Spring Boot tp2 project.

## Features

- Student and University management
- REST API endpoints
- Many-to-One relationship (Student -> University)
- Custom queries for filtering students by university

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

3. Create a superuser (optional):

```bash
python manage.py createsuperuser
```

4. Run the development server:

```bash
python manage.py runserver
```

The server will run on `http://127.0.0.1:8000/`

## API Endpoints

### University Endpoints

- `POST /university/add` - Add a new university
  ```json
  {
    "name": "MIT"
  }
  ```
- `GET /university/getAll` - Get all universities

### Student Endpoints

- `POST /student/add` - Add a new student
  ```json
  {
    "name": "John Doe",
    "address": "123 Main St",
    "university": 1
  }
  ```
- `GET /student/getAll` - Get all students
- `GET /student/getAllUniv` - Get all students with their university names
- `GET /student/findStudUniv?univName=MIT` - Find students by university name

## Comparison with Spring Boot (tp2)

| Feature          | Spring Boot       | Django                   |
| ---------------- | ----------------- | ------------------------ |
| Framework        | Spring Boot 3.5.6 | Django 5.2.7             |
| ORM              | JPA/Hibernate     | Django ORM               |
| Database         | MySQL             | SQLite (default)         |
| Port             | 8081              | 8000                     |
| REST Framework   | Spring Web        | Django REST Framework    |
| Repository Layer | JpaRepository     | Django ORM QuerySets     |
| Service Layer    | @Service classes  | Views (can add services) |
| Controller Layer | @RestController   | @api_view decorators     |

## Equivalent Mappings

### Spring Boot -> Django

- `@Entity` -> `models.Model`
- `@Repository` -> QuerySets (built-in)
- `@Service` -> Business logic in views (or separate services)
- `@RestController` -> `@api_view` decorated functions
- `JpaRepository.findAll()` -> `Model.objects.all()`
- `JpaRepository.save()` -> `Model.save()` or `serializer.save()`
- `@Query` -> `Model.objects.filter()` or `select_related()`
