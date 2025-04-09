from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Brand

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "website", "created", "updated")
    list_filter = ("country",)
    search_fields = ("name", "description")
    ordering = ("name",)
    
    def website_link(self, obj):
        if obj.website:
            return format_html('<a href="{}" target="_blank">{}</a>', obj.website, obj.website)
        return "-"
    website_link.short_description = "Website"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "category", "price", "gender", "volume", "active", "created")
    list_filter = ("active", "gender", "category", "brand")
    search_fields = ("name", "title", "description")
    ordering = ("-created",)
    readonly_fields = ("created", "updated")
    fieldsets = (
        (None, {
            "fields": ("name", "title", "brand", "active")
        }),
        ("Product Details", {
            "fields": ("category", "gender", "volume", "package", "price")
        }),
        ("Fragrance Notes", {
            "fields": ("top_note", "middle_note", "base_note")
        }),
        ("Additional Information", {
            "fields": ("description", "comment")
        }),
        ("Metadata", {
            "fields": ("created", "updated"),
            "classes": ("collapse",)
        })
    )
    list_per_page = 25
