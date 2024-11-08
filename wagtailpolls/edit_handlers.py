from django.template.loader import render_to_string
from django.utils.encoding import force_str
from django.utils.safestring import mark_safe
from wagtail.admin.panels.field_panel import FieldPanel

from .widgets import AdminPollChooser


class BasePollChooserPanel(FieldPanel):
    object_type_name = 'item'

    _target_model = None

    @classmethod
    def widget_overrides(cls):
        return {cls.field_name: AdminPollChooser(model=cls.target_model())}

    @classmethod
    def target_model(cls):
        if cls._target_model is None:
            cls._target_model = cls.model._meta.get_field(cls.field_name).rel.model

        return cls._target_model

    def render_as_field(self):
        instance_obj = self.get_chosen_item()
        return mark_safe(render_to_string(self.field_template, {
            'field': self.bound_field,
            self.object_type_name: instance_obj,
            'snippet_type_name': self.get_snippet_type_name(),
        }))

    @classmethod
    def get_snippet_type_name(cls):
        return force_str(cls.target_model()._meta.verbose_name)


class PollChooserPanel(BasePollChooserPanel):
    object_type_name = 'item'

    def widget_overrides(self):
        return {self.field_name: AdminPollChooser(model=self.target_model)}

    def render_as_field(self):
        instance_obj = self.get_chosen_item()
        return mark_safe(render_to_string(self.field_template, {
            'field': self.bound_field,
            self.object_type_name: instance_obj,
        }))

    def on_model_bound(self):
        super().on_model_bound()
        self.target_model = self.db_field.remote_field.model

#class PollChooserPanel(object):
#    def __init__(self, field_name, snippet_type=None):
#        self.field_name = field_name
#        self.snippet_type = snippet_type
#
#    def bind_to_model(self, model):
#        return type(str('_PollChooserPanel'), (BasePollChooserPanel,), {
#            'model': model,
#            'field_name': self.field_name,
#            'snippet_type': self.snippet_type,
#        })
