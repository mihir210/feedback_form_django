
from django.contrib import admin
from django.urls import path
from home import views


admin.site.site_header = "Mihir Admin"
admin.site.site_title = "feedback portal"
admin.site.index_title = "Welcome to admin panel"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

]