from django.db import models
from django.utils.timezone import now
from .enums import Country, ProductType, Gender, Package, Fragrance
from django.core.validators import MinValueValidator


class TimestampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Brand(TimestampModel):
    """
    Represents a perfume brand in the store.
    
    Contains details about the brand including name, logo, country of origin,
    website, and description.
    """
    name = models.CharField(max_length=255, unique=True)
    logo = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=100, choices=Country.choices(), null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Product(TimestampModel):
    """
    Represents a perfume product in the store inventory.
    
    Contains details about the perfume including brand, fragrance notes,
    pricing, and other product specifications.
    """
    name = models.CharField(max_length=255, null=False, blank=False, unique=True, db_index=True, help_text="Unique name identifier for the product")
    title = models.CharField(max_length=255, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True, related_name="products")
    category = models.CharField(max_length=255, choices=ProductType.choices(), null=True, db_index=True)
    volume = models.IntegerField(default=0, null=True, help_text="ml.", validators=[MinValueValidator(0)])
    package = models.CharField(max_length=255, choices=Package.choices(), null=True)
    top_note = models.CharField(max_length=255, choices=Fragrance.choices(), null=True)
    middle_note = models.CharField(max_length=255, choices=Fragrance.choices(), null=True)
    base_note = models.CharField(max_length=255, choices=Fragrance.choices(), null=True)
    price = models.IntegerField(default=0, null=False, blank=True, validators=[MinValueValidator(0)])
    gender = models.CharField(max_length=255, choices=Gender.choices(), null=True, db_index=True)
    comment = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    active =models.BooleanField(default=True, null=False, blank=False, db_index=True, help_text="Whether this product is available for purchase")

    class Meta:
        abstract = False
        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

