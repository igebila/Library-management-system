# Generated by Django 4.1 on 2022-10-07 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_student_total_books_due_alter_book_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Fiction', 'Fiction'), ('History', 'History'), ('Educational', 'Educational'), ('Journalism', 'Journalism'), ('Kids', 'Kids'), ('Religious', 'Religious'), ('Engineering', 'Engineering'), ('Medcine', 'Medcine')], default='Educational', max_length=15),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('Amharic', 'Amharic'), ('Arabic', 'Arabic'), ('Others', 'Others'), ('Somali', 'Somali'), ('English', 'English'), ('Afan-Oromo', 'Afan-Oromo')], default='English', max_length=15),
        ),
    ]