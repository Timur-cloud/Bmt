# Generated by Django 3.0rc1 on 2020-04-24 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('availability', models.BooleanField()),
                ('group', models.CharField(choices=[('NEONATOLOGY', 'NEONATOLOGY'), ('ANGIOLOGY AND MRI', 'ANGIOLOGY AND MRI'), ('PHYSIOTHERAPY', 'PHYSIOTHERAPY'), ('LABORATORY FURNITURE', 'LABORATORY FURNITURE'), ('ENDOSCOPY', 'ENDOSCOPY'), ('CT SCAN', 'CT SCAN'), ('ULTRASOUND DIAGNOSTICS', 'ULTRASOUND DIAGNOSTICS'), ('DENTISTRY', 'DENTISTRY'), ('VETERINARY', 'VETERINARY'), ('ENDOCRINOLOGY', 'ENDOCRINOLOGY'), ('STERILIZATION AND DISINFECTION', 'STERILIZATION AND DISINFECTION'), ('CONSUMABLES', 'CONSUMABLES'), ('FUNCTIONAL DIAGNOSTICS', 'FUNCTIONAL DIAGNOSTICS'), ('SURGERY', 'SURGERY'), ('ANESTHESIOLOGY AND RESUSCITATION', 'ANESTHESIOLOGY AND RESUSCITATION'), ('MEDICAL FURNITURE', 'MEDICAL FURNITURE'), ('METAL FURNITURE', 'METAL FURNITURE')], default='SURGERY', max_length=50)),
                ('img', models.ImageField(default='no_image.png', upload_to='product_image')),
            ],
        ),
    ]
