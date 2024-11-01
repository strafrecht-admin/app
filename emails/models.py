from birdsong.blocks import DefaultBlocks
from birdsong.models import Campaign
from wagtail.admin.panels.field_panel import FieldPanel
from wagtail.fields import StreamField


# Create your models here.
class NewsletterEmail(Campaign):
    body = StreamField(DefaultBlocks(), use_json_field=True)

    panels = Campaign.panels + [
        FieldPanel('body'),
    ]


# Create your models here.
class LSHNewsletter(Campaign):
    body = StreamField(DefaultBlocks(), use_json_field=True)

    panels = Campaign.panels + [
        FieldPanel('body'),
    ]
