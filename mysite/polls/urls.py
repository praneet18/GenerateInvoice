from django.urls import path

from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("index", views.index, name="index"),
    path('autocomplete', views.autocomplete, name='autocomplete'),
    path("generateinvoice", views.generateinvoice, name="generateinvoice"),
    path('upload-csv/', views.profile_upload, name="profile_upload"),
    # path("login", views.login),
]
