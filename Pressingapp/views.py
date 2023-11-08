from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from .forms import MessageForm


def home(request):
    """

    :param request:
    :return:
    """

    return render(request, 'home.html')


def list_mess(requests):
    """

    :param requests:
    """
    messages = Message.objects.all()
    return render(requests, 'list_message.html', {'messages': messages})


def add_mess(request):
    """

    :param request:
    :return:
    """
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MessageForm()
    return render(request, 'home.html', {'form': form})
