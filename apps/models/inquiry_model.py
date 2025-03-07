from django.db import models

from apps.models.mixin import BaseMixin


class InquiryManager(models.Manager):
    """QuestionのManagerクラス"""

    pass


class Inquiry(BaseMixin):
    """問い合わせテーブル"""

    inquiry_id = models.AutoField(
        verbose_name="問合せコード", primary_key=True
    )
    user_id = models.UUIDField(verbose_name="利用者コード")
    user_name = models.CharField(verbose_name="ユーザー名", max_length=255)
    email = models.EmailField(verbose_name="メールアドレス", max_length=255)
    inquiry_type = models.IntegerField(verbose_name="問合せ種別")
    subject = models.CharField(verbose_name="件名", max_length=200)
    message_body = models.CharField(verbose_name="問合せ本文", max_length=1200)

    objects: InquiryManager = InquiryManager()

    class Meta:
        db_table = "t_inquiry"

    def __str__(self):
        return self.subject
