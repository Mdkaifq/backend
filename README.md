# backend

**refer the env.txt file for database environment variables configuration**

# how to run this project
make a virtual environment and install the repository inside it

activate you virtual environment
```bash
venv/Scripts/activate # for linux: source venv/bin/activate
```

then take a dive inside backend folder and download the used packages
```bash
pip install -r requirements.txt
```

then run the server

```bash
python manage.py runserver
```
**Note: make sure that the virtual environment is activated**

# User paths:

api/register/&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;method type: POST

api/login/&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;method type: POST

api/upload/&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;method type: POST

api/admins/&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;method type: GET


# Admin paths:

admin/register/&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;method type: POST

admin/login/&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;method type: POST

admin/assignments/&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;method type: GET

admin/assignments/:id/accept/&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;method type: POST

admin/assignments/:id/reject/&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;method type: POST


# admin panel path: 

adminpanel/
