from django import forms
from .models import Etudiant

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ( 'name', 'prenom', 'matricule', 'n_cni', 
                  'carte_etudiant', 'carte_cni','lieu_de_naissance','date_de_naissance', 'email', 
                  'contact','universite', 'sexe','ufr',            
                  'filiere','specialite','niveau', 'ville', 'commune'
                  )
        Widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Nom'}),
            'prenom' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Prénom'}),
            'matricule' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Matricule'}),
            'n_cni' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'n°_cni'}),
            'carte_etudiant' : forms.FileInput(attrs={'class' : 'form-control', 'placeholder' : 'Carte_etudiant'}),
            'carte_cni' : forms.FileInput(attrs={'class' : 'form-control', 'placeholder' : 'Carte_cni'}),
            'lieu_de_naissance' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Lieu_de_naissance'}),
            'date_de_naissance' : forms.DateInput(attrs={'class' : 'form-control', 'placeholder' : 'Date_de_naissance'}),
            'email' : forms.EmailInput(attrs={'class' : 'form-control', 'placeholder' : 'Email'}),
            'contact' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Contact'}),
            'universite' : forms.Select(attrs={'class' : 'form-control', 'placeholder' : 'Universite'}),
            'sexe' : forms.Select(attrs={'class' : 'form-control', 'placeholder' : 'Sexe'}),
            'ufr' : forms.Select(attrs={'class' : 'form-control', 'placeholder' : 'UFR'}),
            'filiere' : forms.Select(attrs={'class' : 'form-control', 'placeholder' : 'Filiere'}),
            'specialite' : forms.Select(attrs={'class' : 'form-control', 'placeholder' : 'Specialite'}),
            'niveau' : forms.Select(attrs={'class' : 'form-control', 'placeholder' : 'Niveau'}),
            'ville' : forms.Select(attrs={'class' : 'form-control', 'placeholder' : 'Ville'}),
            'commune' : forms.Select(attrs={'class' : 'form-control', 'placeholder' : 'Commune'}),
        }