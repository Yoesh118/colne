# Generated by Django 2.2.28 on 2022-06-10 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='name',
            field=models.TextField(),
        ),
    ]
