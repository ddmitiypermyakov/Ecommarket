

from django.urls import path
from .views import ImageS
urlpatterns = [

    path('',ImageS.as_view(),name='image')
]
