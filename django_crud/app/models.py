from django.db import models
from base.base_models import BaseModel
from base.choices import EventCategory


# Create your models here.
class Event(BaseModel):
    title = models.CharField(
        max_length=100,
        help_text="event title",
        verbose_name="Title",
        )
    category = models.CharField(
        max_length=20, 
        choices=[x.value for x in EventCategory],
        help_text="category of event",
        verbose_name="Category"
        )
    date = models.DateField(
        help_text="date whene the event is place",
        verbose_name="Event Date"
    )
    start_time = models.TimeField(
        help_text="time when the event is start",
        verbose_name="Start Time"
    )
    end_time = models.TimeField(
        help_text="time when the event is start",
        verbose_name="Start Time"
    )
    is_virtual = models.BooleanField(
        default=False,
        help_text="is event is virtual or not",
        verbose_name="Is Virtual"
        )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="description of the event",
        verbose_name="Description"
    )

    def __str__(self):
        return f"{self.title}"