from django import forms


class TextInterviewInputForm(forms.Form):
    """TextInterview疑似面接回答入力フォーム"""

    interview_answer = forms.CharField(
        max_length=1200,
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "回答を入力してください",
                "cols": "40",
                "rows": "5",
            }
        ),
    )
