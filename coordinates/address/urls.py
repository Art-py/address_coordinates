from django.urls import path
from django.contrib.auth.decorators import user_passes_test

from . import views


app_name = 'address'


urlpatterns = [
    path('get_address/',
         user_passes_test(lambda u: u.is_superuser)(views.index_address),
         name='index_address'),
]
