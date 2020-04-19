from django.contrib import admin
from apps.events.models import *


@admin.register(EventPhoto)
class EventPhotoAdmin(admin.ModelAdmin):
    fields = ['photo', 'event']


@admin.register(Document)
class EventDocumentAdmin(admin.ModelAdmin):
    fields = ['caption', 'file', 'event']


class DocumentInline(admin.TabularInline):
    model = Document


class PhotoInline(admin.TabularInline):
    model = EventPhoto


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ['name', 'poster', 'summary', 'description', 'location', 'date']
    inlines = [
        PhotoInline, DocumentInline
    ]
