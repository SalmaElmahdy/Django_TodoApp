from django.urls import path

from todo import views
urlpatterns = [
    path('add/',views.add,name='add'),
]