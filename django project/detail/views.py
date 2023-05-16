from django.shortcuts import render


def detail(request):
    return render(request, 'detail1.html', {})