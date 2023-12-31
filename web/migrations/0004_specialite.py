# Generated by Django 4.1.7 on 2023-05-29 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_remove_etudiant_specialite_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=70, unique=True, verbose_name='Libellé')),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.filiere', verbose_name='Filière')),
            ],
            options={
                'verbose_name_plural': 'Specialité',
            },
        ),
    ]
