# Generated by Django 3.2.5 on 2021-10-14 16:03

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpolls', '0001_initial'),
        ('pages', '0024_auto_20210924_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='jurcoachpage',
            name='carousel_headline',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jurcoachpage',
            name='contribution_description',
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jurcoachpage',
            name='contribution_headline',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jurcoachpage',
            name='header_headline',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='jurcoachpage',
            name='header_slogan',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='jurcoachpage',
            name='intro_headline',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jurcoachpage',
            name='intro_text',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='jurcoachpage',
            name='poll',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailpolls.poll'),
        ),
        migrations.CreateModel(
            name='JurcoachFooter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('footeritem_headline', models.CharField(blank=True, max_length=200, null=True)),
                ('footeritem_text', wagtail.fields.RichTextField(blank=True, null=True)),
                ('footeritem_linktext', models.CharField(blank=True, max_length=200, null=True)),
                ('footeritem_linkurl', models.CharField(blank=True, max_length=200, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='jurcoachfooter', to='pages.jurcoachpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JurcoachCarousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('illustration', models.CharField(blank=True, choices=[('falltraining', 'Falltraining'), ('wiki', 'Problemfeld-Wiki'), ('mct', 'Multiple-Choice-Test'), ('klausurdatenbank', 'Klausurdatenbank'), ('rechtsprechung', 'Höchstrichterliche Rechtsprechung')], max_length=255)),
                ('carousel_description', wagtail.fields.RichTextField(blank=True, null=True)),
                ('carousel_link_text', models.CharField(blank=True, max_length=200, null=True)),
                ('carousel_link_url', models.CharField(blank=True, max_length=250, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='jurcoachcarousel', to='pages.jurcoachpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
