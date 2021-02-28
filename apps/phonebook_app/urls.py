from django.urls import path

from apps.phonebook_app.views import PhonebookListView, PhonebookAPI, PhonebookDetailView, SearchView

urlpatterns = [
    path('phonebook/', PhonebookListView.as_view(), name='phonebook'),
    path('phonebook/<int:pk>', PhonebookDetailView.as_view(), name='phonebook_detail'),
    path('search/', SearchView.as_view(), name='search'),
    path('api/phonebook/', PhonebookAPI.as_view({'get': 'list', 'post': 'create'})),
    path('api/phonebook/<int:pk>', PhonebookAPI.as_view({'get': 'retrieve', 'put': 'update'})),
]
