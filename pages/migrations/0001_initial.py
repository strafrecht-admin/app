# Generated by Django 3.2.4 on 2021-06-24 12:58

from django.db import migrations, models
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField()),
                ('semester', models.CharField(blank=True, choices=[('2024_2', 'Wintersemester 2024/2025'), ('2024_1', 'Sommersemester 2024'), ('2023_2', 'Wintersemester 2023/2024'), ('2023_1', 'Sommersemester 2023'), ('2022_2', 'Wintersemester 2022/2023'), ('2022_1', 'Sommersemester 2022'), ('2021_2', 'Wintersemester 2021/2022'), ('2021_1', 'Sommersemester 2021'), ('2020_2', 'Wintersemester 2020/2021'), ('2020_1', 'Sommersemester 2020'), ('2019_2', 'Wintersemester 2019/2020'), ('2019_1', 'Sommersemester 2019'), ('2018_2', 'Wintersemester 2018/2019'), ('2018_1', 'Sommersemester 2018'), ('2017_2', 'Wintersemester 2017/2018'), ('2017_1', 'Sommersemester 2017'), ('2016_2', 'Wintersemester 2016/2017'), ('2016_1', 'Sommersemester 2016'), ('2015_2', 'Wintersemester 2015/2016'), ('2015_1', 'Sommersemester 2015'), ('2014_2', 'Wintersemester 2014/2015'), ('2014_1', 'Sommersemester 2014'), ('2013_2', 'Wintersemester 2013/2014'), ('2013_1', 'Sommersemester 2013'), ('2012_2', 'Wintersemester 2012/2013'), ('2012_1', 'Sommersemester 2012'), ('2011_2', 'Wintersemester 2011/2012'), ('2011_1', 'Sommersemester 2011'), ('2010_2', 'Wintersemester 2010/2011'), ('2010_1', 'Sommersemester 2010')], default='ss2021', max_length=255)),
                ('speaker', models.CharField(blank=True, max_length=255, null=True)),
                ('youtube_link', models.CharField(blank=True, max_length=500, null=True)),
                ('newsletter_link', models.CharField(blank=True, max_length=500, null=True)),
                ('type', models.CharField(blank=True, choices=[('tacheles', 'Tacheles'), ('sonstige', 'Sonstige')], default='tacheles', max_length=255)),
                ('description', wagtail.fields.RichTextField(blank=True)),
                ('speaker_description', wagtail.fields.RichTextField(blank=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('showmap', models.BooleanField(default=False)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lon', models.FloatField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('paragraphs', wagtail.fields.RichTextField(blank=True)),
                ('problems', wagtail.fields.RichTextField(blank=True)),
                ('sachverhalt_link', models.CharField(blank=True, max_length=255)),
                ('loesung_link', models.CharField(blank=True, max_length=255)),
                ('difficulty', models.CharField(blank=True, choices=[('beginner', 'Anfänger'), ('intermediate', 'Fortgeschrittene'), ('advanced', 'Examen')], max_length=255)),
                ('type', models.CharField(blank=True, choices=[('falltraining', 'Klausur im Falltraining'), ('exam', 'Examensklausur'), ('original-exam', 'Originalexamensklausur'), ('exercise', 'Übungsfall'), ('tutorial', 'AG-Fall')], max_length=255)),
            ],
            options={
                'verbose_name': 'Klausur',
                'verbose_name_plural': 'Klausuren',
            },
        ),
    ]
