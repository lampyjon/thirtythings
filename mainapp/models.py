from django.db import models


class TimeWindow(models.Model):
    start_date = models.DateField("period begins on date")

    def __str__(self):
        return str(self.start_date)



class Food(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
    name = models.CharField("name", max_length=500)
    consumed_in_period = models.ManyToManyField(TimeWindow, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name




