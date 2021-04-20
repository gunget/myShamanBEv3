from rest_framework import serializers
# from .models import Fbooks
from .models import DirectorInfo, FicWriterInfo, NonFicWriterInfo, OthersInfo
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    directorInfo = serializers.PrimaryKeyRelatedField(many=True, queryset=DirectorInfo.objects.all())
    ficWriterInfo = serializers.PrimaryKeyRelatedField(many=True, queryset=FicWriterInfo.objects.all())
    nonFicWriterInfo = serializers.PrimaryKeyRelatedField(many=True, queryset=NonFicWriterInfo.objects.all())
    othersInfo = serializers.PrimaryKeyRelatedField(many=True, queryset=OthersInfo.objects.all())

    class Meta:
        model = User
        fields = "__all__"

class DirectorInfoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = DirectorInfo
        fields = "__all__"

class FicWriterInfoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = FicWriterInfo
        fields = "__all__"

class NonFicWriterInfoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = NonFicWriterInfo
        fields = "__all__"

class OthersInfoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = OthersInfo
        fields = "__all__"
