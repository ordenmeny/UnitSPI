from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from events.models import EventModel


class CustomUserAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_display_links = ('first_name', 'last_name', 'email')
    # list_editable = ('chat_id', )

    fields_to_set = ('email', 'first_name', 'last_name',)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": fields_to_set}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


class CustomEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'time', 'location', 'description', 'tags')
    list_display_links = ('title', 'time', 'location', 'description', 'tags')
    # list_editable = ('title', )


admin.site.register(get_user_model(), CustomUserAdmin)
admin.site.register(EventModel, CustomEventAdmin)
