# feedback_form_django

# for save details

you need to add this code in django app in models.py file
   ```shell
   class Contact(models.Model):
   name = models.CharField(max_length=122)
   email =models.CharField(max_length=120)
   department = models.CharField(max_length=20)
   roll_no = models.CharField(max_length=20)
   feedback_text = models.TextField()
   date = models.DateField()

   def __str__(self):
      return self.name
   ```
   

# host name

you need to add host name in settings.py file

   ```shell
   ALLOWED_HOSTS = ['*']
   
   STATICFILES_DIRS = [
    BASE_DIR / "static",
    # '/var/www/static/',
   ]
   
   STATIC_ROOT = 'staticfiles'
   STATIC_URL = '/static/'
   
   INSTALLED_APPS = [
    'home.apps.HomeConfig',
   ]
   ```
   
# for deploy app

for deploy in heroku you must change in wsgi.py file

you need to install dj_static module for deploy app
   
   ```shell
   pip install dj_static
   ```
   
   
after install add this code to wsgi.py file
   
   ```shell
   from dj_static import Cling
   application = Cling(get_wsgi_application())
   ```
   
   
   
after this you need to install one more module name gunicorn
   
   
   ```shell
   pip install gunicorn
   ```



after install gunicorn make one file name .Procfile and add this code
   ```shell
   web: gunicorn app_name.wsgi --log-file -
   ```
   
note : app_name is your app name in django app



# Run django-app

   ```shell
   cd app-name
   ```
   ```shell
   python manage.py runserver
   ```
   
   
  # for deploy app in heroku
  
  Install the Heroku CLI
   Download and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.
   ```shell
   $ heroku login
   ```
   
   Create a new Git repository
   Initialize a git repository in a new or existing directory
   ```shell
   $ cd my-project/
   $ git init
   $ heroku git:remote -a asx1w223
   ```
   
Deploy your application
Commit your code to the repository and deploy it to Heroku using Git.
   ```shell
   $ git add .
   $ git commit -am "make it better"
   $ git push heroku master
   ```
