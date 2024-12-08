from django.contrib import admin
from .models import WebsiteFrontImage, WebsiteBlogImage, CatalogueLogo, CatalogueImage

# Register your models here.
admin.site.register(WebsiteFrontImage)
admin.site.register(WebsiteBlogImage)
admin.site.register(CatalogueLogo)
admin.site.register(CatalogueImage)
