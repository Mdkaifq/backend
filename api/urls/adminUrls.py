from django.urls import path
from ..views import *

urlpatterns = [

    path('assignments/', getAssignments ),
    path('register/', registerAsAdmin ),
    path('login/', login ),
    path('assignments/<int:pk>/accept/', acceptAssignment ),
    path('assignments/<int:pk>/reject/', rejectAssignment ),

]
