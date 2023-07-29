from django.urls import path
from profiles import views

# remember to call .as_view() if its a class view
urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
]
