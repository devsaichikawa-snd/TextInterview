// 各種フォームのClientサイドでのFormValidation
import { formSubmit } from '../jsUtil.js';
import { REGEX_EMAIL } from '../jsConst.js';


document.addEventListener('DOMContentLoaded', (event) => {
  // ページリロード時のフォーム再送信を防ぐ
  if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
  }

  const loginForm = document.getElementById('login_form');
  const loginBotton = document.getElementById('login_button');
  loginBotton.addEventListener('click', (event) => {
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
    const inputEmail = document.getElementById('id_email');
    const inputPassword = document.getElementById('id_password');
    const clientErrorEmail = document.getElementById('client_error_email');
    const clientErrorPassword = document.getElementById('client_error_password');

    // Errorのカウント
    let errorCount = 0;

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

    // Submit
    if (errorCount === 0) {
      // 制御に当たらなければ、submitする
      formSubmit(loginForm);
    } else {
      return false;
    }
  });
});
