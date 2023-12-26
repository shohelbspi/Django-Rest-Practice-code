from rest_framework import serializers
from api.models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    student_id = serializers.IntegerField()
    dep = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.student_id = validated_data.get('student_id',instance.student_id)
        instance.dep = validated_data.get('dep',instance.dep)

        instance.save()
        return instance