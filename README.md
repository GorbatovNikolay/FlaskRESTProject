# Flask REST API

___

### Contents

1. Description
2. Setting up
3. Usage

---

### Description

This application offers an interface to work with the database of the educational platform. The API provides the
following features:

1. Add new students;
2. Remove students;
3. Get groups by number of students;
4. Assign students to courses;
5. Remove students from a course;
6. Get all students in the course;

The application is written in Python using the Flask framework with the Flask-RESTful extension. Also, the SQLAlchemy
library is used to work with the database, which is by default the Postgresql database.


---

### Setting up

1. Download the project repository.
2. Install python 3.8 or newer.  
   <small>[Python installation guide][python-link]</small>

[python-link]: https://wiki.python.org/moin/BeginnersGuide/Download

3. Install required packages from "requirements.txt" file:  
   Just run the following command:
    ``` 
    pip install -r requirements.txt
    ```
4. Install PostgreSQL server.  
   <small>[PostgreSQl installation guide][postgresql-link]</small>

[postgresql-link]: https://www.postgresql.org/docs/current/tutorial-install.html

5. Open *rest_api_app/database/processors/consts/connection_consts.py*  
   Change *CONNECTION_STR* object according to your settings.

```python 
CONNECTION_STR: Final = 'postgresql+psycopg2://my_user:resuetaerc@localhost:5432/flask_rest_api'
```

**In case you want to use a different database, modify *CONNECTION_STR* as
required:** <small>[Establishing Connectivity SQLAlchemy][sqlalchemy-link]</small>

[sqlalchemy-link]: https://docs.sqlalchemy.org/en/20/tutorial/engine.html

6. Add tables to the database:
   * open Python Console and run `python`
   * import and run *create_tables* function

```python
from rest_api_app.database.db_creation import create_tables

create_tables()
```

7. If you wish, the application provides the possibility of generating the test data. Just import and run *create_db*
   function. In this case the tables are created automatically, so you can skip section 6.

```python
from rest_api_app.database.db_creation import create_db

create_db()
```

#### The API is ready to be used!

---

### Usage

1. Run the Flask server.  
   Run the following command: `python run.py`
2. The app is connected to the Swagger UI.  
   Just open *http://127.0.0.1:5000/apidocs* in your browser and test the queries:

![GroupsRoute][swagger-groups]

[swagger-groups]: https://downloader.disk.yandex.ru/preview/a9ce78a8913e9e77b915a464ea50dfbffb77dbfd269438b3f4953d7903d6138f/6258e721/UkvRzvceM4VvSEtek4rudaXIZKz1nEOoa53cbrvirpqyp4mhwccD3CzcJzXv22x4q1D4Lyu9cb3_9Z1SFIdojA%3D%3D?uid=0&filename=Swagger%20Groups.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048

3. You may also use the terminal to execute HTTP queries:  
   e.g. `curl -X GET "http://127.0.0.1:5000/api/groups/30" -H "accept: application/json"`  
   Base path: `*127.0.0.1:5000/api*`  
   Available routes:
    - add a new student:  
      `/student/{first_name}/{last_name}`
    - delete student:  
     ` /student/{student_id}`
   - remove a student from a course:  
     `/student/{student_id}/course/{course_id}`
    - get all course students:  
      `/students/{course_name}`
    - get groups with less or equal amount of students:  
      `/groups/{number_of_students}`
    - assign student to courses:  
      `/courses/student/{student_id}`  
      **NOTE:** this route also takes json data with a list of course IDs  
      Example:  
      `curl -X POST "http://127.0.0.1:5000/api/courses/student/23 -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"course_ids\": [ 1, 2, 3 ]}"`

![StudentToCourseRoute][swagger-courses]

[swagger-courses]: https://downloader.disk.yandex.ru/preview/992f07b23f0357d41b15586f9418cde10cd1022493740c766b74d21258046ee9/6258ec7a/AnHYsVYv6QP4uWRK3DsMBIbD0mjN3u1bFHWDeZ8fo-5AEWzD7MVNha1ATDINU0mw8WfTq0dr3PhKhSyxDqbUoQ%3D%3D?uid=0&filename=Swagger%20Student%20to%20Courses.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048

---
