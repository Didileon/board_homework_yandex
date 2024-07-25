from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .filters import AdvertFilter
from .forms import AdvertForm
from .models import Advert
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class AdvertList(ListView):
    """Все объявления"""
    model = Advert
    context_object_name = 'advert'
    queryset = Advert.objects.all()
    template_name = 'board/advert-list.html'
    paginate_by = 3


    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = AdvertFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context

class AdvertDetail(DetailView):
    """Подробно об объявлении"""
    model = Advert
    context_object_name = "advert"
    template_name = 'board/advert-detail.html'


# Добавляем новое представление для создания товаров.
class AdvertCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    # Указываем нашу разработанную форму
    form_class = AdvertForm
    # модель товаров
    model = Advert
    # и новый шаблон, в котором используется форма.
    template_name = 'board/advert_edit.html'


class AdvertUpdate(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = AdvertForm
    model = Advert
    template_name = 'board/advert_edit.html'



class AdvertDelete(LoginRequiredMixin, DeleteView): #PermissionRequiredMixin,
    #permission_required = ('board.delete_advert', )
    raise_exception = True
    model = Advert
    template_name = 'board/advert_delete.html'
    success_url = reverse_lazy('advert-list')
   # success_url = 'http://127.0.0.1:8000'
