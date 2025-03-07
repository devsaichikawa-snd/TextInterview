from django import forms


class UserAnswerForm(forms.Form):
    """新規利用者登録フォーム"""

    answer = forms.CharField(
        label="回答",
        max_length=1200,
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "例：私の名前は大根太郎です。",
                "autofocus": True,
            }
        ),
        error_messages={"required": "回答は入力必須です。"},
    )
