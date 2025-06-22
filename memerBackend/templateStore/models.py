from django.db import models
from PIL import Image

# Create your models here.
class MemeTemplate(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='templates/')
    width = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    box_count = models.PositiveIntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image and (not self.width or not self.height):
            img = Image.open(self.image.path)
            self.width = img.width
            self.height = img.height
            super().save(update_fields=["width", "height"])
            