
## Prerequisites
1. Install Python
2. Install Django
3. Install Pycharm (Community version. Ignore Professional version)

## Creating python django web app
**Step 1:** Creating new project in the root directory such as, `C:\Users\samue\PyCharmProjects\my_python_project`. Make sure `venv` is selected as the environment and
check the boxes `Inherit global site packages`, `Make available to all projects` and choose `Create`. A new python project will be created.

**Step 2: Install django using terminal**
Open the terminal in PyCharm and while we are inside the `venv` directory, `(venv) PS C:\Users\samue\PyCharmProjects\my_python_project>`, use `pip install django`
to install django.

**Step 3: Create a django project (Using django admin command)**
Create a project named, `mydjangosite`, using the command:

```
django-admin startproject mydjangosite
```

Go to the file explorer and locate the folder, `mydjangosite`.

**Step 4: Change directory to `mydjangosite`**

```
 cd mydjangosite
```

**Step 5: Create an app inside django project**

Create an app named `myapp` inside the project:

```
django-admin startapp myapp
```

The app has many files such as admin, apps, models, tests, views

**Step 6: Add app to settings.py**

Add your app, `myapp` to the installed apps section of settings.py:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp'
]
```

**Step 7: Run the server**
Run the server using the following commands, to test if everything is running fine:

```
python manage.py runserver
```

The django setup is completed. Now we can create and run some webpages to start the website development.

**Step 8: Migrate**
Migrate is done for the databases

```
python manage.py migrate
```

**Step 9: Create Superuser**
To access the admin section, create Superuser. While creating Supercase, you will have to provide three inputs, username, password, and email address.

```
python manage.py createsuperuser
Username: samuel
email address: samuel7.ag.gis@gmail.com
password: Samuelds@7797
```

**Step 10: Check admin credentials by logging into admin**
First run the server using, `python manage.py runserver`

Change the url to, `http://127.0.0.1:8000/admin`

**Step 11: Create directory named templates in app**
Close the server using `Ctrl + C`. Go to `myapp` --> `New` --> `Directory` --> `templates`.

**Step 12: Inside template directory create another directory with same name as app**
Go to `templates` --> `New` --> `Directory` --> `myapp`

**Step 13: Create index.html in the myapp directory**
Create an html file in the directory and add a `h1` tag between the `<body>` tag:

```
<h1>My first python django app</h1>
```

**Step 14: In views.py define index view for index.html**

Views for index.html is defined as:
```
def index(request):
    render(request)
```

**Step 15: Copy urls.py from django project to your app**
Copy the urls.py from the `mydjangosite` folder to the `myapp` folder

**Step 16: In your app inside urls.py create url pattern for index veiw**
First import views from the current directory

```
from . import views
```

Now create a pattern for index view:

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index')
]

```

**Step 17: Create url pattern in django project inside urls.py**

Go to the `urls.py` file in the `mydjangosite` folder. Here you have to import all the urls that you created in the `myapp` url path.

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('myapp.urls'))
    path('admin/', admin.site.urls),
]
```

**Step 18: Run the server**

Run the server as:
```
python manage.py runserver
```

The app that we created:
![django](https://github.com/samueldsingh/python-dev-90-days-bootcamp/assets/62851341/3b7ddcaf-edd3-4d11-bf1d-0916219c7fd2)


[Youtube Tutorial](https://youtu.be/4XYsODaQ6Ok)
