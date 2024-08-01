from django.contrib import admin
from .models import User, Student, Teacher, NonTeachingStaff, Subject, Enrollment, Attendance, Exam, ExamResult, Room, Timetable, Event

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(NonTeachingStaff)
admin.site.register(Subject)
admin.site.register(Enrollment)
admin.site.register(Attendance)
admin.site.register(Exam)
admin.site.register(ExamResult)
admin.site.register(Room)
admin.site.register(Timetable)
admin.site.register(Event)
