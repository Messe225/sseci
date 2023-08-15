# Generated by Django 4.1.7 on 2023-05-30 16:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_etudiant_carte_cni_etudiant_carte_etudiant_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='specialite',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.specialite', verbose_name='Spécialité'),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=150, verbose_name="Date d'identification"),
        ),
    ]
