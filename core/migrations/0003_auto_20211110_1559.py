# Generated by Django 3.2.5 on 2021-11-10 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerversion',
            name='question_version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.questionversion'),
        ),
        migrations.AlterField(
            model_name='questionversion',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.question'),
        ),
    ]
