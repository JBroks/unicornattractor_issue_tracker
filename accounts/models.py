from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    '''
    Create a profile model that will enable user to upload the profile image
    This model will have one to one relationship with the User model
    Set a placeholder image as a default
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'profile_image', 
                                default = 'profile_image/default_img.jpg',
                                blank=True,
                                null = True)

    def __str__(self):
        return f"{self.user.username}'s profile"

@receiver(post_save, sender=User)        
def create_user_profile(sender, instance, created, **kwargs):
    '''
    When a new user registers create a user profile
    '''
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)