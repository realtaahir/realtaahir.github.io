from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Section(models.Model):
    section_name = models.CharField(max_length=100)

    def __str__(self):
        return self.section_name
    


class SubSection(models.Model):
    subsection_name = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.subsection_name
    

class HeadQuiz(models.Model):
    headquiz_name = models.CharField(max_length=100)
    subsection = models.ForeignKey(SubSection, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_view_1_headquiz", "Can view the 1 headquizzes"),
            ("can_view_all_headquiz", "Can view all headquizzes"),
        ]

    def __str__(self):
        return self.headquiz_name


class Question(models.Model):
    que = models.ForeignKey('HeadQuiz', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=255, choices=[
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
        ('option4', 'Option 4'),
    ])
    explanation = models.TextField()

    def get_options(self):
        return [self.option1, self.option2, self.option3, self.option4]

    def __str__(self):
        return self.text



class UserResponse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    head_quiz = models.ForeignKey(HeadQuiz, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    total_questions = models.IntegerField()
    correct = models.IntegerField()
    incorrect = models.IntegerField()
    omitted = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.head_quiz.headquiz_name} - {self.datetime}'