from django import forms

from common.const import INQUIRY_TYPE_CHOICES


class InquiryForm(forms.Form):
    """問い合わせフォーム"""

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
            "required": "氏名は入力必須です。",
            "max_length": "メールアドレスは255字以内です。",
        },
    )
    email = forms.EmailField(
        label="返信用メールアドレス",
        help_text="※宛先として指定可能なメールアドレスは '1つ' のみです。恐れ入ります。",
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
            "max_length": "メールアドレスは255字以内です。",
        },
    )
    inquiry_type = forms.ChoiceField(
        label="問合せ種別",
        choices=INQUIRY_TYPE_CHOICES,
        initial="default",
        required=True,
        widget=forms.Select(
            attrs={
                "class": "form-control mb-1",
            }
        ),
        error_messages={"required": "問合せ種別は入力必須です。"},
    )
    subject = forms.CharField(
        label="件名",
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-1",
                "placeholder": "例：サービス不具合の報告",
            }
        ),
        error_messages={
            "required": "件名は入力必須です。",
            "max_length": "件名は200文字以内です。",
        },
    )
    message_body = forms.CharField(
        label="問合せ本文",
        max_length=1200,
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-control mb-1",
                "placeholder": "例：面接原稿の作成をした後、登録ボタンを押下しましたが、エラーが発生しました。",
                "autofocus": True,
            }
        ),
        error_messages={
            "required": "問合せ本文は入力必須です。",
            "max_length": "ユーザー名は1200文字以内です。",
        },
    )
