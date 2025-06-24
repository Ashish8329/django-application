from django.contrib import admin
from base.base_admin import BaseAdmin
from .models import Event

# Register your models here.

@admin.register(Event)
class EventAdmin(BaseAdmin):
    list_display= (
        "title",
        "category",
        "start_time",
        "end_time"
    )
