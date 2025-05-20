from django.db import models

class Test(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    time_limit = models.IntegerField(help_text="Time in minutes")

    def __str__(self):
        return f"{self.title}"

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='questions/', blank=True, null=True)
    def __str__(self):
        return f"{self.text}"

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='options/', blank=True, null=True)
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.text}"

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.selected_option}"
