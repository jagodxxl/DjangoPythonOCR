# -*- coding: utf-8 -*-

from django.shortcuts import render


def index(request):
    """Strona główna"""
    kontekst = {'komunikat': 'Witaj w aplikacji!'}
    return render(request, 'mainpage.html', kontekst)
