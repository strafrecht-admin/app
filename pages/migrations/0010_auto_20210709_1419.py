# Generated by Django 3.1.8 on 2021-07-09 14:19

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail_color_panel.blocks
import wagtailmodelchooser.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_genericpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsnewsletterpage',
            name='content',
            field=wagtail.fields.StreamField([('content', wagtail.blocks.StreamBlock([('richtext', wagtail.blocks.RichTextBlock()), ('newsletter_list_block', wagtail.blocks.StructBlock([]))]))], default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsnewsletterpage',
            name='sidebar',
            field=wagtail.fields.StreamField([('sidebar', wagtail.blocks.StreamBlock([('sidebar_title', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock())])), ('sidebar_image_text', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('sidebar_poll', wagtail.blocks.StructBlock([('poll', wagtailmodelchooser.blocks.ModelChooserBlock(target_model='wagtailpolls.poll'))]))], required=False))], default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='sidebar',
            field=wagtail.fields.StreamField([('sidebar', wagtail.blocks.StreamBlock([('sidebar_title', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock())])), ('sidebar_image_text', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('sidebar_poll', wagtail.blocks.StructBlock([('poll', wagtailmodelchooser.blocks.ModelChooserBlock(target_model='wagtailpolls.poll'))]))], required=False))]),
        ),
        migrations.AlterField(
            model_name='articlespage',
            name='sidebar',
            field=wagtail.fields.StreamField([('sidebar', wagtail.blocks.StreamBlock([('sidebar_title', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock())])), ('sidebar_image_text', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('sidebar_poll', wagtail.blocks.StructBlock([('poll', wagtailmodelchooser.blocks.ModelChooserBlock(target_model='wagtailpolls.poll'))]))], required=False))]),
        ),
        migrations.AlterField(
            model_name='evaluationspage',
            name='sidebar',
            field=wagtail.fields.StreamField([('sidebar', wagtail.blocks.StreamBlock([('sidebar_title', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock())])), ('sidebar_image_text', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('sidebar_poll', wagtail.blocks.StructBlock([('poll', wagtailmodelchooser.blocks.ModelChooserBlock(target_model='wagtailpolls.poll'))]))], required=False))]),
        ),
        migrations.AlterField(
            model_name='genericpage',
            name='sidebar',
            field=wagtail.fields.StreamField([('sidebar', wagtail.blocks.StreamBlock([('sidebar_title', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock())])), ('sidebar_simple', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock())])), ('sidebar_border', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock())])), ('sidebar_image_text', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('sidebar_calendar_text', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock()), ('calendar', wagtail.blocks.DateBlock(format='%Y-%m-%d'))])), ('sidebar_header', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('color', wagtail_color_panel.blocks.NativeColorBlock('color', default='#333d44')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('content', wagtail.blocks.RichTextBlock(required=False))])), ('sidebar_poll', wagtail.blocks.StructBlock([('poll', wagtailmodelchooser.blocks.ModelChooserBlock(target_model='wagtailpolls.poll'))])), ('sidebar_subscribe', wagtail.blocks.StructBlock([])), ('sidebar_event', wagtail.blocks.StructBlock([]))], required=False))]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='sidebar',
            field=wagtail.fields.StreamField([('sidebar', wagtail.blocks.StreamBlock([('sidebar_title', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock())])), ('sidebar_simple', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock())])), ('sidebar_border', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock())])), ('sidebar_image_text', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('sidebar_calendar_text', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock()), ('calendar', wagtail.blocks.DateBlock(format='%Y-%m-%d'))])), ('sidebar_header', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('color', wagtail_color_panel.blocks.NativeColorBlock('color', default='#333d44')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('content', wagtail.blocks.RichTextBlock(required=False))])), ('sidebar_poll', wagtail.blocks.StructBlock([('poll', wagtailmodelchooser.blocks.ModelChooserBlock(target_model='wagtailpolls.poll'))])), ('sidebar_subscribe', wagtail.blocks.StructBlock([])), ('sidebar_event', wagtail.blocks.StructBlock([]))], required=False))]),
        ),
    ]
