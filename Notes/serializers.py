from rest_framework import serializers
from .models import Group, Note


class GroupSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Group
        fields = "__all__"
        
class NoteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Note
        fields = "__all__"