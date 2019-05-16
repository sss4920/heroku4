from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.layout, name='layout'),
    path('blog/home/', blog.views.home, name='home'),
    path('blog/newblog/', blog.views.blogform, name='newblog'),
    path('blog/create/', blog.views.create, name='create'),
    path('blog/<int:pk>/edit/', blog.views.edit, name='edit'),
    path('blog/<int:pk>/remove/', blog.views.remove, name='remove'),
]