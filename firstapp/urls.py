from django.urls import path
from .views import * 

urlpatterns = [
    path('', MainStartPage.as_view()),
]