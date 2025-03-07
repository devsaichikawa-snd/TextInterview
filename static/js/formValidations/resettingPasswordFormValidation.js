// 各種フォームのClientサイドでのFormValidation
import { formSubmit } from '../jsUtil.js';


document.addEventListener('DOMContentLoaded', (event) => {
  // ページリロード時のフォーム再送信を防ぐ
  if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
  }

  const resettingPasswordForm = document.getElementById('resetting_password_form');
  const resettingPasswordButton = document.getElementById('resetting_password_button');
  resettingPasswordButton.addEventListener('click', (event) => {
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
    const inputOldPassword = document.getElementById('id_old_password');
    const inputNewPassword = document.getElementById('id_new_password');
    const inputNewPasswordConfirm = document.getElementById('id_new_password_confirm');
    const clientOldPassword = document.getElementById('client_error_old_password');
    const clientErrorNewPassword = document.getElementById('client_error_new_password');
    const clientErrorNewPasswordConfirm = document.getElementById('client_error_new_password_confirm');
    // Errorのカウント
    let errorCount = 0;

    // Old Password Validation
    if (inputOldPassword.value === '') {
      // 古いパスワードが未入力の場合
      clientOldPassword.innerHTML = '※古いパスワードは入力必須です。';
      inputOldPassword.style.borderColor = 'red';
      errorCount += 1;
    }

    // New Password Validation
    if (inputNewPassword.value === '') {
      // 新しいパスワードが未入力の場合
      clientErrorNewPassword.innerHTML = '※新しいパスワードは入力必須です。';
      inputNewPassword.style.borderColor = 'red';
      errorCount += 1;
    }

    // New Password Confirm Validation
    if (inputNewPasswordConfirm.value === '') {
      // 確認用新しいパスワードが未入力の場合
      clientErrorNewPasswordConfirm.innerHTML = '※確認用新しいパスワードは入力必須です。';
      inputNewPasswordConfirm.style.borderColor = 'red';
      errorCount += 1;
    }

    // Submit
    if (errorCount === 0) {
      formSubmit(resettingPasswordForm);
    } else {
      return false;
    }
  });
});
