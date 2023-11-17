from django.db import models

# Create your models here.

# district_id_id Model
class District(models.Model):
    name = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.name

# User Model
class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    german_proficiency_level = models.CharField(max_length=255, null=True, blank=True)
    native_language = models.CharField(max_length=255, null=True, blank=True)
    learning_languages = models.CharField(max_length=255, null=True, blank=True)
    hobbies = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username


# Cafe Model
class Cafe(models.Model):
    name = models.CharField(max_length=255, unique=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    address = models.TextField()
    suitable_for_events = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# Reservation Model
class Reservation(models.Model):
    reservation_date = models.DateTimeField()
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)

# Reservation Participants Model
class Reservation_Participants(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('reservation', 'user')

# Event Model
class Event(models.Model):
    event_name = models.CharField(max_length=255)
    event_type = models.CharField(max_length=255)
    date = models.DateTimeField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_name

# User Event Model
class UserEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'event')
