# Generated by Django 3.1.8 on 2021-07-01 14:38

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_articlepage_newsnewsletterpage_pagetag'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='sidebar',
            field=wagtail.fields.StreamField([('sidebar', wagtail.blocks.StreamBlock([('sidebar_title', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock())])), ('sidebar_image_text', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]))], required=False))], default=False),
            preserve_default=False,
        ),
    ]
