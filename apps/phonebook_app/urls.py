from django.urls import path
from .views import PhonebookListView, PhonebookAPI, PhonebookDetailView, SearchView, initial_view, SignUpView, \
    PhonebookDeleteView, UserCreateView, make_user, make_middleuser, make_superuser
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', initial_view, name='initial'),
    path('phonebook/', PhonebookListView.as_view(), name='phonebook'),
    path('phonebook/<int:pk>', PhonebookDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', PhonebookDeleteView.as_view(), name='delete'),
    path('create/', UserCreateView.as_view(), name='create'),
    path('search/', SearchView.as_view(), name='search'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('make-user/<int:pk>', make_user, name='make-user'),
    path('make-middleuser/<int:pk>', make_middleuser, name='make-middleuser'),
    path('make-superuser/<int:pk>', make_superuser, name='make-superuser'),

    # path('api/phonebook/', PhonebookAPI.as_view({'get': 'list', 'post': 'create'})),
    # path('api/phonebook/<int:pk>', PhonebookAPI.as_view({'get': 'retrieve', 'put': 'update'})),
]
