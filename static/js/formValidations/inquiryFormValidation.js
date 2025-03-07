// 各種フォームのClientサイドでのFormValidation
import { formSubmit } from '../jsUtil.js';
import { REGEX_EMAIL, INQUIRY_DELETE_ACCOUNT_TEXT } from '../jsConst.js';


document.addEventListener('DOMContentLoaded', (event) => {
  // ページリロード時のフォーム再送信を防ぐ
  if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
  }

  const inquiryForm = document.getElementById('inquiry_form');
  const inquiryButton = document.getElementById('inquiry_button');
  inquiryButton.addEventListener('click', (event) => {
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
    const inputInquiryType = document.getElementById('id_inquiry_type');
    const inputSubject = document.getElementById('id_subject');
    const inputMessageBody = document.getElementById('id_message_body');
    const clientErrorUserName = document.getElementById('client_error_user_name');
    const clientErrorEmail = document.getElementById('client_error_email');
    const clientErrorInquiryType = document.getElementById('client_error_inquiry_type');
    const clientErrorSubject = document.getElementById('client_error_subject');
    const clientErrorMessageBody = document.getElementById('client_error_message_body');

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

    // InquiryType Validation
    if (inputInquiryType.value === 'default') {
      // 問合せ種別が未入力の場合
      clientErrorInquiryType.innerHTML = '※問合せ種別を選択してください。';
      inputInquiryType.style.borderColor = 'red';
      errorCount += 1;
    }

    // Subject Validation
    if (inputSubject.value === '') {
      // 件名が未入力の場合
      clientErrorSubject.innerHTML = '※件名は入力必須です。';
      inputSubject.style.borderColor = 'red';
      errorCount += 1;
    }

    // MessageBody Validation
    if (inputMessageBody.value === '') {
      // 問合せ本文が未入力の場合
      clientErrorMessageBody.innerHTML = '※問合せ本文は入力必須です。';
      inputMessageBody.style.borderColor = 'red';
      errorCount += 1;
    }

    // Submit
    if (errorCount === 0) {
      formSubmit(inquiryForm);
    } else {
      return false;
    }
  });
});


// 問い合わせ画面のみ、問い合わせ種別の選択によってTextAreaのPlaceHolderを可変にする。
document.addEventListener('change', (event) => {
  event.preventDefault();

  const inputInquiryType = document.getElementById('id_inquiry_type');
  const inputMessageBody = document.getElementById('id_message_body');
  if (inputInquiryType.value === '4') {
    inputMessageBody.innerHTML = INQUIRY_DELETE_ACCOUNT_TEXT;
  }
});
