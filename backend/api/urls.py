from django.urls import path

# from .views import PostList, PostDetail
from .views import AcademicYearList, InstitutionDetail, InstitutionList

# from django.views.generic import TemplateView


app_name = "api"

urlpatterns = [
    # this view accepts a primary key
    path("institutions/", InstitutionList.as_view(), name="listcreate"),
    path("academic-years/", AcademicYearList.as_view(), name="listcreate"),
    path("<int:pk>/", InstitutionDetail.as_view(), name="detailcreate"),
    path("", InstitutionList.as_view(), name="listcreate"),
    # path('', TemplateView.as_view(template_name="assist/index.html"))
]
