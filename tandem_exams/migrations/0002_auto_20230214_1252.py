# Generated by Django 3.2.5 on 2023-02-14 11:52

from django.db import migrations, models
import tandem_exams.models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tandem_exams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examsolution',
            name='correction_sheet',
        ),
        migrations.AddField(
            model_name='tandemexam',
            name='proof_sheet',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Korrekturbogen'),
        ),
        migrations.AddField(
            model_name='tandemexam',
            name='sample_solution',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Musterlösung'),
        ),
        migrations.AlterField(
            model_name='examsolution',
            name='correction',
            field=models.FileField(blank=True, null=True, upload_to=tandem_exams.models.ExamSolution.correction_target, verbose_name='Korrektur'),
        ),
        migrations.AlterField(
            model_name='examsolution',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=tandem_exams.models.ExamSolution.file_target, verbose_name='Gutachten'),
        ),
        migrations.AlterField(
            model_name='tandemexam',
            name='description',
            field=wagtail.fields.RichTextField(default=''),
        ),
    ]
