from django import forms
from .models import User, Entreprise, Filiale, Client


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'sex', 'username', 'email', 'groups', 'user_permissions']
        widgets = {'sex': forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 '
                                                       'text-sm rounded-lg focus:ring-blue-500'
                                                       'focus:border-blue-500 block w-full p-2.5 '
                                                       'dark:bg-gray-700 dark:border-gray-600'
                                                       'dark:placeholder-gray-400 dark:text-white '
                                                       'dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
                   'last_name': forms.TextInput(attrs={'class': 'block w-full rounded-md border-0 px-3.5 py-2 pl-20 '
                                                                'text-gray-900 shadow-sm ring-1 ring-inset '
                                                                'ring-gray-300 placeholder:text-gray-400 '
                                                                'focus:ring-2 focus:ring-inset '
                                                                'focus:ring-indigo-600 sm:text-sm sm:leading-6'}),
                   'first_name': forms.TextInput(attrs={'class': 'block w-full rounded-md border-0 px-3.5 py-2 pl-20 '
                                                                 'text-gray-900 shadow-sm ring-1 ring-inset '
                                                                 'ring-gray-300 placeholder:text-gray-400 '
                                                                 'focus:ring-2 focus:ring-inset '
                                                                 'focus:ring-indigo-600 sm:text-sm sm:leading-6'}),
                   'username': forms.TextInput(attrs={'class': 'block w-full rounded-md border-0 px-3.5 py-2 pl-20 '
                                                               'text-gray-900 shadow-sm ring-1 ring-inset '
                                                               'ring-gray-300 placeholder:text-gray-400 '
                                                               'focus:ring-2 focus:ring-inset '
                                                               'focus:ring-indigo-600 sm:text-sm sm:leading-6'}),
                   'email': forms.TextInput(attrs={'class': 'block w - full rounded - md border - 0 px - 3.5 py - 2 '
                                                            'pl - 20'
                                                            'text-gray-900 shadow-sm ring-1 ring-inset '
                                                            'ring-gray-300 placeholder:text-gray-400 '
                                                            'focus:ring-2 focus:ring-inset '
                                                            'focus:ring-indigo-600 sm:text-sm sm:leading-6'}),
                   'groups': forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 '
                                                          'text-sm rounded-lg focus:ring-blue-500'
                                                          'focus:border-blue-500 block w-full p-2.5 '
                                                          'dark:bg-gray-700 dark:border-gray-600'
                                                          'dark:placeholder-gray-400 dark:text-white '
                                                          'dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
                   'user_permissions': forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 '
                                                                    'text-sm rounded-lg focus:ring-blue-500'
                                                                    'focus:border-blue-500 block w-full p-2.5 '
                                                                    'dark:bg-gray-700 dark:border-gray-600'
                                                                    'dark:placeholder-gray-400 dark:text-white '
                                                                    'dark:focus:ring-blue-500 '
                                                                    'dark:focus:border-blue-500'}),
                   }


class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = ['nom', 'adresse', 'tel']


class FilialeForm(forms.ModelForm):
    class Meta:
        model = Filiale
        fields = ['entreprise', 'ville', 'nom', 'adresse', 'tel']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['user', 'nom', 'prenom', 'adresse', 'email', 'tel']
