from django.contrib import admin
from .models import Record

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'city', 'zipcode', 'created_at')

