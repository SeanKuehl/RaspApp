from django.db import models

# Create your models here.

#recipe, meal ideas, grocery stuff to check


class MealIdea(models.Model):
    meal = models.CharField(max_length=60)