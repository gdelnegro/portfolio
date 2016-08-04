from portfolio.models import *
from rest_framework import serializers


class TranslationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslationType
        fields = ('tag', 'has_auxiliary_text', 'auxiliary_tag',)


class TranslationSerializer(serializers.ModelSerializer):
    type = TranslationTypeSerializer()

    class Meta:
        model = Translation
        fields = "__all__"