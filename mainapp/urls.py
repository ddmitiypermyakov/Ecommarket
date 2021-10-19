

from django.urls import path
from .views import ImageS
urlpatterns = [

    path('',ImageS.as_view(),name='image')
    # path('base/',ImageS.as_view(),name='image')
]
