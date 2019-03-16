# Generated by Django 2.1.7 on 2019-03-16 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lovelace', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opiniao',
            options={'verbose_name_plural': 'Opiniao'},
        ),
        migrations.AlterModelOptions(
            name='parceiras',
            options={'verbose_name_plural': 'Parceiras'},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name_plural': 'Usuario'},
        ),
        migrations.AlterModelOptions(
            name='votacao',
            options={'verbose_name_plural': 'Votacao'},
        ),
        migrations.AlterField(
            model_name='usuario',
            name='dt_nasc_usuario',
            field=models.DateField(verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email_usuario',
            field=models.EmailField(max_length=256, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome_usuario',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='senha_usuario',
            field=models.CharField(max_length=256, verbose_name='Senha'),
        ),
    ]
