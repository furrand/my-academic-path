from django.urls import path
from django.views.generic import TemplateView

app_name = "assist"

urlpatterns = [
    path("", TemplateView.as_view(template_name="assist/index.html")),
]
