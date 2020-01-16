from django.urls import path

from . import views

urlpatterns = [
  path('<slug:fosdemtag>/', views.fosdem_tag_to_id, name='fosdemtagtoid'),
]
