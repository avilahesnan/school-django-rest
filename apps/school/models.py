from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    phone = models.CharField(max_length=11, default='')
    rg = models.CharField(max_length=9, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)
    date_birth = models.DateField()
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'


class Course(models.Model):
    LEVEL = (
        ('B', 'Basic'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    )

    name = models.CharField(max_length=60, null=False, blank=False)
    code = models.CharField(max_length=10, null=False, blank=False)
    description = models.CharField(max_length=150, null=False, blank=False)
    level = models.CharField(
        max_length=1,
        choices=LEVEL,
        default='B',
        null=False,
        blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'


class Registration(models.Model):
    PERIOD = (
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('N', 'Night'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.CharField(
        max_length=1,
        choices=PERIOD,
        default='M',
        null=False,
        blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.student} - {self.course}'
