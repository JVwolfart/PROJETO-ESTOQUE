# Generated by Django 4.0.3 on 2022-04-20 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0009_alter_produto_estoque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/'),
        ),
    ]