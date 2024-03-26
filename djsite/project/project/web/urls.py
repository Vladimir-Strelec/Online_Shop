from django.urls import path
from .views import __index__, categories

urlpatterns = [
    path('', __index__),
    path('categories/<slug:slug>/', categories),
]
