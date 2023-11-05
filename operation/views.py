from django.shortcuts import render, redirect, get_object_or_404
from .models import Commande, CommandeArticle, LigneCommande, Service, Article
from .forms import CommandeForm, ArticleForm, CommandeArticleForm, LigneCommandeForm, ServiceForm
from structure.models import Filiale, Entreprise, Client


def index(request):
    """

    :param request:
    :return:
    """
    return render(request, "operation/index.html")


def list_article(request):
    """

    :param request:
    :return:
    """
    articles = Article.objects.all()
    return render(request, 'operation/article/list_article.html', {'articles': articles})


def add_article(request):
    """

    :param request:
    :return:
    """
    clients = Client.objects.all()

    if request.method == 'POST':
        client = request.POST.get('client')
        nombre = request.POST.get('nombre')
        prix = request.POST.get('prix')
        intitule = request.POST.get('intitule')
        client = Client.objects.get(pk=client)
        Article.objects.create(client=client, nombre=nombre, prix=prix, intitule=intitule)
        return redirect('operation:article_list')
    return render(request, 'operation/article/add_article.html', {'clients': clients})


def update_article(request, pk):
    """

    :param request:
    :param pk:
    :return:
    """
    clients = Client.objects.all()
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('operation:article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'operation/article/update_article.html', {'form': form, 'article': article, 'clients': clients})


def delete_article(request, pk):
    """

    :param request:
    :param pk:
    :return:
    """
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('operation:article_list')
    return render(request, 'operation/article/delete_article.html', {'article': article})


def list_service(request):
    """

    :param request:
    :return:
    """
    services = Service.objects.all()
    return render(request, 'operation/service/list_service.html', {'services': services})


def add_service(request):
    """

    :param request:
    :return:
    """
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('operation:service_list')
    else:
        form = ServiceForm()
    return render(request, 'operation/service/add_service.html', {'form': form})


def update_service(request, pk):
    """

    :param request:
    :param pk:
    :return:
    """
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('operation:service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'operation/service/update_service.html', {'form': form, 'service': service})


def delete_service(request, pk):
    """

    :param request:
    :param pk:
    :return:
    """
    service = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('operation:service_list')
    return render(request, 'operation/service/delete_service.html', {'service': service})


def list_commande(request):
    """

    :param request:
    :return:
    """
    commandes = Commande.objects.all()
    return render(request, 'operation/commande/list_commande.html', {'commandes': commandes})


def add_commande(request):
    """

    :param request:
    :return:
    """
    clients = Client.objects.all()
    filiales = Filiale.objects.all()

    if request.method == "POST":
        client = request.POST.get('client')
        filiale = request.POST.get('filiale')
        date = request.POST.get('date')
        prix = request.POST.get('prix')
        client = Client.objects.get(pk=client)
        filiale = Filiale.objects.get(pk=filiale)
        Commande.objects.create(client=client, filiale=filiale, date=date, prix=prix)
        return redirect('operation:commande_list')

    return render(request, 'operation/commande/add_commande.html', {'clients': clients, 'filiales': filiales})


def update_commande(request, pk):
    """

    :param request:
    :param pk:
    :return:
    """
    clients = Client.objects.all()
    filiales = Filiale.objects.all()
    commande = get_object_or_404(Commande, pk=pk)

    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('operation:commande_list')
    else:
        form = CommandeForm(instance=commande)
    return render(request, 'operation/commande/update_commande.html',
                  {'form': form, 'clients': clients, 'filiales': filiales})


def delete_commande(request, pk):
    """

    :param request:
    :param pk:
    :return:
    """
    commande = get_object_or_404(Commande, pk=pk)
    if request.method == 'POST':
        commande.delete()
        return redirect('operation:commande_list')
    return render(request, 'operation/commande/list_commande.html', {'commande': commande})


def list_comart(request):
    """

    :param request:
    :return:
    """
    comarts = CommandeArticle.objects.all()
    return render(request, 'operation/commandearticle/list_comart.html', {'comarts': comarts})


def add_comart(request):
    """

    :param request:
    :return:
    """
    commandes = Commande.objects.all()
    articles = Article.objects.all()

    if request.method == "POST":
        commande = request.POST.get('commande')
        article = request.POST.get('article')
        quantite = request.POST.get('quantite')
        montant = request.POST.get('montant')
        commande = Commande.objects.get(pk=commande)
        article = Article.objects.get(pk=article)
        CommandeArticle.objects.create(commande=commande, article=article, quantite=quantite, montant=montant)
        return redirect('operation:comart_list')

    return render(request, 'operation/commandearticle/add_comart.html', {'commandes': commandes, 'articles': articles})


def update_comart(request, pk):
    """

    :param request:
    :param pk:
    :return:
    """
    commandes = Commande.objects.all()
    articles = Article.objects.all()
    comart = get_object_or_404(CommandeArticle, pk=pk)

    if request.method == 'POST':
        form = CommandeArticleForm(request.POST, instance=comart)
        if form.is_valid():
            form.save()
            return redirect('operation:comart_list')
    else:
        form = CommandeArticleForm(instance=comart)
    return render(request, 'operation/commandearticle/update_comart.html',
                  {'form': form, 'commandes': commandes, 'articles': articles})


def delete_comart(request, pk):
    comart = get_object_or_404(CommandeArticle, pk=pk)
    if request.method == 'POST':
        comart.delete()
        return redirect('operation:comart_list')
    return render(request, 'operation/commandearticle/list_comart.html', {'comart': comart})


def list_ligncom(request):
    ligncoms = LigneCommande.objects.all()
    return render(request, 'operation/lignecommande/list_ligncom.html', {'ligncoms': ligncoms})


def add_ligncom(request):
    commandes = Commande.objects.all()
    services = Service.objects.all()
    if request.method == "POST":
        commande = request.POST.get('commande')
        service = request.POST.get('service')
        intitule = request.POST.get('intitule')
        commande = Commande.objects.get(pk=commande)
        service = Service.objects.get(pk=service)
        LigneCommande.objects.create(commande=commande, service=service, intitule=intitule)
        return redirect('operation:ligncom_list')

    return render(request, 'operation/lignecommande/add_ligncom.html', {'commandes': commandes, 'services': services})


def update_ligncom(request, pk):
    commandes = Commande.objects.all()
    services = Service.objects.all()
    ligncom = get_object_or_404(LigneCommande, pk=pk)

    if request.method == 'POST':
        form = LigneCommandeForm(request.POST, instance=ligncom)
        if form.is_valid():
            form.save()
            return redirect('operation:ligncom_list')
    else:
        form = LigneCommandeForm(instance=ligncom)
    return render(request, 'operation/lignecommande/update_ligncom.html',
                  {'form': form, 'commandes': commandes, 'services': services})


def delete_ligncom(request, pk):
    ligncom = get_object_or_404(LigneCommande, pk=pk)
    if request.method == 'POST':
        ligncom.delete()
        return redirect('operation:ligncom_list')
    return render(request, 'operation/lignecommande/list_ligncom.html', {'ligncom': ligncom})
