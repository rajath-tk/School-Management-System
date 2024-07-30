from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ExamResult

@receiver(post_save, sender=ExamResult)
def update_student_grades(sender, instance, **kwargs):
    student = instance.student
    student.update_grades()