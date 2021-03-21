from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView
from django.views.generic.list import ListView
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .forms import SignUpForm, UserForm
from .models import PhonebookUser
from .serializers import PersonSerializer, PersonSerializerDetail
from phonebook.settings import REST_FRAMEWORK


class PhonebookListView(ListView):
    template_name = 'index.html'
    queryset = PhonebookUser.objects.all()
    allow_empty = True
    paginate_by = 15
    context_object_name = 'person_list'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        if request.user.status == 0:
            return redirect(reverse('detail', kwargs={'pk': self.request.user.id}))
        return super(PhonebookListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        print(self.request.user.status)
        if self.request.user.status == 2:
            return self.queryset
        if self.request.user.status == 1:
            if self.request.user.city:
                queryset = PhonebookUser.objects.filter(city=self.request.user.city)
            else:
                queryset = PhonebookUser.objects.filter(id=self.request.user.id)
            return queryset


class PhonebookDetailView(DetailView):
    model = PhonebookUser
    template_name = 'detail.html'
    context_object_name = 'phonebook_item'


class PhonebookDeleteView(DeleteView):
    model = PhonebookUser
    success_url = '/phonebook'
    template_name = 'phonebookuser_confirm_delete.html'


class SearchView(TemplateView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('text1')
        context = super().get_context_data()
        searched_items = PhonebookUser.objects.filter(
                Q(name__icontains=query) |
                Q(surname__icontains=query) |
                Q(phone__icontains=query) |
                Q(city__name__icontains=query)
                )
        context['searched_items'] = searched_items
        context['person_list'] = PhonebookUser.objects.all()
        return context


class PhonebookAPI(ModelViewSet):
    serializer_class = PersonSerializer
    queryset = PhonebookUser.objects.all()
    pagination_class = PageNumberPagination
    page_size = REST_FRAMEWORK['PAGE_SIZE']

    def get_queryset(self, **kwargs):
        print(kwargs)
        word = self.request.GET['name']
        print(self.request.GET)
        print(word)
        objs = PhonebookUser.objects.filter(name=word)
        return objs

    def get_object(self):
        if 'pk' in self.kwargs:
            self.serializer_class = PersonSerializerDetail
            obj = PhonebookUser.objects.get(id=self.kwargs['pk'])
            return obj

    def create(self, request, *args, **kwargs):
        serializer = PersonSerializerDetail(data=request.data)  # Метод переопределен для использования
        serializer.is_valid(raise_exception=True)               # нужного сериалайзера
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TestAPI(APIView):

    def get(self, request):
        obj = PhonebookUser.objects.filter(name=request.query_params['name'])
        print(obj)
        serializer = PersonSerializerDetail(obj, many=True)
        print(serializer.data)
        return Response(serializer.data)


def initial_view(request):
    return render(request, 'initial.html')


# def register(request):
#     if request.method == 'POST':
#         print(request.POST)
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             print('hello')
#             form.save()
#             return redirect('initial')
#     form = SignUpForm
#     context = {
#         'form': form
#     }
#     return render(request, 'signup.html', context)

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = '/'
    template_name = 'signup.html'


class UserCreateView(CreateView):
    form_class = UserForm
    success_url = '/phonebook'
    template_name = 'user-create.html'


def make_user(request, *args, **kwargs):
    user = PhonebookUser.objects.get(id=kwargs['pk'])
    user.status = 0
    user.save()
    return redirect('phonebook')


def make_middleuser(request, *args, **kwargs):
    user = PhonebookUser.objects.get(id=kwargs['pk'])
    print((datetime.today().year - user.get_in_date.year) * 12 + (datetime.today().month - user.get_in_date.month))
    # print(datetime.today().strftime('%d-%m-%Y').split('-'), user.get_in_date.split('-'))
    # ((date1.Year - date2.Year) * 12) + date1.Month - date2.Month
    user = PhonebookUser.objects.get(id=kwargs['pk'])
    user.status = 1
    user.save()
    return redirect('phonebook')


def make_superuser(request, *args, **kwargs):
    user = PhonebookUser.objects.get(id=kwargs['pk'])
    user.status = 2
    user.save()
    return redirect('phonebook')


