# Generated by Django 4.1.1 on 2022-10-07 22:57

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_service_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Contenido'),
        ),
    ]
