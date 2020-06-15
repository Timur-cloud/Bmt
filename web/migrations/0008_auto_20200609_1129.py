# Generated by Django 3.0.7 on 2020-06-09 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20200609_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('DENTISTRY', 'DENTISTRY'), ('ANESTHESIOLOGY AND RESUSCITATION', 'ANESTHESIOLOGY AND RESUSCITATION'), ('ENDOSCOPY', 'ENDOSCOPY'), ('CT SCAN', 'CT SCAN'), ('ENDOCRINOLOGY', 'ENDOCRINOLOGY'), ('PHYSIOTHERAPY', 'PHYSIOTHERAPY'), ('CONSUMABLES', 'CONSUMABLES'), ('ANGIOLOGY AND MRI', 'ANGIOLOGY AND MRI'), ('STERILIZATION AND DISINFECTION', 'STERILIZATION AND DISINFECTION'), ('METAL FURNITURE', 'METAL FURNITURE'), ('FUNCTIONAL DIAGNOSTICS', 'FUNCTIONAL DIAGNOSTICS'), ('ULTRASOUND DIAGNOSTICS', 'ULTRASOUND DIAGNOSTICS'), ('SURGERY', 'SURGERY'), ('VETERINARY', 'VETERINARY'), ('LABORATORY FURNITURE', 'LABORATORY FURNITURE'), ('NEONATOLOGY', 'NEONATOLOGY'), ('MEDICAL FURNITURE', 'MEDICAL FURNITURE')], default='SURGERY', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=100),
        ),
    ]