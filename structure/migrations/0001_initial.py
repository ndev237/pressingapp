# Generated by Django 4.2.5 on 2023-10-17 10:42

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import ulid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('localisation', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entreprise',
            fields=[
                ('id', models.CharField(db_index=True, default=ulid.ulid, editable=False, max_length=30, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=20)),
                ('adresse', models.CharField(max_length=20)),
                ('tel', models.IntegerField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('sex', models.CharField(choices=[('man', 'Homme'), ('Woman', 'Femme')], max_length=12)),
                ('groups', models.ManyToManyField(related_name='custom_user_group', to='auth.group')),
                ('parent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='structure.user')),
                ('user_permissions', models.ManyToManyField(related_name='custom_user_permission', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Filiale',
            fields=[
                ('id', models.CharField(db_index=True, default=ulid.ulid, editable=False, max_length=30, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=20)),
                ('adresse', models.CharField(max_length=20)),
                ('tel', models.IntegerField(max_length=9)),
                ('entreprise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='structure.entreprise')),
                ('ville', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='localisation.ville')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.CharField(db_index=True, default=ulid.ulid, editable=False, max_length=30, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=15)),
                ('prenom', models.CharField(max_length=15)),
                ('adresse', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=40)),
                ('tel', models.IntegerField(max_length=9)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='structure.user')),
            ],
        ),
    ]
