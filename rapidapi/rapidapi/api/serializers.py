from django.contrib.auth.models import User, Group
from rest_framework import serializers

#serializrs do SQL to JSON conversion for python response
#hyperlinked relations doesn't include id field, includes clickable url field

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['urls', 'name']
