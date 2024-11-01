# Generated by Django 3.2.5 on 2023-02-14 11:52

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailmodelchooser.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0036_auto_20230203_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='sidebar',
            field=wagtail.fields.StreamField([('sidebar_title', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock())], label='Grau unterlegte Überschrift')), ('sidebar_simple', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock())], label='Schlichter Text')), ('sidebar_image_text', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], label='Bild links, Text rechts')), ('sidebar_poll', wagtail.blocks.StructBlock([('poll', wagtailmodelchooser.blocks.ModelChooserBlock(target_model='wagtailpolls.poll'))], label='Abstimmung')), ('sidebar_search', wagtail.blocks.StructBlock([], label='Suchfeld'))], blank=True, verbose_name='Seitenleiste'),
        ),
        migrations.AlterField(
            model_name='articlespage',
            name='sidebar',
            field=wagtail.fields.StreamField([('sidebar_title', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock())], label='Grau unterlegte Überschrift')), ('sidebar_simple', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock())], label='Schlichter Text')), ('sidebar_image_text', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], label='Bild links, Text rechts')), ('sidebar_poll', wagtail.blocks.StructBlock([('poll', wagtailmodelchooser.blocks.ModelChooserBlock(target_model='wagtailpolls.poll'))], label='Abstimmung')), ('sidebar_search', wagtail.blocks.StructBlock([], label='Suchfeld'))], verbose_name='Seitenleiste'),
        ),
        migrations.AlterField(
            model_name='evaluationspage',
            name='sidebar',
            field=wagtail.fields.StreamField([('sidebar', wagtail.blocks.StreamBlock([('sidebar_title', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock())], label='Grau unterlegte Überschrift')), ('sidebar_simple', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock())], label='Schlichter Text')), ('sidebar_image_text', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], label='Bild links, Text rechts')), ('sidebar_poll', wagtail.blocks.StructBlock([('poll', wagtailmodelchooser.blocks.ModelChooserBlock(target_model='wagtailpolls.poll'))], label='Abstimmung')), ('sidebar_search', wagtail.blocks.StructBlock([], label='Suchfeld'))], label='Seitenleiste', required=False))], verbose_name='Seitenleiste'),
        ),
        migrations.AlterField(
            model_name='genericpage',
            name='content',
            field=wagtail.fields.StreamField([('content', wagtail.blocks.StreamBlock([('richtext', wagtail.blocks.RichTextBlock(label='Formatierter Text')), ('collapse_block', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(required=True)), ('content', wagtail.blocks.RichTextBlock(label='Formatierter Text'))], label='Ausklappbares Element')), ('flipcard_block', wagtail.blocks.StructBlock([('front', wagtail.blocks.RichTextBlock(label='Vorderseite')), ('back', wagtail.blocks.RichTextBlock(label='Rückseite'))], label='Flipcard')), ('home_news_block', wagtail.blocks.StructBlock([], label='Vier letzte News-Beiträge')), ('home_jurcoach_block', wagtail.blocks.StructBlock([], label='Jurcoach-Startseiten-Widget')), ('table', wagtail.contrib.table_block.blocks.TableBlock())], label='Hauptspalte'))], verbose_name='Hauptspalte'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('content', wagtail.blocks.StreamBlock([('richtext', wagtail.blocks.RichTextBlock(label='Formatierter Text')), ('collapse_block', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(required=True)), ('content', wagtail.blocks.RichTextBlock(label='Formatierter Text'))], label='Ausklappbares Element')), ('flipcard_block', wagtail.blocks.StructBlock([('front', wagtail.blocks.RichTextBlock(label='Vorderseite')), ('back', wagtail.blocks.RichTextBlock(label='Rückseite'))], label='Flipcard')), ('home_news_block', wagtail.blocks.StructBlock([], label='Vier letzte News-Beiträge')), ('home_jurcoach_block', wagtail.blocks.StructBlock([], label='Jurcoach-Startseiten-Widget')), ('table', wagtail.contrib.table_block.blocks.TableBlock())], label='Hauptspalte'))], verbose_name='Hauptspalte'),
        ),
    ]
