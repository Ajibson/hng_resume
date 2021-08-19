from django.urls import path
from .views import signup,edit_resume,message
urlpatterns = [
    path('', message, name = "message"),
    path('resume/', signup, name = 'resume'),
    path('edit_resume/', edit_resume, name = "edit_resume")
]
