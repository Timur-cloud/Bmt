from django.db import models
from PIL import Image
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Product(models.Model):
    ANGIOLOGYANDMRI ='ANGIOLOGY AND MRI'
    ANESTHESIOLOGYANDRESUSCITATION ='ANESTHESIOLOGY AND RESUSCITATION'
    VETERINARY ='VETERINARY'
    CTSCAN ='CT SCAN'
    LABORATORYFURNITURE ='LABORATORY FURNITURE'
    MEDICALFURNITURE ='MEDICAL FURNITURE'
    METALFURNITURE ='METAL FURNITURE'
    NEONATOLOGY ='NEONATOLOGY'
    CONSUMABLES ='CONSUMABLES'
    STERILIZATIONANDDISINFECTION ='STERILIZATION AND DISINFECTION'
    DENTISTRY ='DENTISTRY'
    ULTRASOUNDDIAGNOSTICS ='ULTRASOUND DIAGNOSTICS'
    PHYSIOTHERAPY ='PHYSIOTHERAPY'
    FUNCTIONALDIAGNOSTICS ='FUNCTIONAL DIAGNOSTICS'
    SURGERY ='SURGERY'
    ENDOCRINOLOGY ='ENDOCRINOLOGY'
    ENDOSCOPY ='ENDOSCOPY'

    CHOICE_GROUP ={
        (ANGIOLOGYANDMRI,'ANGIOLOGY AND MRI'),
        (ANESTHESIOLOGYANDRESUSCITATION, 'ANESTHESIOLOGY AND RESUSCITATION'),
        (VETERINARY, 'VETERINARY'),
        (CTSCAN, 'CT SCAN'),
        (LABORATORYFURNITURE, 'LABORATORY FURNITURE'),
        (MEDICALFURNITURE, 'MEDICAL FURNITURE'),
        (METALFURNITURE, 'METAL FURNITURE'),
        (NEONATOLOGY, 'NEONATOLOGY'),
        (CONSUMABLES, 'CONSUMABLES'),
        (STERILIZATIONANDDISINFECTION, 'STERILIZATION AND DISINFECTION'),
        (DENTISTRY, 'DENTISTRY'),
        (ULTRASOUNDDIAGNOSTICS, 'ULTRASOUND DIAGNOSTICS'),
        (PHYSIOTHERAPY, 'PHYSIOTHERAPY'),
        (FUNCTIONALDIAGNOSTICS, 'FUNCTIONAL DIAGNOSTICS'),
        (SURGERY, 'SURGERY'),
        (ENDOCRINOLOGY, 'ENDOCRINOLOGY'),
        (ENDOSCOPY, 'ENDOSCOPY'),
    }

    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField(default ='1')
    name = models.CharField(max_length=100)
    description = models.TextField()
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    availability = models.BooleanField()
    group = models.CharField(max_length=50, choices=CHOICE_GROUP, default=SURGERY)
    img = models.ImageField(default='no_image.png', upload_to='product_image')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
