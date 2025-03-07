from django.urls import path

from apps.pages.auth_user import (
    login,
    logout,
    signup,
    modify_userinfo,
    resetting_password,
    delete_user,
)
from apps.pages.about_us import aboutus_page
from apps.pages.home import home_page
from apps.pages.inquiry import inquiry_top
from apps.pages.questions import question_top, upsert_answer, preview_answer
from apps.pages.textinterview import (
    textinterview_top_page,
    textinterview_start_page,
    textinterview_finish_page,
)
from apps.views.question_api import api_get_question


urlpatterns = [
    path("", home_page, name="home"),
    # User Auth
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("signup/", signup, name="signup"),
    path(
        "modify_userinfo/",
        modify_userinfo,
        name="modify_userinfo",
    ),
    path(
        "resetting_password/",
        resetting_password,
        name="resetting_password",
    ),
    path("delete_user/", delete_user, name="delete_user"),
    # Question
    path("question/", question_top, name="question_top"),
    path(
        "question/upsert_answer/<int:question_id>/<str:q_content>/",
        upsert_answer,
        name="upsert_answer",
    ),
    path(
        "question/preview_answer/",
        preview_answer,
        name="preview_answer",
    ),
    # TextInterview
    path(
        "textinterview_top/",
        textinterview_top_page,
        name="textinterview_top",
    ),
    path(
        "textinterview_start/",
        textinterview_start_page,
        name="textinterview_start",
    ),
    path(
        "textinterview_finish/",
        textinterview_finish_page,
        name="textinterview_finish",
    ),
    # Inquiry
    path("inquiry/", inquiry_top, name="inquiry"),
    path("aboutus_page/", aboutus_page, name="aboutus_page"),
    # API
    path(
        "api/get_question/",
        api_get_question,
        name="api_get_question",
    ),
]
