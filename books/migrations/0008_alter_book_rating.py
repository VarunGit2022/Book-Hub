# Generated by Django 4.0.6 on 2024-08-05 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_book_author_alter_book_cover_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.CharField(max_length=100, null=True),
        ),
    ]