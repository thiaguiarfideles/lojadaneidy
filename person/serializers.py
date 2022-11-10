from rest_framework import serializers
from person.models import Person
from usuarios.models import User

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = (["id","address","user"])