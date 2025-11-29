from django.db import models

class EventModel(models.Model):
    title = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.CharField(max_length=255)
    joined_users = models.ManyToManyField(
        "events_app.CustomUser",
        blank=True,
        related_name="joined_users"
    )
    organizer = models.ForeignKey(
        "events_app.CustomUser",
        on_delete=models.SET_NULL,
        null=True, blank=True, related_name="organizer"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'События'
        verbose_name_plural = 'События'