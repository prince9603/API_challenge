from django.contrib.auth.models import User, AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    LISTE_DROITS=(
        ('Utilisateur','Utilisateur'),
        ("Administrateur","Administrateur"),
    )
    pseudo=models.CharField(max_length=100)
    droit=models.CharField(max_length=15,choices=LISTE_DROITS)


