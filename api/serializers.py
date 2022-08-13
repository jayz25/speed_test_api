# Response object cannot natively handle complex datatype such as django model instances, so we'll first need to serialize our data
from rest_framework import serializers
from . import models

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Paragraph
        fields = '__all__'