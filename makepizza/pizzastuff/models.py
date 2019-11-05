from django.db import models

# Create your models here.
class ToppingRestrictions(models.Model):
    # ...
    VEGAN = 'VE'
    GLUTENFREE = 'GF'
    HALAL = 'HA'
    MEATDAIRYOK = 'OK'

    TOPPING_TYPE_CHOICES = [
        (VEGAN, 'Vegan'),
        (GLUTENFREE, 'Gluten-Free'),
        (HALAL, 'Halal'),
        (MEATDAIRYOK, 'No Dietary Restrictions')
    ]

    topping_type = models.CharField(max_length=2,
        choices=TOPPING_TYPE_CHOICES,
        default=MEATDAIRYOK)

class Toppings(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return "Making a change"

class Pizza(models.Model):
    # ...
    topping_restrict = models.ManyToManyField(ToppingRestrictions)