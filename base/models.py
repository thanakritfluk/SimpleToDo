from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    # user one to many relationship => 1 user have many items
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    complete = models.BooleanField(default=False)
    # Auto now add set timestamp
    create = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title

    
    """
    Meta inner class in Django models:
    This is just a class container with some options (metadata) attached to the model.
    It defines such things as available permissions, associated database table name, whether the model is abstract or not, 
    singular and plural versions of the name etc.
    """
    class Meta:
        ordering = ['complete']