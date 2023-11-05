from django.shortcuts import render, redirect, get_object_or_404
from .models import Continant, Pays, Ville, Quartier
from .forms import ContinantForm, PaysForm, VilleForm, QuartierForm


def index(request):
    """

    :param request:
    :return:
    """
    return render(request, "localisation/index.html")


def list_conti(request):
    """

    :param request:
    :return:
    """
    continents = Continant.objects.all()
    return render(request, 'localisation/continant/list_conti.html', {'continants': continents})


def create_conti(request):
    """

    :param request:
    """
    if request.method == 'POST':
        form = ContinantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('localisation:continant_list')
    else:
        form = ContinantForm()
    return render(request, 'localisation/continant/create_conti.html', {'form': form})


def update_conti(request, pk):
    """

    :param pk:
    :param request:
    :return:
    """
    continent = get_object_or_404(Continant, pk=pk)
    if request.method == 'POST':
        form = ContinantForm(request.POST, instance=continent)
        if form.is_valid():
            form.save()
            return redirect('localisation:continant_list')
    else:
        form = ContinantForm(instance=continent)
    return render(request, 'localisation/continant/update_conti.html', {'form': form, 'continant': continent})


def delete_conti(request, pk):
    """

    :param request:
    :param pk:
    :return:
    """
    continent = get_object_or_404(Continant, pk=pk)
    if request.method == 'POST':
        continent.delete()
        return redirect('localisation:continant_list')
    return render(request, 'localisation/continant/delete_conti.html', {'continant': continent})


def list_pays(request):
    """

    :param request:
    :return:
    """
    pays = Pays.objects.all()
    return render(request, 'localisation/pays/list_pays.html', {'pays': pays})


def create_pays(request):
    """

    :param request:

"""

    continants = Continant.objects.all()

    if request.method == "POST":
        continant = request.POST.get('continant')
        intitule = request.POST.get('intitule')
        continant = Continant.objects.get(pk=continant)
        continant.save()
        Pays.objects.create(continant=continant, intitule=intitule)
        return redirect('localisation:pays_list')
    return render(request, 'localisation/pays/create_pays.html', {'continants': continants})


def update_pays(request, pk):
    """

    :param pk:
    :param request:
    :return:
    """
    continants = Continant.objects.all()
    pays = get_object_or_404(Pays, pk=pk)
    if request.method == 'POST':
        form = PaysForm(request.POST, instance=pays)
        if form.is_valid():
            form.save()
            return redirect('localisation:pays_list')
    else:
        form = PaysForm(instance=pays)
    return render(request, 'localisation/pays/update_pays.html', {'form': form, 'pays': pays, 'continants': continants})


def delete_pays(request, pk):
    """

    :param request:
    :param pk:
    :return:
    """
    pays = get_object_or_404(Pays, pk=pk)
    if request.method == 'POST':
        pays.delete()
        return redirect('localisation:pays_list')
    return render(request, 'localisation/pays/delete_pays.html', {'pays': pays})


def list_ville(request):
    """

    :param request:
    :return:
    """
    villes = Ville.objects.all()
    return render(request, 'localisation/ville/list_ville.html', {'villes': villes})


def create_ville(request):
    """
    :param request:


    """

    pays = Pays.objects.all()

    if request.method == "POST":
        pays = request.POST.get('pays')
        intitule = request.POST.get('intitule')
        pays = Pays.objects.get(pk=pays)
        pays.save()
        Ville.objects.create(pays=pays, intitule=intitule)
        return redirect('localisation:ville_list')

    return render(request, 'localisation/ville/create_ville.html', {'pays': pays})


def update_ville(request, pk):
    """

    :param pk:
    :param request:
    :return:
    """
    pays = Pays.objects.all()
    ville = get_object_or_404(Ville, pk=pk)
    if request.method == 'POST':
        form = VilleForm(request.POST, instance=ville)
        if form.is_valid():
            form.save()
            return redirect('localisation:ville_list')
    else:
        form = VilleForm(instance=ville)
    return render(request, 'localisation/ville/update_ville.html', {'form': form, 'ville': ville, 'pays': pays})


def delete_ville(request, pk):
    """

    :param request:
    :param pk:
    :return:
    """
    ville = get_object_or_404(Ville, pk=pk)
    if request.method == 'POST':
        ville.delete()
        return redirect('localisation:ville_list')
    return render(request, 'localisation/ville/delete_ville.html', {'ville': ville})


def list_quartier(request):
    """

    :param request:
    :return:
    """
    quartiers = Quartier.objects.all()
    return render(request, 'localisation/quartier/list_quartier.html', {'quartiers': quartiers})


def create_quartier(request):
    """

    :param request:

    """

    villes = Ville.objects.all()

    if request.method == "POST":
        ville = request.POST.get('ville')
        intitule = request.POST.get('intitule')
        ville = Ville.objects.get(pk=ville)
        ville.save()
        Quartier.objects.create(ville=ville, intitule=intitule)
        return redirect('localisation:quartier_list')

    return render(request, 'localisation/quartier/create_quartier.html', {'villes': villes})


def update_quartier(request, pk):
    """

    :param pk:
    :param request:
    :return:
    """
    villes = Ville.objects.all()
    quartier = get_object_or_404(Quartier, pk=pk)
    if request.method == 'POST':
        form = QuartierForm(request.POST, instance=quartier)
        if form.is_valid():
            form.save()
            return redirect('localisation:quartier_list')
    else:
        form = VilleForm(instance=quartier)
    return render(request, 'localisation/quartier/update_quartier.html', {'form': form, 'quartier': quartier, 'villes': villes})


def delete_quartier(request, pk):
    """

    :param request:
    :param pk:
    :return:
    """
    quartier = get_object_or_404(Quartier, pk=pk)
    if request.method == 'POST':
        quartier.delete()
        return redirect('localisation:quartier_list')
    return render(request, 'localisation/quartier/list_quartier.html', {'quartier': quartier})
