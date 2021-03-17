from rest_framework import serializers
# from .models import Fbooks
from .models import DirectorInfo, WriterInfo

class DirectorInfoSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = DirectorInfo
        fields = "__all__"

class WriterInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WriterInfo
        fields = "__all__"
