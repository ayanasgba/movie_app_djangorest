# Generated by Django 4.2.7 on 2023-12-10 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_review_movierev'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='movieRev',
        ),
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movie_app.movie'),
        ),
    ]
