from django.contrib import admin
from cars.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    ordering = ('front_of',)
    list_display = ('car', 'color',)
    list_per_page = 20
    list_filter = ['color']
    readonly_fields = ('created', 'lastUpdated',)
    search_fields = ['car', ]
    fieldsets = (
            ('Car Details', {
                'fields': ('car', 'color', 'front_of', 'created', 'lastUpdated')
            }),
        )


admin.site.site_header = 'Car CRUD System'