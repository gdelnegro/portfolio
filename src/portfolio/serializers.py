from portfolio.models import *
from rest_framework import serializers


class TranslationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslationType
        fields = ('tag', 'has_tooltip', 'tooltip_tag',)


class TranslationSerializer(serializers.ModelSerializer):
    last_tag = serializers.SerializerMethodField()
    last_id = serializers.SerializerMethodField()
    type = TranslationTypeSerializer()

    def get_last_tag(self, model):
        return model.last_tag()

    def get_last_id(self, model):
        last_tag = model.last_tag()
        return last_tag[3:]

    class Meta:
        model = Translation
        fields = "__all__"