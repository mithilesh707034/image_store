from django.db import models

# Create your models here.
class WebsiteFrontImage(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="website_front_image")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Website Front Image {self.id}"

class WebsiteBlogImage(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="website_blog_image")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Website Blog Image {self.id}"

class CatalogueLogo(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="catalogue_logo")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Catalogue Logo {self.id}"

class CatalogueImage(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="catalogue_image")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Catalogue Image {self.id}"
