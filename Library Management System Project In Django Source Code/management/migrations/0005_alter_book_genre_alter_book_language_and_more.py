# Generated by Django 4.1 on 2022-10-07 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_book_timestamp_alter_book_genre_alter_book_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Engineering', 'Engineering'), ('Medcine', 'Medcine'), ('Kids', 'Kids'), ('Educational', 'Educational'), ('Journalism', 'Journalism'), ('History', 'History'), ('Religious', 'Religious'), ('Fiction', 'Fiction')], default='Educational', max_length=15),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('Afan-Oromo', 'Afan-Oromo'), ('Others', 'Others'), ('English', 'English'), ('Somali', 'Somali'), ('Arabic', 'Arabic'), ('Amharic', 'Amharic')], default='English', max_length=15),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
