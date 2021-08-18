from django.urls import path
from .views import signup,edit_resume
urlpatterns = [
    path('signup/', signup, name = "signup"),
    path('edit_resume/', edit_resume, name = "edit_resume")
]
