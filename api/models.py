from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('non_teaching_staff', 'Non Teaching Staff'),
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"
    
class Student(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'id__role': 'student'})
    admission_date = models.DateField(blank=True, null=True)
    grades = models.JSONField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.id.__str__()


class Teacher(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.id.__str__()


class NonTeachingStaff(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    position = models.CharField(max_length=255)
    department = models.CharField(max_length=255)

    def __str__(self):
        return self.id.__str__()
    
class Subject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    status = models.CharField(max_length=20)
    
    class Meta:
        unique_together = ['student', 'subject']

    def __str__(self):
        return f"{self.student} - {self.subject}"

class Attendance(models.Model):
    ATTENDANCE_STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
    ]
    
    attendee_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=7, choices=ATTENDANCE_STATUS_CHOICES)
    
    class Meta:
        unique_together = ['attendee_id', 'date']

    def __str__(self):
        return f"{self.attendee_id} - {self.date}"
    
class Exam(models.Model):
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.name
    
    class Meta:
        unique_together = ['name', 'subject']
    
class ExamResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    grade = models.CharField(max_length=5)
    
    class Meta:
        unique_together = ['student', 'exam']

    def __str__(self):
        return f"{self.student} - {self.exam}"
    

class Room(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Timetable(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['teacher', 'day_of_week', 'start_time']
    
    def __str__(self):
        return f"{self.teacher} - {self.subject} - {self.day_of_week}"
    
class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    security_staff = models.ForeignKey(NonTeachingStaff, related_name='security_events', on_delete=models.CASCADE)
    event_in_charge = models.ForeignKey(Teacher, related_name='in_charge_events', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
