from django.db import models

class University(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name if len(self.name) < 20 else f"{self.name[:20]}..."

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title if len(self.title) < 20 else f"{self.title[:20]}..."

class UniversityCourse(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=50)
    duration_weeks = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['university', 'course', 'semester'],
                                    name='unique university and course and semester')
        ]