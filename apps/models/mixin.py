from django.db import models


class BaseMixin(models.Model):
    """Originalモデルの基底クラス"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
