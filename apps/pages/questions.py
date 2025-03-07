from collections import defaultdict
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from apps.forms.answer_form import UserAnswerForm
from apps.models.question_model import QuestionCategory, Question, UserAnswer
from apps.views.decorators import log_decorator
from common.util import replace_lineFeedCode


@login_required
@log_decorator
def question_top(request):
    """面接原稿作成Top画面"""
    categories = QuestionCategory.objects.all()
    questions = Question.objects.all().values()

    # category_idをkeyとしグループ化したdictリストを作成する。(N+1対策)
    # → dict{'1':['質問1', '質問2'..., '質問5'], '2':[], '3':[]..., '10':[]}
    questions_dict = defaultdict(list)
    for question in questions:
        if question["question_id"] == 9:
            new_text = replace_lineFeedCode(question["content"])
            question["content"] = new_text
        questions_dict[question["category_id"]].append(question)

    context = {"categories": categories, "questions_dict": questions_dict}

    return render(request, "questions/qtop.html", context)


@login_required
@log_decorator
def upsert_answer(request, question_id, q_content):
    """面接原稿作成&更新画面"""
    user = request.user
    form = None

    user_answer = UserAnswer.objects.get_user_answer(question_id, user.user_id)

    if request.method == "GET":
        if not user_answer:
            form = UserAnswerForm()
        else:
            form = UserAnswerForm(initial={"answer": user_answer.answer})

    if request.method == "POST":
        form = UserAnswerForm(request.POST)

        if form.is_valid():
            if user_answer is None:
                # 新規登録処理
                UserAnswer.objects.create(
                    question_id=question_id,
                    user_id=user.user_id,
                    answer=form.cleaned_data["answer"],
                )
                messages.success(
                    request,
                    "回答を登録しました！",
                )
                return redirect("question_top")
            else:
                # 更新処理
                user_answer.answer = form.cleaned_data["answer"]
                user_answer.save()
                messages.success(
                    request,
                    "回答を更新しました！",
                )
                return redirect("question_top")

    context = {"form": form, "content": q_content}

    return render(request, "questions/upsert_answer.html", context)


@login_required
@log_decorator
def preview_answer(request):
    """質問・回答のプレビュー画面"""

    user = request.user

    # クエリイメージ
    # SELECT
    #   a.id,
    #   a.answer,
    #   q.content
    # FROM dev_textinterview_db.t_user_answer a
    # LEFT JOIN dev_textinterview_db.m_question q
    # 	ON a.question_id = q.question_id
    # WHERE a.user_id = '28236f36c55e415ab383a41c18161264'
    # ;
    queryset = (
        UserAnswer.objects.select_answers_with_question()
        .filter(user_id=user.user_id)
        .values()
    )

    # OutPutイメージ
    # [{
    #     'id': 4,
    #     'created_at': datetime.datetime,
    #     'updated_at': datetime.datetime,
    #     'question_id': 1,
    #     'user_id': UUID('35ce36f9-7f02-462f-831f-8be074bb42af'),
    #     'answer': 'testUser1_test_1',
    #     'content': '自己紹介をしてください。'
    # }]
    useranswer_list = list(queryset)

    context = {"answers": useranswer_list}

    return render(request, "questions/preview_answer.html", context)
