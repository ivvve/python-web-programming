from django.db import models
from datetime import datetime


class Question(models.Model):
    id: int = models.AutoField(primary_key=True)
    text: str = models.CharField(max_length=100)
    published_at: datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text


class Choice(models.Model):
    id: int = models.AutoField(primary_key=True)
    text: str = models.CharField(max_length=100)
    question: Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    vote_count: int = models.PositiveIntegerField(default=0)

    def increase_vote_count(self) -> None:
        self.vote_count += 1

    def __str__(self) -> str:
        return self.text
