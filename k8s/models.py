from django.db import models


class Member(models.Model):
    user_id = models.CharField(max_length=14, unique=True, null=False)
    user_pwd = models.CharField(max_length=20, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id
