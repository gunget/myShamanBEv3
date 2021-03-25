from rest_framework import serializers
# from .models import Fbooks
from .models import DirectorInfo, FicWriterInfo, NonFicWriterInfo

class DirectorInfoSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = DirectorInfo
        fields = "__all__"

class FicWriterInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FicWriterInfo
        fields = "__all__"

class NonFicWriterInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonFicWriterInfo
        fields = "__all__"
