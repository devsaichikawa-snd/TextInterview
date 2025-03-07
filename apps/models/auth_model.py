import uuid
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

from apps.models.mixin import BaseMixin


class UserManager(BaseUserManager):
    def create_user(self, user_name, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not user_name:
            raise ValueError("Users must have a user name")

        user = self.model(
            email=self.normalize_email(email),
            user_name=user_name,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, user_name, email, password=None):
        user = self.create_user(user_name, email, password)
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin, BaseMixin):
    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    user_name = models.CharField(verbose_name="ユーザー名", max_length=255)
    email = models.EmailField(
        verbose_name="メールアドレス",
        max_length=255,
        unique=True,
    )
    password = models.CharField(verbose_name="パスワード", max_length=128)
    last_login = models.DateTimeField(
        verbose_name="最終ログイン記録", blank=True, null=True
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects: UserManager = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_name"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
