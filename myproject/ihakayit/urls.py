from django.urls import path
from .views import *
urlpatterns = [
    path('add/', IHARegistrationView.as_view(),name='add-iha'),
    path('list/', IHAListView.as_view(),name='get-list'),
    path('search/', IHAFilterView.as_view(),name='search-iha'),
    path('delete/<int:id>', IHADeleteView.as_view(), name='delete-iha'),
    path('update/<int:id>', IHAUpdateView.as_view(), name='update-iha'),
]
