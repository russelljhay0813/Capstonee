import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bwest_backend.settings')
django.setup()

from users.models import User
from academics.models import Program, Subject, StudentProfile
from finance.models import EWallet, FeeAssessment

# Create Program
bsit, _ = Program.objects.get_or_create(code='BSIT', name='BS Information Technology')

# Create Subjects
subjects = [
    ('IT101', 'Intro to Computing', 3, 1),
    ('IT102', 'Programming Logic', 3, 1),
    ('IT201', 'Data Structures', 3, 2),
]

for code, name, units, year in subjects:
    Subject.objects.get_or_create(code=code, defaults={
        'name': name, 'units': units, 'year_level': year, 'program': bsit
    })

# Create Student User
user, _ = User.objects.get_or_create(
    username='2024-0001',
    defaults={
        'email': 'student@bwest.edu.ph',
        'first_name': 'Juan',
        'last_name': 'Dela Cruz',
        'role': 'student'
    }
)

if user.password != 'pbkdf2_sha256$...':  # If password not set
    user.set_password('student123')
    user.save()

# Create Student Profile
profile, _ = StudentProfile.objects.get_or_create(
    user=user,
    defaults={'student_id': '2024-0001', 'program': bsit, 'year_level': 2}
)

# Create E-Wallet
EWallet.objects.get_or_create(student=profile, defaults={'balance': 5000})

# Create Fee Assessment
FeeAssessment.objects.get_or_create(
    student=profile,
    semester='1st Sem 2024-2025',
    defaults={
        'tuition_fee': 15000,
        'miscellaneous_fee': 3000,
        'laboratory_fee': 2000,
        'library_fee': 500,
        'amount_paid': 5000
    }
)

print("✅ Sample data created!")
print("Student Login: 2024-0001 / student123")