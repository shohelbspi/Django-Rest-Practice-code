from rest_framework import serializers

class StudentSerializers(serializers.Serializer):
    roll = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    dep = serializers.CharField(max_length=100)
