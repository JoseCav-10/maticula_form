# Generated by Django 5.1 on 2024-09-01 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('cidade', models.CharField(choices=[('Pereiro', 'Pe'), ('Pau dos Ferros', 'Pf'), ('Ereré', 'Er'), ('São Miguel', 'Sm')], default='', max_length=255)),
                ('curso', models.CharField(choices=[('informatica', 'informatica'), ('alimentos', 'alimentos'), ('apicultura', 'apicultura')], default='', max_length=30)),
            ],
        ),
    ]
