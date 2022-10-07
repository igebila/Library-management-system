# Generated by Django 4.1 on 2022-10-07 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_alter_book_genre_alter_book_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='total_books_due',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('History', 'History'), ('Engineering', 'Engineering'), ('Medcine', 'Medcine'), ('Journalism', 'Journalism'), ('Educational', 'Educational'), ('Fiction', 'Fiction'), ('Religious', 'Religious'), ('Kids', 'Kids')], default='Educational', max_length=15),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('Others', 'Others'), ('Somali', 'Somali'), ('English', 'English'), ('Arabic', 'Arabic'), ('Afan-Oromo', 'Afan-Oromo'), ('Amharic', 'Amharic')], default='English', max_length=15),
        ),
    ]