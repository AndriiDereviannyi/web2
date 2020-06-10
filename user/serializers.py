from rest_framework import serializers

from user.models import User

class Userserializer(serializers.ModelSerializers):
    class Meta:
        model = User
        fields = "__all__"