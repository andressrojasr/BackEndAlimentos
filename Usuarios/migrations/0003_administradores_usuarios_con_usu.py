# Generated by Django 4.2.2 on 2023-06-06 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0002_alimentos_tip_alimentos_registro_alimentos_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ADMINISTRADORES',
            fields=[
                ('Usu_Adm', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Con_Adm', models.CharField(max_length=25)),
                ('Cor_Adm', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='usuarios',
            name='Con_Usu',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
