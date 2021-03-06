# Generated by Django 3.0rc1 on 2020-05-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('VETERINARY', 'VETERINARY'), ('SURGERY', 'SURGERY'), ('CT SCAN', 'CT SCAN'), ('STERILIZATION AND DISINFECTION', 'STERILIZATION AND DISINFECTION'), ('LABORATORY FURNITURE', 'LABORATORY FURNITURE'), ('ANESTHESIOLOGY AND RESUSCITATION', 'ANESTHESIOLOGY AND RESUSCITATION'), ('ULTRASOUND DIAGNOSTICS', 'ULTRASOUND DIAGNOSTICS'), ('METAL FURNITURE', 'METAL FURNITURE'), ('PHYSIOTHERAPY', 'PHYSIOTHERAPY'), ('ENDOSCOPY', 'ENDOSCOPY'), ('ENDOCRINOLOGY', 'ENDOCRINOLOGY'), ('CONSUMABLES', 'CONSUMABLES'), ('DENTISTRY', 'DENTISTRY'), ('ANGIOLOGY AND MRI', 'ANGIOLOGY AND MRI'), ('NEONATOLOGY', 'NEONATOLOGY'), ('FUNCTIONAL DIAGNOSTICS', 'FUNCTIONAL DIAGNOSTICS'), ('MEDICAL FURNITURE', 'MEDICAL FURNITURE')], default='SURGERY', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
