from django.db import models


class Topic(models.Model):
    """사용자가 배우는 주제"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """모델의 문자열 표현을 반환합니다"""
        return self.text


class Entry(models.Model):
    """주제에 대해 배운 내용"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """항목을 나타내는 문자열을 반환합니다"""
        return f"{self.text[:50]}..."
