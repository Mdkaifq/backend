from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class AssignmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Assignments
        fields = ["id", "task", "status", "admin"]

class AdminSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["username" ]