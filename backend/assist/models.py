from django.db import models


# Create your models here.
class AcademicYear(models.Model):

    class AcademicYearObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter()

    fall_year = models.IntegerField(default=0)
    objects = models.Manager()
    academic_year_objects = AcademicYearObjects()

    def __str__(self):  # pyright: ignore
        return self.fall_year


class Institution(models.Model):

    class InstitutionObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter()

    code = models.CharField(max_length=250)
    prefers_2016_legacy_report = models.BooleanField(blank=False, default=False)
    is_community_college = models.BooleanField(blank=False, default=True)
    category = models.IntegerField(default=0)
    begin_id = models.IntegerField(default=0)
    objects = models.Manager()
    institution_objects = InstitutionObjects()

    def __str__(self):
        return self.code


class InstitutionName(models.Model):
    institution = models.ForeignKey(
        Institution, related_name="names", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=250)
    alternate_institution = models.ForeignKey(
        Institution, on_delete=models.CASCADE, null=True
    )
    from_year = models.IntegerField(null=True)
    has_departments = models.BooleanField(default=True)
    hide_in_list = models.BooleanField(default=False)

    def __str__(self):
        return self.name
