from assist.models import AcademicYear, Institution, InstitutionName
from rest_framework import serializers


class AcademicYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicYear
        fields = ("id", "fall_year")


class InstitutionNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutionName
        fields = ["name", "has_departments", "hide_in_list"]


class InstitutionSerializer(serializers.ModelSerializer):
    names = InstitutionNameSerializer(many=True)

    class Meta:
        model = Institution
        fields = (
            "id",
            "names",
            "code",
            "prefers_2016_legacy_report",
            "is_community_college",
            "category",
            "begin_id",
        )
