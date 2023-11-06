from django.db import models

# Create your models here.

# District Model
class District(models.Model):
    name = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.username

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
    native_languages = models.JSONField()
    learning_languages = models.JSONField()
    hobbies = models.JSONField()

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField()
    participants = models.JSONField()  # Storing an array of user IDs

    def __str__(self):
        return f"Reservation by {self.user.username} on {self.reservation_date}"


# Events Model
class Event(models.Model):
    name = models.CharField(max_length=255)
    event_type = models.CharField(max_length=255, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    date = models.DateTimeField()
    participants = models.JSONField()

    def __str__(self):
        return self.name

