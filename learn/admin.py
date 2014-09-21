from django.contrib import admin

from .models import Token
from utils import csv_response, generate_table


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['code', 'added', 'redeemed']
    list_filter = ['added', 'redeemed']
    search_fields = ['code']

    actions = [
        'download_report',
    ]

    def download_report(self, request, queryset):
        """Allows downloading a payment contract report from the admin site."""
        return csv_response('Tokens',
                            generate_table(self.list_display, queryset))
