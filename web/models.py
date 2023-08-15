from django.db import models
from django.utils import timezone

# Create your models here.
class Universite(models.Model):
    code = models.CharField('Code', unique=True, max_length = 40)
    name = models.CharField('Nom', unique=True, max_length = 150)
    email = models.EmailField('Email', unique=True, max_length = 100)
    contact = models.CharField('Contact',unique=True, max_length = 70)

    class Meta:
     verbose_name_plural = 'Universités'
    def __str__(self):
        return self.name

# Create your models here.
class Sexe(models.Model):
    libelle = models.CharField('Libellé', max_length = 20)

    class Meta:
     verbose_name_plural = 'Sexe'
    def __str__(self):
        return self.libelle

# Create your models here.
class Ufr(models.Model):
    code = models.CharField('Code', unique=True, max_length = 45)
    name = models.CharField('Nom', unique=True, max_length = 150)
    email = models.EmailField('Email', unique=True, max_length = 100)
    contact = models.CharField('Contact',unique=True, max_length = 70)
    universite = models.ForeignKey(Universite,verbose_name = 'Université', on_delete = models.CASCADE)

    class Meta:
     verbose_name_plural = 'UFR'
    def __str__(self):
        return self.name

# Create your models here Filiere (id_filiere,code,libelle,email,contact,#id_ufr).
class Filiere(models.Model):
    code = models.CharField('Code', unique=True, max_length = 45)
    name = models.CharField('Nom', unique=True, max_length = 150)
    email = models.EmailField('Email', unique=True, max_length = 100)
    contact = models.CharField('Contact',unique=True, max_length = 70)
    ufr = models.ForeignKey(Ufr,verbose_name = 'Ufr', on_delete = models.CASCADE)

    class Meta:
     verbose_name_plural = 'Filière'
    def __str__(self):
        return self.name
    
# Create your models here Specialite (id_specialite,libelle,#id_ufr).  filiere = models.ForeignKey(Filiere, verbose_name = "Filière", NULL= True, blank = True, on_delete = models.CASCADE)
class Specialite(models.Model):
    libelle = models.CharField('Libellé', unique=True, max_length = 70)
    filiere = models.ForeignKey(Filiere,verbose_name = 'Filière', on_delete = models.CASCADE)

    class Meta:
     verbose_name_plural = 'Specialité'
    def __str__(self):
        return self.libelle
    
    
# Create your models here Niveau (id_niveau,libelle).
class Niveau(models.Model):
    libelle = models.CharField('Libelle', unique=True, max_length = 60)

    class Meta:
     verbose_name_plural = 'Niveau'
    def __str__(self):
        return self.libelle
    
# Create your models here Ville (id_ville,libelle.
class Ville(models.Model):
    libelle = models.CharField('Libelle', unique=True, max_length = 100)

    class Meta:
     verbose_name_plural = 'Ville'
    def __str__(self):
        return self.libelle
    
# Create your models here Commune (id_commune,#id_ville,libelle)
class Commune(models.Model):
    libelle = models.CharField('Libelle', unique=True, max_length = 100)
    ville = models.ForeignKey(Ville,verbose_name = 'Ville', on_delete = models.CASCADE)

    class Meta:
     verbose_name_plural = 'Commune'
    def __str__(self):
        return self.libelle
    
#Create your models here Niveau_specialite (id_niveau_specialite,#id_niveau,#id_specialite)
class Niveau_Specialite(models.Model):
    niveau = models.ForeignKey(Niveau,verbose_name = 'Niveau', on_delete = models.CASCADE)

    class Meta:
     verbose_name_plural = 'Niveau_Specialite'
    def __str__(self):
        return self.Niveau

#Create your models here Etudiant (id_etudiant,,nom ,prenom,matricule,lieu_de_naissance,date_de_naissance,email,contact,#id_univ#id_sex,#id_ufr,
# #id_filiere,#id_specialite,#id_niveau,#id_ville,
#id_commune)

class Etudiant(models.Model):
    name = models.CharField('Name', max_length = 100)
    prenom = models.CharField('Prenom', max_length = 150)
    matricule = models.CharField('Matricule', max_length = 150)
    n_cni = models.CharField('N°CNI',unique=True, null=True, blank=True, max_length = 150)
    carte_etudiant = models.FileField('Carte d\'étudiant',upload_to = 'CarteEtudiant',null=True, blank=True, max_length = 150)
    carte_cni = models.FileField('Carte CNI', upload_to = 'cni',null=True, blank=True, max_length = 150)
    lieu_de_naissance = models.CharField('Lieu de naissance', max_length = 150)
    date_de_naissance = models.DateField('Date de naissance', max_length = 150)
    email = models.EmailField('Email', unique=True, max_length = 100)
    contact = models.CharField('Contact',unique=True, max_length = 70)
    universite = models.ForeignKey(Universite,verbose_name = 'Universite', on_delete = models.CASCADE)

    sexe = models.ForeignKey(Sexe,verbose_name = 'Sexe', on_delete = models.CASCADE)
    ufr = models.ForeignKey(Ufr,verbose_name = 'Ufr', on_delete = models.CASCADE)
    filiere = models.ForeignKey(Filiere,verbose_name = 'Filiere', null=True, blank=True, on_delete = models.CASCADE)
    specialite = models.ForeignKey(Specialite,verbose_name = 'Spécialité', null=True, blank=True, on_delete = models.CASCADE)
    niveau = models.ForeignKey(Niveau,verbose_name = 'Niveau', on_delete = models.CASCADE)
    ville = models.ForeignKey(Ville,verbose_name = 'Ville', on_delete = models.CASCADE)
    commune = models.ForeignKey(Commune,verbose_name = 'Commune', on_delete = models.CASCADE)
    date = models.DateTimeField('Date d\'identification', max_length = 150, default = timezone.now)

    class Meta:
     verbose_name_plural = 'Etudiant'
    def __str__(self):
        return self.name
