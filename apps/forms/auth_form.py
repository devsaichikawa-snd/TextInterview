from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from apps.models.auth_model import User


class LoginForm(forms.Form):
    """ログインフォーム"""

    email = forms.EmailField(
        label="メールアドレス",
        max_length=255,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control mb-1",
                "placeholder": "sample@example.ne.jp",
                "autofocus": True,
            }
        ),
        error_messages={
            "required": "メールアドレスは入力必須です。",
            "max_length": "メールアドレスは255字以内です。",
        },
    )
    password = forms.CharField(
        label="パスワード",
        max_length=128,
        min_length=8,
        required=True,
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mb-1",
                "autocomplete": "current-password",
            }
        ),
        error_messages={
            "required": "パスワードは入力必須です。",
            "max_length": "パスワードは255文字以内です。",
            "min_length": "パスワードは8文字以上です。",
        },
    )

    def clean_email(self):
        """emailフィールド単体のFormvalidation"""
        email = self.cleaned_data.get("email")
        if email and not User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "このメールアドレスは存在しません。新規登録を行ってください。"
            )
        return email


class SignUpForm(forms.Form):
    """新規登録フォーム"""

    user_name = forms.CharField(
        label="氏名",
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-1",
                "placeholder": "例：大根太郎",
                "autofocus": True,
            }
        ),
        error_messages={
            "required": "ユーザー名は入力必須です。",
            "max_length": "ユーザー名は255文字以内です。",
        },
    )
    email = forms.EmailField(
        label="メールアドレス",
        max_length=255,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control mb-1",
                "placeholder": "sample@example.ne.jp",
            }
        ),
        error_messages={
            "required": "メールアドレスは入力必須です。",
            "max_length": "メールアドレスは255文字以内です。",
        },
    )
    password = forms.CharField(
        label="パスワード",
        help_text="※パスワードは8文字以上かつ半角英数字で入力してください。",
        max_length=128,
        min_length=8,
        required=True,
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mb-1",
                "autocomplete": "current-password",
            }
        ),
        error_messages={
            "required": "パスワードは入力必須です。",
            "max_length": "パスワードは128文字以内です。",
            "min_length": "パスワードは8文字以上です。",
        },
    )
    password_confirm = forms.CharField(
        label="確認用パスワード",
        help_text="※確認の為、もう一度パスワードを入力してください。",
        max_length=128,
        min_length=8,
        required=True,
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mb-1",
                "autocomplete": "current-password",
            }
        ),
        error_messages={
            "required": "確認用パスワードは入力必須です。",
            "max_length": "パスワードは128文字以内です。",
            "min_length": "パスワードは8文字以上です。",
        },
    )

    def clean(self):
        """SignUpForm全体のvalidation"""
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if email and User.objects.filter(email=email).exists():
            self.add_error(
                "email",
                "このメールアドレスは既に登録されています。",
            )

        if password and password_confirm and password != password_confirm:
            self.add_error("password_confirm", "パスワードが一致しません。")

        try:
            validate_password(
                password=password, user=None, password_validators=None
            )
        except ValidationError as e:
            self.add_error("password_confirm", e)

        return cleaned_data


class ModifyUserInfoForm(forms.Form):
    """利用者情報修正フォーム"""

    user_name = forms.CharField(
        label="氏名",
        help_text="※変更不可",
        max_length=255,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control bg-secondary mb-1",
                "readonly": "readonly",
            }
        ),
    )
    email = forms.EmailField(
        label="メールアドレス",
        max_length=255,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control mb-1",
                "autofocus": True,
                "placeholder": "sample@example.ne.jp",
            }
        ),
        error_messages={
            "required": "メールアドレスは入力必須です。",
            "max_length": "メールアドレスは255字以内です。",
        },
    )


class ResettingPasswordForm(forms.Form):
    """パスワード再設定フォーム"""

    old_password = forms.CharField(
        label="古いパスワード",
        help_text="※現在使用しているパスワードを入力してください。",
        max_length=128,
        min_length=8,
        required=True,
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mb-1",
                "autocomplete": "current-password",
                "autofocus": True,
            }
        ),
        error_messages={
            "required": "古いパスワードは入力必須です。",
            "max_length": "パスワードは255文字以内です。",
            "min_length": "パスワードは8文字以上です。",
        },
    )
    new_password = forms.CharField(
        label="新しいパスワード",
        help_text="※新しいパスワードは8文字以上かつ半角英数字で入力してください。",
        max_length=128,
        min_length=8,
        required=True,
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mb-1",
                "autocomplete": "current-password",
            }
        ),
        error_messages={
            "required": "パスワードは入力必須です。",
            "max_length": "パスワードは255文字以内です。",
            "min_length": "パスワードは8文字以上です。",
        },
    )
    new_password_confirm = forms.CharField(
        label="確認用新しいパスワード",
        help_text="※確認の為、もう一度新しいパスワードを入力してください。",
        max_length=128,
        min_length=8,
        required=True,
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mb-1",
                "autocomplete": "current-password",
            }
        ),
        error_messages={
            "required": "確認用パスワードは入力必須です。",
            "max_length": "パスワードは255文字以内です。",
            "min_length": "パスワードは8文字以上です。",
        },
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_old_password(self):
        """old_passwordフィールド単体のFormvalidation"""
        old_password = self.cleaned_data.get("old_password")
        if not self.user.check_password(old_password):
            self.add_error(
                "old_password", "古いパスワードが正しくありません。"
            )

        return old_password

    def clean(self):
        """ResettingPasswordForm全体のvalidation"""
        cleaned_data = super().clean()
        old_password = cleaned_data.get("old_password")
        new_password = cleaned_data.get("new_password")
        new_password_confirm = cleaned_data.get("new_password_confirm")

        try:
            validate_password(
                password=new_password, user=self.user, password_validators=None
            )
        except ValidationError as e:
            self.add_error("password_confirm", e)

        if (
            old_password
            and new_password
            and new_password_confirm
            and new_password != new_password_confirm
        ):
            self.add_error(
                "new_password_confirm", "新しいパスワードが一致しません。"
            )

        return cleaned_data


class DeleteUserForm(forms.Form):
    """ユーザー退会フォーム"""

    confirmed = forms.BooleanField(
        label="退会しますか？",
        required=True,
        error_messages={"required": "退会する場合はチェックが必須です。"},
    )

    def clean_confirmed(self):
        """confirmed_quitフィールド単体のFormvalidation"""
        confirmed = self.cleaned_data.get("confirmed")
        if not confirmed:
            self.add_error("confirm", "退会する場合はチェックが必須です。")

        return confirmed
