## Overview 
This is python django hackathon project that outputs a list of developer advocates with their details such as where they work, social links, bio, etc.

## Project Requirements
Your API should at a minumum have these 4 endpoints

```
/advocates
/advocates/:id
/companies
/companies/:id
```
Your API should be searchable (By user name), paginated.

## Installation & Usage
You can simply clone  ``django-developer-advocate-api
`` like below on your git bash

```bash
git clone https://github.com/ayangzy/django-developer-advocate-api.git
```
After cloning the project, Create your own virtual environment
```
python3 -m venv venv
```

Activate your virtual environment
<br>
For mac Os users
```
source venv/bin/activate
```

For windows users
```
venv\Scripts\activate.bat 
```

Install your requirements if you can't find it in the project file
```
pip install -r requirements.txt
```

Set up PostgreSQL database or you can leave the default DB sqlite 

Next  cd into the project directory

```
cd advocateapi
```

Finally serve your application
```
python manage.py runserver
```

You application should be live on 
```
http://127.0.0.1:8000/
```

Here is the available endpoint per the project requirments if you are using local development server

Advocates endpoints
```
http://127.0.0.1:8000/api/advocates/

http://127.0.0.1:8000/api/advocates/1

http://127.0.0.1:8000/api/advocates/?search=felix&page=2&limit=10

```


Company endpoints
```
http://127.0.0.1:8000/api/companies/

http://127.0.0.1:8000/api/companies/1

```

The project is also hosted on Heroku, kindly find below the endpoints

Advocates
```
https://advocateapi.herokuapp.com/api/advocates/

https://advocateapi.herokuapp.com/api/advocates/1/

https://advocateapi.herokuapp.com/api/advocates/?page=1&search=Dennis
```

companies endpoints
```
https://advocateapi.herokuapp.com/api/companies/

https://advocateapi.herokuapp.com/api/companies/2/

```



If you run into any issue, please email

```felixdecoder2020@gmail```

## Credits

- [Ayange Felix](https://github.com/ayangzy)

