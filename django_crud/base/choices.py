from enum import Enum

class ChoieEnum(Enum):
    @classmethod
    def get_value(cls, member):
        return cls[member].value[0]
    

class Status(ChoieEnum):
    PENDING = ("pending", "Pending")
    COMPLETED = ("completed", "Completed")
    REJECTED = ("rejected", "Rejected")

class EventCategory(ChoieEnum):
    MEETING = ('meeting', 'Meeting')
    HOLIDAY = ('holiday', 'Holiday')
    REMINDER = ('reminder', 'Reminder')