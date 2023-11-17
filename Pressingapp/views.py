from django.shortcuts import render, redirect, get_object_or_404



def home(request):
    """

    :param request:
    :return:
    """

    return render(request, 'home.html')
