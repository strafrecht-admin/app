from birdsong.models import Contact
from birdsong.options import CampaignAdmin
from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

from .filters import ContactFilter
from .models import LSHNewsletter


class ContactAdmin(ModelAdmin):
    model = Contact
    menu_label = 'Abonnenten'
    menu_icon = 'user'
    # list_diplay = ('email')


class LSHNewsletterAdmin(CampaignAdmin):
    model = LSHNewsletter
    menu_label = 'LSH'
    menu_icon = 'mail'
    contact_class = Contact
    contact_filter_class = ContactFilter


@modeladmin_register
class NewsletterMenuAdmin(ModelAdminGroup):
    menu_label = 'Newsletter'
    menu_icon = 'folder'
    items = (LSHNewsletterAdmin, ContactAdmin)
