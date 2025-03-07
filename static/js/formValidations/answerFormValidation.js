// 各種フォームのClientサイドでのFormValidation
import { formSubmit } from '../jsUtil.js';
import { REGEX_EMAIL } from '../jsConst.js';


document.addEventListener('DOMContentLoaded', (event) => {
  // ページリロード時のフォーム再送信を防ぐ
  if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
  }

  const answerForm = document.getElementById('answer_form');
  const answerButton = document.getElementById('answer_button');
  answerButton.addEventListener('click', (event) => {
    // HTMLデフォルトのvalidationをキャンセル
    event.preventDefault();

    // サーバーエラーメッセージを削除
    const serverErrorList = document.querySelectorAll('.server-error-message');
    if (serverErrorList.length > 0) {
      serverErrorList.forEach((serverError) => {
        serverError.remove();
      });
    }

    // Inputとエラー表示箇所の要素を取得する
    const inputAnswer = document.getElementById('id_answer');
    const clientErrorAnswer = document.getElementById('client_error_answer');

    // Errorのカウント
    let errorCount = 0;

    // UserName Validation
    if (inputAnswer.value === '') {
      // ユーザー名が未入力の場合
      clientErrorAnswer.innerHTML = '※回答は入力必須です。';
      inputAnswer.style.borderColor = 'red';
      errorCount += 1;
    }

    // Submit
    if (errorCount === 0) {
      formSubmit(answerForm);
    } else {
      return false;
    }
  });
});
