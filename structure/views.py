from django.shortcuts import render, redirect, get_object_or_404
from .models import Entreprise, Filiale, User, Client
from .forms import EntrepriseForm, FilialeForm, UserForm, ClientForm
from localisation.models import Ville


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


def update_user(request, pk):
    """

    :param pk:
    :param request:
    :return:
    """
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('structure:user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'structure/user/update_user.html', {'form': form, 'user': user})


def delete_user(request, pk):
    """

    :param request:
    :param pk:
    :return:
    """
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('structure:user_list')
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


def update_entreprise(request, pk):
    """

    :param pk:
    :param request:
    :return:
    """
    entreprise = get_object_or_404(Entreprise, pk=pk)
    if request.method == 'POST':
        form = EntrepriseForm(request.POST, instance=entreprise)
        if form.is_valid():
            form.save()
            return redirect('structure:entreprise_list')
    else:
        form = EntrepriseForm(instance=entreprise)
    return render(request, 'structure/entreprise/update_entreprise.html', {'form': form, 'entreprise': entreprise})


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
    villes = Ville.objects.all()

    entreprises = Entreprise.objects.all()

    if request.method == "POST":
        entreprise = request.POST.get('entreprise')
        viller = request.POST.get('ville')
        nom = request.POST.get('nom')
        adresse = request.POST.get('adresse')
        tel = request.POST.get('tel')
        ville = Ville.objects.get(pk=viller)
        entreprise = Entreprise.objects.get(pk=entreprise)
        Filiale.objects.create(ville=ville, entreprise=entreprise, nom=nom, adresse=adresse, tel=tel)
        return redirect('structure:filiale_list')
    return render(request, 'structure/filiale/add_filiale.html', {'villes': villes, 'entreprises': entreprises})


def update_filiale(request, pk):
    """

    :param pk:
    :param request:
    :return:
    """
    villes = Ville.objects.all()

    entreprises = Entreprise.objects.all()
    filiale = get_object_or_404(Filiale, pk=pk)
    if request.method == 'POST':
        form = FilialeForm(request.POST, instance=filiale)
        if form.is_valid():
            form.save()
            return redirect('structure:filiale_list')
    else:
        form = FilialeForm(instance=filiale)
    return render(request, 'structure/filiale/update_filiale.html', {'form': form, 'filiale': filiale, 'villes': villes, 'entreprises':entreprises})


def delete_filiale(request, pk):
    """

    :param request:
    :param pk:
    :return:
    """
    filiale = get_object_or_404(Filiale, pk=pk)
    if request.method == 'POST':
        filiale.delete()
        return redirect('structure:filiale_list')
    return render(request, 'structure/filiale/list_filiale.html', {'filiale': filiale})


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
    users = User.objects.all()

    if request.method == "POST":
        user = request.POST.get('user')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        adresse = request.POST.get('adresse')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        user = User.objects.get(pk=user)
        Client.objects.create(user=user, nom=nom, prenom=prenom, adresse=adresse, email=email, tel=tel)
        return redirect('structure:client_list')
    return render(request, 'structure/client/create_client.html', {'users': users})


def update_client(request, pk):
    """

    :param pk:
    :param request:
    :return:
    """
    users = User.objects.all()
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('structure:client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'structure/client/update_client.html', {'form': form, 'client': client, 'users': users})


def delete_client(request, pk):
    """

    :param request:
    :param pk:
    :return:
    """
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('structure:client_list')
    return render(request, 'structure/client/list_client.html', {'client': client})
