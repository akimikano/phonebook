from django.views.generic import TemplateView, DetailView
from django.views.generic.list import ListView
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apps.phonebook_app.models import Person
from apps.phonebook_app.serializers import PersonSerializer, PersonSerializerDetail
from phonebook.settings import REST_FRAMEWORK


class PhonebookListView(ListView):
    template_name = 'index.html'
    queryset = Person.objects.all()
    allow_empty = False
    paginate_by = 9
    context_object_name = 'person_list'


class PhonebookDetailView(DetailView):
    model = Person
    template_name = 'detail.html'
    context_object_name = 'phonebook_item'


class SearchView(TemplateView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('text1')
        context = super().get_context_data()
        searched_items = Person.objects.filter(phone__startswith=query)
        context['searched_items'] = searched_items
        return context


class PhonebookAPI(ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    pagination_class = PageNumberPagination
    page_size = REST_FRAMEWORK['PAGE_SIZE']

    def get_object(self):
        if 'pk' in self.kwargs:
            self.serializer_class = PersonSerializerDetail
            obj = Person.objects.get(id=self.kwargs['pk'])
            return obj

    def create(self, request, *args, **kwargs):
        serializer = PersonSerializerDetail(data=request.data)  # Метод переопределен для использования
        serializer.is_valid(raise_exception=True)               # нужного сериалайзера
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



