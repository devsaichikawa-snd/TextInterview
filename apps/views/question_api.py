from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods

from apps.models.question_model import Question


def __serialize_item(item):
    return {
        "question_id": item.question_id,
        "category_id": item.category_id,
        "content": item.content,
        "category_name": item.category_name,
    }


def __serialize_items(items):
    for item in items:
        if item.question_id == 9:
            content_list = item.content.split(r"\r\n")
            new_text = "".join(content_list)
            item.content = new_text

    return [__serialize_item(item) for item in items]


@login_required
@require_http_methods(["GET"])
def api_get_question(request):
    """API Get Question"""
    if request.method == "GET":
        questions = Question.objects.select_questions_with_category()
        data = __serialize_items(questions)

        return JsonResponse(
            data, safe=False, json_dumps_params={"ensure_ascii": False}
        )

    # HTTP Methodが異なっているので、BadRequest
    return HttpResponseBadRequest()
