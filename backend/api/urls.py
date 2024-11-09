from django.urls import path
# from .views import PostList, PostDetail
from .views import InstitutionList, InstitutionDetail
from django.views.generic import TemplateView


app_name = 'api'

urlpatterns = [
        # this view accepts a primary key 
        path('<int:pk>/', InstitutionDetail.as_view(), name='detailcreate'),
        path('', InstitutionList.as_view(), name='listcreate'),
        # path('', TemplateView.as_view(template_name="assist/index.html"))
        ]
