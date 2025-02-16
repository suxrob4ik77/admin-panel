
from django.db import models


# class Kurs(models.Model):
#     title=models.CharField(max_length=50)

class Kurs(models.Model):
    title = models.CharField(max_length=255)
    boshlanish = models.DateTimeField(null=True, blank=True)
    tugashi = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.boshlanish} - {self.tugashi} - {self.created_at} {self.updated_at}"

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"
        ordering = ['-created_at']


class Student(models.Model):
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.phone} - {self.email} - {self.kurs}"
