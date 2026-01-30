from django.db import models

class QuizResult(models.Model):
    email = models.EmailField()
    score = models.IntegerField()
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.score}"
