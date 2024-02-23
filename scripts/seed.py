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
    Faker.seed(10)
    for _ in range(quantity_courses):

        options = {'Python Fundamentals': 'Learn the basics of Python programming, covering syntax, data types, and fundamental concepts for beginners', 'Intermediate Python': ' Dive deeper into Python with advanced topics, including object-oriented programming, algorithms, and intermediate-level concepts', 'Advanced Python': 'Master advanced Python features, such as decorators, generators, and metaclasses, to enhance your programming skills', 'Python for Data Science': "Explore Python's powerful libraries (NumPy, Pandas, Matplotlib) for data manipulation, analysis, and visualization in a data science context", 'Python/React': 'Combine Python backend development with React frontend to build dynamic and interactive web applications'}  # noqa: E501

        name, description = random.choice(list(options.items()))
        code = '{}{}-{}'.format(random.choice('ABCDEF'), random.randrange(10, 99), random.randrange(1, 9))  # noqa: E501
        level = random.choice('BIA')
        c = Course(name=name, code=code, description=description, level=level)  # noqa: E501
        c.save()


# create_students(100)
create_courses(5)
