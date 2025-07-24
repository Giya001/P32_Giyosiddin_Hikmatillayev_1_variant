from django.contrib import admin
from django.urls import path,include

from book import views

urlpatterns = [
    path('',views.home,name='home'),
    path('create/',views.createBook,name='createBook'),
    path('<int:book_id/update>',views.updateBook,name='updateBook'),
]