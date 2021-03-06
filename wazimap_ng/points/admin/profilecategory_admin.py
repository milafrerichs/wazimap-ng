from django.contrib.gis import admin
from django import forms

from wazimap_ng.general.admin.admin_base import BaseAdminModel
from wazimap_ng.general.services.permissions import assign_perms_to_group
from wazimap_ng.general.admin import filters

from .. import models

from icon_picker_widget.widgets import IconPickerWidget


class ProfileCategoryAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['icon'].widget = IconPickerWidget()


@admin.register(models.ProfileCategory)
class ProfileCategoryAdmin(BaseAdminModel):
    list_display = ("label", "theme", "category", "profile")
    list_filter = (filters.ProfileFilter, filters.ThemeFilter, filters.CollectionFilter)

    fieldsets = (
        ("Database fields (can't change after being created)", {
            'fields': ('profile', 'theme', 'category',)
        }),
        ("Permissions", {
            'fields': ('permission_type', )

        }),
        ("Profile Collection Icon", {
            'fields': ('icon', )

        }),
        ("Point Collection description fields", {
          'fields': ('label', 'description',)
        }),
    )
    form = ProfileCategoryAdminForm
    search_fields = ("label", )

    class Media:
        css = {
             'all': ('/static/css/admin-custom.css',)
        }

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ("profile", "category", ) + self.readonly_fields
        return self.readonly_fields

    def save_model(self, request, obj, form, change):
        is_new = obj.pk == None and change == False
        is_profile_updated = change and "profile" in form.changed_data

        super().save_model(request, obj, form, change)
        if is_new or is_profile_updated:
            assign_perms_to_group(obj.profile.name, obj, is_profile_updated)
        return obj