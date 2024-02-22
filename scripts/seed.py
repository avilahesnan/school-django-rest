import os
import django
import random
from faker import Faker
from validate_docbr import CPF
from apps.school.models import Student, Course


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()


def create_students(quantity_students):
    fake = Faker('en-us')
    Faker.seed(10)
    for _ in range(quantity_students):
        cpf = CPF()
        name = fake.name()
        rg = '{}{}{}{}'.format(random.randrange(10, 99), random.randrange(100, 999), random.randrange(100, 999), random.randrange(0, 9))  # noqa: E501
        cpf = cpf.generate()
        date_birth = fake.date_between(start_date='-18y', end_date='today')
        a = Student(name=name, rg=rg, cpf=cpf, date_birth=date_birth)
        a.save()


def create_courses(quantity_courses):
    fake = Faker('en-us')
    Faker.seed(10)
    for _ in range(quantity_courses):
        name = fake.name()
        code = '{}{}-{}'.format(random.choice('ABCDEF'), random.randrange(10, 99), random.randrange(1, 9))  # noqa: E501
        descs = ['Python Fundamentals', 'Intermediate Python', 'Advanced Python', 'Python for Data Science', 'Python/React']  # noqa: E501
        description = random.choice(descs)
        descs.remove(description)
        level = random.choice('BIA')
        c = Course(name=name, code=code, description=description, level=level)  # noqa: E501
        c.save()


create_students(100)
create_courses(5)
