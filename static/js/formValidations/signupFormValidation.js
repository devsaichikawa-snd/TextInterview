// 各種フォームのClientサイドでのFormValidation
import { formSubmit } from '../jsUtil.js';
import { REGEX_EMAIL } from '../jsConst.js';


document.addEventListener('DOMContentLoaded', (event) => {
  // ページリロード時のフォーム再送信を防ぐ
  if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
  }

  const signupForm = document.getElementById('signup_form');
  const signupButton = document.getElementById('signup_button');
  signupButton.addEventListener('click', (event) => {
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
    const inputUserName = document.getElementById('id_user_name');
    const inputEmail = document.getElementById('id_email');
    const inputPassword = document.getElementById('id_password');
    const inputPasswordConfirm = document.getElementById('id_password_confirm');
    const clientErrorUserName = document.getElementById('client_error_user_name');
    const clientErrorEmail = document.getElementById('client_error_email');
    const clientErrorPassword = document.getElementById('client_error_password');
    const clientErrorPasswordConfirm = document.getElementById('client_error_password_confirm');

    // Errorのカウント
    let errorCount = 0;

    // UserName Validation
    if (inputUserName.value === '') {
      // ユーザー名が未入力の場合
      clientErrorUserName.innerHTML = '※氏名は入力必須です。';
      inputUserName.style.borderColor = 'red';
      errorCount += 1;
    }

    // Email Validation
    if (inputEmail.value === '') {
      // メールアドレスが未入力の場合
      clientErrorEmail.innerHTML = '※メールアドレスは入力必須です。';
      inputEmail.style.borderColor = 'red';
      errorCount += 1;
    } else if (!REGEX_EMAIL.test(inputEmail.value)) {
      // メールアドレスの形式かチェックする
      clientErrorEmail.innerHTML = '※メールアドレスの形式で入力してください。';
      inputEmail.style.borderColor = 'red';
      errorCount += 1;
    }

    // Password Validation
    if (inputPassword.value === '') {
      // パスワードが未入力の場合
      clientErrorPassword.innerHTML = '※パスワードは入力必須です。';
      inputPassword.style.borderColor = 'red';
      errorCount += 1;
    }

    // Password Confirm Validation
    if (inputPasswordConfirm.value === '') {
      // 確認用パスワードが未入力の場合
      clientErrorPasswordConfirm.innerHTML = '※確認用パスワードは入力必須です。';
      inputPasswordConfirm.style.borderColor = 'red';
      errorCount += 1;
    }

    // Submit
    if (errorCount === 0) {
      formSubmit(signupForm);
    } else {
      return false;
    }
  });
});
