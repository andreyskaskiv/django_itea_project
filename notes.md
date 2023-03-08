~~~shell
$ pip install -r requirements.txt
~~~

~~~shell
$ pip freeze > requirements.txt
~~~
<a name="top"></a>
### Tutorial



1. Create blog:
   ```
   python manage.py startapp blog
   ```
   
    Registration blog:
   ```
   settings.py -> 
   
   INSTALLED_APPS = [
   ....
    # user apps
    'blog.apps.BlogConfig'
   ....
   ]
   
   ```
   
2. Create models:
   ```
   blog. models.py -> 
   Post
   ```


3. Registration models:
   ```
   blog. admin.py -> 
   PostAdmin
   ```

4. DataBase
   ```python
    python manage.py makemigrations
    python manage.py migrate
       ```


5. Create createsuperuser
   ```bash
   python manage.py createsuperuser
       ```

6. Create PostListView
   ```
   blog -> urls.py added urlpatterns
   core_project  -> urls.py  include('blog.urls', namespace='blog')
   
   added files in static and templates 
   ```


6. Create PostDetailView
   ```
   blog -> urls.py added path('<int:year>/<int:month>/<int:day>/<slug:slug>', PostDetailView.as_view(), name='post_detail')
   blog -> models.py  added  def get_absolute_url
   
   added 
   ```
   
7. Create app users
   ```python
    python manage.py startapp users
    ```
   
   Registration users:
   ```
   settings.py -> 
   
   INSTALLED_APPS = [
   ....
    # user apps
    'users.apps.UsersConfig'
   ....
   ]
   
   ```
   
8. Create UserLoginView
   ```
   user -> urls.py added urlpatterns login-logout
   core_project  -> urls.py  include('users.urls', namespace='users')
   user -> forms.py UserLoginForm

   ```
   
9. Create UserRegistrationForm
      ```
   user -> urls.py added urlpatterns register
   user -> forms.py UserRegistrationForm
   user -> views.py UserRegistrationView

   ```

10. Create ReactivationForm
   ```
   user -> urls.py added urlpatterns activate, reactivation_sent
   user -> forms.py ReactivationForm
   user -> views.py ActivateAccountView, ReactivationSentView
   user -> sending.py EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
   user -> models.py RegistrationToken

   ```





QuerySet
   https://docs.djangoproject.com/en/4.1/ref/models/querysets/

   ```pycon
   from products.models import ProductCategory
   category = ProductCategory.objects.get(id=1)
   category
   <ProductCategory: Clothes>
   ```
   
   ```pycon
   ProductCategory.objects.all()
   <QuerySet [<ProductCategory: Clothes>, <ProductCategory: New>, <ProductCategory: Shoes>, <ProductCategory: Accessories>, <ProductCategory: Present>]>
   ```
   
   ```pycon
   ProductCategory.objects.filter(description=None)
   <QuerySet []>
   ```

Fixture
   ```bash
   python manage.py dumpdata blog.Post > products/fixtures/post.json

   ```
   
   ```bash
   python manage.py loaddata products/fixtures/post.json

   ```




<a href="#top">UP</a>


