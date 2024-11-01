# Generated by Django 5.1.2 on 2024-10-27 16:48

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('art_image', models.ImageField(upload_to='art_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exposition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Galerie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('adresse', models.CharField(max_length=255)),
                ('description', models.TextField()),
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
                ('is_admin', models.BooleanField(default=False, verbose_name='Is admin')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('liked_paintings', models.ManyToManyField(blank=True, related_name='liked_by_users', to='photofolio.artimages')),
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
        migrations.AddField(
            model_name='artimages',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='art_images', to='photofolio.artist'),
        ),
        migrations.CreateModel(
            name='ArtGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Gallery Name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='galleries/')),
                ('adresse', models.CharField(max_length=255, verbose_name='Address')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('heures_ouverture', models.TimeField(verbose_name='Opening Hours')),
                ('heures_fermeture', models.TimeField(verbose_name='Closing Hours')),
                ('expositions', models.ManyToManyField(blank=True, related_name='galleries', to='photofolio.exposition', verbose_name='Expositions')),
            ],
        ),
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('type_catalogue', models.CharField(choices=[('galerie', 'Galerie'), ('exposition', 'Exposition'), ('les_deux', 'Les deux')], default='galerie', max_length=20)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('exposition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photofolio.exposition')),
                ('galerie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photofolio.galerie')),
            ],
        ),
        migrations.CreateModel(
            name='Avis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
                ('note', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type_avis', models.CharField(choices=[('galerie', 'Galerie'), ('exposition', 'Exposition'), ('les_deux', 'Les deux')], default='galerie', max_length=20)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('exposition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photofolio.exposition')),
                ('galerie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photofolio.galerie')),
            ],
        ),
        migrations.CreateModel(
            name='PlannedVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Visit Name')),
                ('date_visite', models.DateField(verbose_name='Visit Date')),
                ('duree_estimee', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Estimated Duration (hours)')),
                ('statut_visite', models.CharField(choices=[('planned', 'Planned'), ('completed', 'Completed'), ('canceled', 'Canceled')], default='planned', max_length=10, verbose_name='Visit Status')),
                ('galleries_a_visiter', models.ManyToManyField(related_name='planned_visits', to='photofolio.artgallery', verbose_name='List of Galleries to Visit')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('entry_time', models.TimeField()),
                ('status', models.CharField(choices=[('valid', 'Valide'), ('cancelled', 'Annulé')], default='Reserved', max_length=10)),
                ('exposition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photofolio.exposition')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='exposition',
            name='attendees',
            field=models.ManyToManyField(related_name='expositions', through='photofolio.Reservation', to=settings.AUTH_USER_MODEL),
        ),
    ]
