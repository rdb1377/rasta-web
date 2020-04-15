from django.db import models
from ckeditor.fields import RichTextField
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

class Event(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    poster = models.ImageField(upload_to='event_posters/', null=True, blank=True) #todo false
    summary = models.TextField(null=False, blank=False)
    description = RichTextField(null=False, blank=False)
    location = models.CharField(max_length=100, null=True, blank=True) #todo false
    date = models.DateField(null=True, blank=True) # todo false

    def save(self ,*args, **kwargs):
        im1 = Image.open(self.poster)

        output1 = BytesIO()
        im1 = im1.resize((300, 400))
        im1.save(output1, format='png', quality=100)

        output1.seek(0)

        self.poster = InMemoryUploadedFile(output1, 'ImageField',
                                                  "%s.jpg" % self.poster.name.split('.')[0], 'image/jpeg',
                                                  sys.getsizeof(output1), None)

        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Document(models.Model):
    caption = models.CharField(max_length=200, null=False, blank=False)
    file = models.FileField(null=False, blank=False, upload_to='event_documents/')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.event) + ' - ' + str(self.file.name)


class EventPhoto(models.Model):
    photo = models.ImageField(upload_to='event_photos/', null=False, blank=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.event) + ' - ' + str(self.photo.name)



