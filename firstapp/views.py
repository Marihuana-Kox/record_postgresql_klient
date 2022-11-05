from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import MainStartPage


class MainPage(View):
    '''Вывод главной страницы'''
    def get(self, request):
        template_name = 'firstapp/content.html'
        queryset = MainStartPage.objects.get(pk=1)
        return render(request, template_name, {'context': queryset,})