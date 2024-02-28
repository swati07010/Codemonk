from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import SearchData

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'name', 'dob', 'is_staff', 'created_at', 'modified_at']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'dob')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_at', 'modified_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'dob', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    search_fields = ('email', 'name')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)


class SearchDataAdmin(admin.ModelAdmin):
    list_display = ('paragraph_preview', 'word', 'created_at')
    list_filter = ('created_at', )
    search_fields = ('paragraph', 'word')
    readonly_fields = ('created_at', )

    def paragraph_preview(self, obj):
        return obj.paragraph[:50] + '...' if len(obj.paragraph) > 50 else obj.paragraph
    paragraph_preview.short_description = 'Paragraph Preview'

admin.site.register(SearchData, SearchDataAdmin)
