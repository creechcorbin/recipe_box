"""recipe_box URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from homepage import views

urlpatterns = [
    path('', views.recipe_list, name="homepage"),
    path('recipe/<int:recipe_id>/edit/', views.edit_recipe_view),
    path('recipe/<int:recipe_id>/', views.recipe_detail),
    path('newrecipe/', views.recipe_form, name="newrecipe"),
    path('newauthor/', views.author_form),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('signup/', views.signup_view),
    path('admin/', admin.site.urls),
    path('<str:author_name>/', views.author_detail),
    path('favorite/<int:recipe_id>/', views.add_favorite_view),
]
