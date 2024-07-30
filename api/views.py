# api/views.py
from rest_framework import viewsets
from .models import User, Student, Teacher, NonTeachingStaff, Subject, Enrollment, Attendance, Exam, ExamResult, Room, Timetable, Event
from .serializers import UserSerializer, StudentSerializer, TeacherSerializer, NonTeachingStaffSerializer, SubjectSerializer, EnrollmentSerializer, AttendanceSerializer, ExamSerializer, ExamResultSerializer, RoomSerializer, TimetableSerializer, EventSerializer
import django_filters
from rest_framework import permissions

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['id', 'username', 'firstname', 'role']


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.filter(id__role='student')
    serializer_class = StudentSerializer
    filterset_fields = ['id', 'admission_date', 'status']


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filterset_fields = '__all__'


class NonTeachingStaffViewSet(viewsets.ModelViewSet):
    queryset = NonTeachingStaff.objects.all()
    serializer_class = NonTeachingStaffSerializer
    filterset_fields = '__all__'


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filterset_fields = '__all__'


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    filterset_fields = '__all__'


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filterset_fields = '__all__'


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    filterset_fields = '__all__'


class ExamResultViewSet(viewsets.ModelViewSet):
    queryset = ExamResult.objects.all()
    serializer_class = ExamResultSerializer
    filterset_fields = '__all__'


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filterset_fields = '__all__'


class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer
    filterset_fields = '__all__'


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filterset_fields = '__all__'
