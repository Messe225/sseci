from django.contrib import admin
from .models import *

# Register your models here.
class UniversiteAdmin(admin.ModelAdmin):
    list_display = ['code','name','email','contact']
    search_fields = ['name']


admin.site.register(Universite, UniversiteAdmin)

# Register your models here.
class SexeAdmin(admin.ModelAdmin):
    list_display = ['libelle']
    search_fields = ['libelle']


admin.site.register(Sexe, SexeAdmin)

# Register your models here.
class UfrAdmin(admin.ModelAdmin):
    list_display = ['code','name','email','contact','universite']
    search_fields = ['name']

admin.site.register(Ufr, UfrAdmin)

# Register your models here (id_filiere,code,name,email,contact,#id_ufr).
class FiliereAdmin(admin.ModelAdmin):
    list_display = ['code','name','email','contact','ufr']
    search_fields = ['name']

admin.site.register(Filiere, FiliereAdmin)

# Register your models here (id_specialite,libelle,#id_filiere).
class SpecialiteAdmin(admin.ModelAdmin):
    list_display = ['libelle','filiere']
    search_fields = ['libelle']

admin.site.register(Specialite, SpecialiteAdmin)

# Register your models here Niveau (id_niveau,libelle).
class NiveauAdmin(admin.ModelAdmin):
    list_display = ['libelle']
    search_fields = ['libelle']

admin.site.register(Niveau, NiveauAdmin)

# Register your models here Ville (id_ville,libelle.
class VilleAdmin(admin.ModelAdmin):
    list_display = ['libelle']
    search_fields = ['libelle']

admin.site.register(Ville, VilleAdmin)

# Register your models here Ville (id_ville,libelle.)
class CommuneAdmin(admin.ModelAdmin):
    list_display = ['libelle']
    search_fields = ['libelle']

admin.site.register(Commune, CommuneAdmin)

# Register your models here Niveau_specialite (id_niveau_specialite,#id_niveau,#id_specialite)
class Niveau_specialiteAdmin(admin.ModelAdmin):
    list_display = ['niveau']
    search_fields = ['libelle']

admin.site.register(Niveau_Specialite, Niveau_specialiteAdmin)

# Register your models here. Etudiant (id_etudiant,,nom ,prenom,matricule,lieu_de_naissance,date_de_naissance,email,contact,#id_univ#id_sex,#id_ufr,
# #id_filiere,#id_specialite,#id_niveau,#id_ville,
#id_commune)

class EtudiantAdmin(admin.ModelAdmin):
    list_display = ['name','prenom','matricule','n_cni','carte_etudiant','carte_cni','lieu_de_naissance','date_de_naissance','email','contact','universite','sexe','ufr','filiere','niveau','ville','commune','date']
    search_fields = ['name']
 
admin.site.register(Etudiant, EtudiantAdmin)





