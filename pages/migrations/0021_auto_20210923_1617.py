# Generated by Django 3.2.5 on 2021-09-23 16:17

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_auto_20210820_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionpage',
            name='semester',
            field=models.CharField(blank=True, choices=[('ss-2022', 'Sommersemester 2022'), ('ws-2022', 'Wintersemester 2022'), ('ss-2021', 'Sommersemester 2021'), ('ws-2021', 'Wintersemester 2021'), ('ss-2020', 'Sommersemester 2020'), ('ws-2020', 'Wintersemester 2020'), ('ss-2019', 'Sommersemester 2019'), ('ws-2019', 'Wintersemester 2019'), ('ss-2018', 'Sommersemester 2018'), ('ws-2018', 'Sommersemester 2018'), ('ss-2017', 'Sommersemester 2017'), ('ws-2017', 'Wintersemester 2017'), ('ss-2016', 'Sommersemester 2016'), ('ws-2016', 'Wintersemester 2015'), ('ss-2015', 'Sommersemester 2015'), ('ws-2015', 'Wintersemester 2014'), ('ss-2014', 'Sommersemester 2014'), ('ws-2014', 'Wintersemester 2014'), ('ss-2013', 'Sommersemester 2013'), ('ws-2013', 'Wintersemester 2013'), ('ss-2012', 'Sommersemester 2012'), ('ws-2012', 'Wintersemester 2012'), ('ss-2011', 'Sommersemester 2011'), ('ws-2011', 'Wintersemester 2011'), ('ss-2010', 'Sommersemester 2010'), ('ws-2010', 'Wintersemester 2010'), ('ss-2009', 'Sommersemester 2009'), ('ws-2009', 'Wintersemester 2009'), ('ss-2008', 'Sommersemester 2008'), ('ws-2008', 'Wintersemester 2008'), ('ss-2007', 'Sommersemester 2007'), ('ws-2007', 'Wintersemester 2007'), ('ss-2006', 'Sommersemester 2006'), ('ws-2006', 'Wintersemester 2006'), ('ss-2005', 'Sommersemester 2005'), ('ws-2005', 'Wintersemester 2005'), ('ss-2004', 'Sommersemester 2004'), ('ws-2004', 'Wintersemester 2004')], max_length=255),
        ),
        migrations.AlterField(
            model_name='sessionspage',
            name='content',
            field=wagtail.fields.StreamField([('content', wagtail.blocks.StreamBlock([('richtext', wagtail.blocks.RichTextBlock()), ('semester_block', wagtail.blocks.StructBlock([('semester', wagtail.blocks.ChoiceBlock(choices=[('ss-2022', 'Sommersemester 2022'), ('ws-2022', 'Wintersemester 2022'), ('ss-2021', 'Sommersemester 2021'), ('ws-2021', 'Wintersemester 2021'), ('ss-2020', 'Sommersemester 2020'), ('ws-2020', 'Wintersemester 2020'), ('ss-2019', 'Sommersemester 2019'), ('ws-2019', 'Wintersemester 2019'), ('ss-2018', 'Sommersemester 2018'), ('ws-2018', 'Wintersemester 2018')], icon='calendar'))]))]))]),
        ),
    ]
