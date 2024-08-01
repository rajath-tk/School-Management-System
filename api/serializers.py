from rest_framework import serializers
from django.contrib.auth.hashers import make_password  # Add this import statement
from .models import User, Student, Teacher, NonTeachingStaff, Subject, Enrollment, Attendance, Exam, ExamResult, Room, Timetable, Event

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).update(instance, validated_data)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'role', 'gender', 'phone_number', 'date_of_birth', 'address']


class StudentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='id.username')
    email = serializers.ReadOnlyField(source='id.email')
    first_name = serializers.ReadOnlyField(source='id.first_name')
    last_name = serializers.ReadOnlyField(source='id.last_name')
    role = serializers.ReadOnlyField(source='id.role')
    gender = serializers.ReadOnlyField(source='id.gender')
    phone_number = serializers.ReadOnlyField(source='id.phone_number')
    date_of_birth = serializers.ReadOnlyField(source='id.date_of_birth')
    address = serializers.ReadOnlyField(source='id.address')
    
    class Meta:
        model = Student
        fields = '__all__'
        
    def validate(self, data):
        if data['id'].role != 'student':
            raise serializers.ValidationError("The associated user must have the role 'student'.")
        return data
        


class TeacherSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='id.username')
    email = serializers.ReadOnlyField(source='id.email')
    first_name = serializers.ReadOnlyField(source='id.first_name')
    last_name = serializers.ReadOnlyField(source='id.last_name')
    role = serializers.ReadOnlyField(source='id.role')
    gender = serializers.ReadOnlyField(source='id.gender')
    phone_number = serializers.ReadOnlyField(source='id.phone_number')
    date_of_birth = serializers.ReadOnlyField(source='id.date_of_birth')
    address = serializers.ReadOnlyField(source='id.address')
    
    class Meta:
        model = Teacher
        fields = '__all__'
    
    def validate(self, data):
        if data['id'].role != 'teacher':
            raise serializers.ValidationError("The associated user must have the role 'teacher'.")
        return data


class NonTeachingStaffSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='id.username')
    email = serializers.ReadOnlyField(source='id.email')
    first_name = serializers.ReadOnlyField(source='id.first_name')
    last_name = serializers.ReadOnlyField(source='id.last_name')
    role = serializers.ReadOnlyField(source='id.role')
    gender = serializers.ReadOnlyField(source='id.gender')
    phone_number = serializers.ReadOnlyField(source='id.phone_number')
    date_of_birth = serializers.ReadOnlyField(source='id.date_of_birth')
    address = serializers.ReadOnlyField(source='id.address')
    
    class Meta:
        model = NonTeachingStaff
        fields = '__all__'

    def validate(self, data):
        if data['id'].role != 'non_teaching_staff':
            raise serializers.ValidationError("The associated user must have the role 'non_teaching_staff'.")
        return data

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class ExamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = '__all__'
    
    def validate_marks(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError("Marks must be greater than 0.")
        return value
    
    def validate(self, data):
        student = data.get('student')
        subject = data.get('subject')
        
        if not Enrollment.objects.filter(student=student, subject=subject).exists():
            raise serializers.ValidationError("The student is not enrolled in the subject for which the exam result is being created.")    
        return data


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
