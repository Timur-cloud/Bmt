# Generated by Django 3.0.7 on 2020-06-09 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20200608_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='model',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('ANESTHESIOLOGY AND RESUSCITATION', 'ANESTHESIOLOGY AND RESUSCITATION'), ('LABORATORY FURNITURE', 'LABORATORY FURNITURE'), ('VETERINARY', 'VETERINARY'), ('CONSUMABLES', 'CONSUMABLES'), ('STERILIZATION AND DISINFECTION', 'STERILIZATION AND DISINFECTION'), ('ULTRASOUND DIAGNOSTICS', 'ULTRASOUND DIAGNOSTICS'), ('ANGIOLOGY AND MRI', 'ANGIOLOGY AND MRI'), ('METAL FURNITURE', 'METAL FURNITURE'), ('MEDICAL FURNITURE', 'MEDICAL FURNITURE'), ('NEONATOLOGY', 'NEONATOLOGY'), ('FUNCTIONAL DIAGNOSTICS', 'FUNCTIONAL DIAGNOSTICS'), ('SURGERY', 'SURGERY'), ('ENDOCRINOLOGY', 'ENDOCRINOLOGY'), ('ENDOSCOPY', 'ENDOSCOPY'), ('CT SCAN', 'CT SCAN'), ('PHYSIOTHERAPY', 'PHYSIOTHERAPY'), ('DENTISTRY', 'DENTISTRY')], default='SURGERY', max_length=50),
        ),
    ]
