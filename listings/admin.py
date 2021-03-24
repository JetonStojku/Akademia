from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    # -- 2
    # list_display_links = ('id', 'title')
    # -- 3
    # list_filter = ('realtor',)
    # -- 4
    # list_editable = ('is_published',)
    # -- 5
    # search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    # -- 6
    # list_per_page = 25


admin.site.register(Listing, ListingAdmin)
