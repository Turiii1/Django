# Generated by Django 5.0.4 on 2024-04-16 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='item_desct',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='item_images',
            field=models.ImageField(blank=True, null=True, upload_to='category/'),
        ),
    ]
