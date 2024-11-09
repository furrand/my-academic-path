from django.db import models


# Create your models here.
class AcademicYears:
    code = models.CharField(max_length=250),
    begin_date = models.DateField
    end_date = models.DateField

    def __str__(self): # pyright: ignore
        return self.code

class Institution(models.Model):

    class InstitutionObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter()

    code = models.CharField(max_length=250)
    prefers_2016_legacy_report = models.BooleanField(blank=False, default=False) # pyright: ignore
    is_community_college = models.BooleanField(blank=False, default=True) # pyright: ignore
    category = models.IntegerField(default=0) # pyright: ignore
    begin_id = models.IntegerField(default=0) # pyright: ignore
    objects = models.Manager
    institution_objects = InstitutionObjects() 

    def __str__(self): # pyright: ignore
        return self.code


class InstitutionNames(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT)
    name = models.CharField(max_length=250)
    has_departments = models.BooleanField(default=True) # pyright: ignore
    hide_in_list = models.BooleanField(default=False) # pyright: ignore

    def __str__(self): # pyright: ignore
        return self.name
