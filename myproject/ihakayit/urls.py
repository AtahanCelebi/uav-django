from django.urls import path
from .views import *
urlpatterns = [
    path('ihas/register/', IHARegistrationView.as_view(),name='add-iha'),
    path('ihas/list/', IHAListView.as_view(),name='get-list'),
    path('ihas/filter/', IHAFilterView.as_view(),name='search-iha'),
    path('ihas/<id>/delete/', IHADeleteView.as_view(), name='delete-iha'),
    path('ihas/<id>/update/', IHAUpdateView.as_view(), name='update-iha'),
]
