from django.views.generic.dates import models
from rest_framework import serializers
from assist.models import Institution

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ('id', 'code', 'prefers_2016_legacy_report', 
                  'is_community_college', 'category', 'begin_id')
