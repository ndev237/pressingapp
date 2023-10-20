from django.shortcuts import render, redirect, get_object_or_404
from .models import Entreprise, Filiale, User, Client
from .forms import EntrepriseForm, FilialeForm, UserForm, ClientForm


def index(request):
    """

    :param request:
    :return:
    """
    return render(request, "structure/index.html")


def list_user(request):
    """

    :param request:
    :return:
    """
    users = User.objects.all()
    return render(request, 'structure/user/list_user.html', {'users': users})


def create_user(request):
    """

    :param request:
    """
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('structure:user_list')
    else:
        form = UserForm()
    return render(request, 'structure/user/create_user.html', {'form': form})


def update_user(request, id):
    """

    :param id:
    :param request:
    :return:
    """
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('structure:user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'structure/user/update_user.html', {'form': form}, {'user': user})


def delete_user(request, id):
    """

    :param request:
    :param id:
    :return:
    """
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        user.delete()
        return redirect('structure:continant_list')
    return render(request, 'structure/user/delete_user.html', {'user': user})


def list_entreprise(request):
    """

    :param request:
    :return:
    """
    entreprises = Entreprise.objects.all()
    return render(request, 'structure/entreprise/list_entreprise.html', {'entreprises': entreprises})


def create_entreprise(request):
    """

    :param request:
    """
    if request.method == 'POST':
        form = EntrepriseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('structure:entreprise_list')
    else:
        form = EntrepriseForm()
    return render(request, 'structure/entreprise/create_entreprise.html', {'form': form})


def update_entreprise(request, id):
    """

    :param id:
    :param request:
    :return:
    """
    entreprise = get_object_or_404(Entreprise, pk=id)
    if request.method == 'POST':
        form = EntrepriseForm(request.POST, instance=entreprise)
        if form.is_valid():
            form.save()
            return redirect('structure:entreprise_list')
    else:
        form = EntrepriseForm(instance=entreprise)
    return render(request, 'structure/entreprise/update_entreprise.html', {'form': form}, {'entreprise': entreprise})


def delete_entreprise(request, id):
    """

    :param request:
    :param id:
    :return:
    """
    entreprise = get_object_or_404(Entreprise, pk=id)
    if request.method == 'POST':
        entreprise.delete()
        return redirect('structure:entreprise_list')
    return render(request, 'structure/entreprise/delete_entreprise.html', {'entreprise': entreprise})


def list_filiale(request):
    """

    :param request:
    :return:
    """
    filiales = Filiale.objects.all()
    return render(request, 'structure/filiale/list_filiale.html', {'filiales': filiales})


def create_filiale(request):
    """

    :param request:
    """
    if request.method == 'POST':
        form = FilialeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('structure:filiale_list')
    else:
        form = FilialeForm()
    return render(request, 'structure/filiale/create_filiale.html', {'form': form})


def update_filiale(request, id):
    """

    :param id:
    :param request:
    :return:
    """
    filiale = get_object_or_404(Filiale, pk=id)
    if request.method == 'POST':
        form = FilialeForm(request.POST, instance=filiale)
        if form.is_valid():
            form.save()
            return redirect('structure:filiale_list')
    else:
        form = FilialeForm(instance=filiale)
    return render(request, 'structure/filiale/update_filiale.html', {'form': form}, {'filiale': filiale})


def delete_filiale(request, id):
    """

    :param request:
    :param id:
    :return:
    """
    filiale = get_object_or_404(Filiale, pk=id)
    if request.method == 'POST':
        filiale.delete()
        return redirect('structure:filiale_list')
    return render(request, 'structure/filiale/delete_filiale.html', {'filiale': filiale})


def list_client(request):
    """

    :param request:
    :return:
    """
    clients = Client.objects.all()
    return render(request, 'structure/client/list_client.html', {'clients': clients})


def create_client(request):
    """

    :param request:
    """
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('structure:client_list')
    else:
        form = ClientForm()
    return render(request, 'structure/client/create_client.html', {'form': form})


def update_client(request, id):
    """

    :param id:
    :param request:
    :return:
    """
    client = get_object_or_404(Client, pk=id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('structure:client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'structure/client/update_client.html', {'form': form}, {'client': client})


def delete_client(request, id):
    """

    :param request:
    :param id:
    :return:
    """
    client = get_object_or_404(Client, pk=id)
    if request.method == 'POST':
        client.delete()
        return redirect('structure:client_list')
    return render(request, 'structure/client/delete_client.html', {'client': client})
