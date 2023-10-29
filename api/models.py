from django.db import models

# Create your models here.

class Question(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/', null=True,blank=True) 
    questions = models.TextField( null=True,blank=True)
    answers = models.TextField( null=True,blank=True)
    audio = models.FileField(upload_to='audio/',null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        if self.questions:
            return self.questions[:50]  # Return the first 50 characters of questions if it's not None
        else:
            return "No questions available"  # Provide a default message if questions is None
