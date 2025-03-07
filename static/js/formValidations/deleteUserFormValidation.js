// 各種フォームのClientサイドでのFormValidation
import { formSubmit } from '../jsUtil.js';


document.addEventListener('DOMContentLoaded', (event) => {
  // ページリロード時のフォーム再送信を防ぐ
  if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
  }

  const deleteUserForm = document.getElementById('delete_user_form');
  const deleteUserButton = document.getElementById('delete_user_button');
  deleteUserButton.addEventListener('click', (event) => {
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
    const inputConfirmed = document.getElementById('id_confirmed');
    const clientErrorConfirmed = document.getElementById('client_error_confirmed');

    // Errorのカウント
    let errorCount = 0;

    // UserName Validation
    if (inputConfirmed.value === false) {
      // ユーザー名が未入力の場合
      clientErrorConfirmed.innerHTML = '※退会する場合はチェックが必須です。';
      inputConfirmed.style.borderColor = 'red';
      errorCount += 1;
    }

    // Submit
    if (errorCount === 0) {
      formSubmit(deleteUserForm);
    } else {
      return false;
    }
  });
});
