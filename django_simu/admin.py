from django.contrib import admin
from .models import Service, AboutUs, AboutUsListItem

admin.site.register(
    [
        Service,
        AboutUs,
        AboutUsListItem
    ]
)
