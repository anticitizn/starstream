# Generated by Django 3.2.12 on 2022-03-27 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='image',
            field=models.FileField(default='/thumb.jpg', upload_to='uploads/images/'),
            preserve_default=False,
        ),
    ]
