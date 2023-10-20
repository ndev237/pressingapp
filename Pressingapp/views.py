from django.shortcuts import render, redirect


def home(request):
    """

    :param request:
    :return:
    """
    return render(request, 'home.html')
