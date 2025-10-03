from django.db import models

class Images(models.Model):
	image = models.ImageField(null=True,blank=True,upload_to="pics/")