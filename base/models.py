from django.db import models

# Create your models here.

class ContactMessage(models.Model):


    Query_Choices =  [
        ('', 'Query Related'),
        ('general', 'General Inquiry'),
        ('support', 'Support'),
        ('feedback', 'Feedback'),
    ]
    fullname=models.CharField( max_length=100)
    Email=models.EmailField()
    QueryRelated=models.CharField( max_length=50, choices=Query_Choices)
    message=models.TextField()
    created=models.DateTimeField(auto_now_add=True)

    def __self__(self):
        return self.fullname
    

class Subscriber(models.Model):
    email=models.EmailField( unique=True)
    subscribed_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ['-subscribed_at']

