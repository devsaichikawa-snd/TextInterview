from django.db import models
from django.db.models import OuterRef, Subquery

from apps.models.mixin import BaseMixin


class QuestionCategory(BaseMixin):
    """質問カテゴリテーブル"""

    category_id = models.AutoField(verbose_name="分類コード", primary_key=True)
    category_name = models.CharField(verbose_name="分類名称", max_length=100)

    class Meta:
        db_table = "m_question_category"

    def __str__(self):
        return self.category_name


class QuestionManager(models.Manager):
    """QuestionのManagerクラス"""

    def select_questions_with_category(self):
        """QuestionCategoryの[category_name]を合わせて取得する"""
        return self.get_queryset().annotate(
            category_name=Subquery(
                QuestionCategory.objects.filter(
                    category_id=OuterRef("category_id")
                ).values("category_name")[:1]
            )
        )


class Question(BaseMixin):
    """質問テーブル"""

    question_id = models.AutoField(verbose_name="質問コード", primary_key=True)
    category_id = models.IntegerField(verbose_name="分類コード")
    content = models.CharField(verbose_name="質問本文", max_length=400)

    objects: QuestionManager = QuestionManager()

    class Meta:
        db_table = "m_question"

    def __str__(self):
        return self.content


class UserAnswerManager(models.Manager):
    """UserAnswerのManagerクラス"""

    def get_user_answer(self, question_id, user_id):
        try:
            return self.get(question_id=question_id, user_id=user_id)
        except self.model.DoesNotExist:
            return None

    def select_answers_with_question(self):
        """QuestionCategoryの[content]を合わせて取得する"""
        return self.get_queryset().annotate(
            content=Subquery(
                Question.objects.filter(
                    question_id=OuterRef("question_id")
                ).values("content")[:1]
            )
        )


class UserAnswer(BaseMixin):
    """利用者回答テーブル"""

    question_id = models.IntegerField(verbose_name="質問コード")
    user_id = models.UUIDField(verbose_name="個人コード")
    answer = models.CharField(verbose_name="回答内容", max_length=1200)

    objects: UserAnswerManager = UserAnswerManager()

    class Meta:
        db_table = "t_user_answer"
        unique_together = ("question_id", "user_id")
