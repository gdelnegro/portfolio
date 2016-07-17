from portfolio.models import *
from rest_framework import serializers


class TranslationSerializer(serializers.HyperlinkedModelSerializer):
    last_tag = serializers.SerializerMethodField()

    def get_last_tag(self, model):
        # from django.core import serializers as dj_serializer
        # import json
        return model.last_tag()

    class Meta:
        model = Translation
        fields = "__all__"

