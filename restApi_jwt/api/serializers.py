from rest_framework import serializers
from api.models import Company

class CompanySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Company
        fields = "__all__"

class LoginSerializer(serializers.Serializer):
    print("serializr call")
    name = serializers.CharField()
    password = serializers.CharField()