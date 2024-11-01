from __future__ import unicode_literals, absolute_import

from django.conf.urls import include
from django.urls import reverse, re_path
from django.utils.translation import gettext_lazy as _
from wagtail import hooks
from wagtail.admin.menu import MenuItem

from . import urls


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        re_path(r'^polls/', include(urls)),
    ]


@hooks.register('construct_main_menu')
def construct_main_menu(request, menu_items):
    menu_items.append(
        MenuItem(_('Polls'), reverse('wagtailpolls_index'),
                 classnames='icon icon-group', order=250)
    )
