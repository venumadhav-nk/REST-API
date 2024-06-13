from django.urls import path
from.import views

urlpatterns = [
    path('welcome/',views.welcome),
    path('get/',views.getemployee),
    path('add/',views.addEmployee),
    path('put/',views.putemployee),
    path('patch/',views.patchemployee),
    path('delete/',views.delemployee),


]
