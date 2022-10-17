##### .../myapp/models.py #####

from django.db import models
from datetime import datetime               # Local datetime that is NOT timezone aware.
from django.utils.timezone import now       # Local datetime that is timezone aware (RECOMMENDED!).
#from django.db.models import Deferrable, UniqueConstraint
from django.core.validators import MaxValueValidator, RegexValidator

# Create your models here.
#* Once you have defined your models, you need to tell Django you’re going to use those models.
#** Do this by editing your 'settings' file and changing the 'INSTALLED_APPS' setting to add the name of the module that contains your 'models.py'.


# SIMPLE-MODEL-01:
#* The name of the table, myapp_person, is automatically derived from some model metadata but can be overridden.
#* An id field is added automatically, but this behavior can be overridden.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

# SIMPLE-MODEL-02:
class Shirt(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

    def __str__(self):
        return self.name


# SIMPLE-MODEL-03:
class Student(models.Model):
    # ID must be all digits (with max # of digits <= 10).
    id = models.CharField(primary_key=True, max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MaxValueValidator(150)])
    pub_date = models.DateTimeField(default=now, editable=False, help_text = "Please use the following format: <em>YYYY-MM-DD</em>.")
    #pub_date = models.DateTimeField(default=datetime.now, blank=True, help_text = "Please use the following format: <em>YYYY-MM-DD</em>.")
    #CONSTRAINT: Restricts new entry to unique (not currently existing) student names only.
    #UniqueConstraint(fields=['first_name', 'last_name'], name='unique_name')

    #* OPTIONAL: Give your model metadata by using an inner class 'Meta' as follows:
    #** Model metadata is “anything that’s not a field”
    #*** For example:
    #**** - Database table name 'db_table',
    #**** - Ordering options 'ordering' or
    #**** - Human-readable singular and plural names ('verbose_name' and 'verbose_name_plural')
    class Meta:
        #* NOTE: It is strongly advised that you use lowercase table names when you override the table name explicitly via 'db_table'.
        #** This overrides the default auto table naming convention format: {name-of-app}_{name-of-model}.
        db_table = 'student'
        # NOTE: Fields with a leading minus (“-”) will be ordered descending.
        ordering = ['id']
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'], name='unique_name')
        ]

    #* RECOMMENDED: Set the default field name to return as a string.
    #** A Python “magic method” that returns a string representation of any object.
    #** This is what Python and Django will use whenever a model instance needs to be coerced and displayed as a plain string.
    #*** Most notably, this happens when you display an object in an interactive console or in the admin.
    #** You’ll always want to define this method; the default isn’t very helpful at all.

    def __str__(self):
        return self.id



"""
    TO-DO!
    Expense models.
"""
class Category(models.Model):
    name = models.CharField(max_length=30)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.amount
