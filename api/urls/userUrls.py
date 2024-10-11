from django.contrib import admin
from django.urls import path
from ..views import *

urlpatterns = [

    path('register/', registerAsUser ),
    path('login/', login ),
    path('upload/', submitAssignment ),
    path('admins/', getAdmins ),


]
