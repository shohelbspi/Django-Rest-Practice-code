from rest_framework import serializers
from api.models import Student

class StudentSerializer(serializers.Serializer):
    roll = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    dep  = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
