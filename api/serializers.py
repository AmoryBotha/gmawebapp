from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note
#django uses ORM (object relational mapping): 
#maps python objects to corresponding code that
#needs to be executed to make a change in DB

#code explaination: create a model(table) for our DB on django
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}