/* TextInterview 実行部のモジュール */
import { getQuestion } from './api.js';

/* グローバル宣言 */
let response;
let clickCounter;
let questionId;

// 初回の画面ロード時にAPIを実行し、Questionを取得する
document.addEventListener("DOMContentLoaded", async (event) => {
  event.preventDefault();

  // クリックカウンターをリセットする
  clickCounter = 0;

  // Questionを取得する
  const url = 'https://textinterview.azurewebsites.net/api/get_question/';
  // const url = 'http://127.0.0.1:8000/api/get_question/';
  response = await getQuestion(url);

  alert('まずは挨拶をしましょう！挨拶を送信しましたら、早速質問が投げかけられます。');
});

// 送信ボタン押下時の実行部
document.getElementById('send_button').addEventListener('click', (event) => {
  event.preventDefault();

  const interviewAnswer = document.getElementById('id_interview_answer');
  const clientErrorInterviewAnswer = document.getElementById('client_error');
  const interviewAnswerValue = interviewAnswer.value.trim();

  if (!interviewAnswerValue) {
    clientErrorInterviewAnswer.innerHTML = '※回答を入力してください。';
    interviewAnswer.style.borderColor = 'red';
    return;
  }

  // 未入力エラーを削除する
  if (clientErrorInterviewAnswer) {
    interviewAnswer.style.borderColor = '';
    clientErrorInterviewAnswer.innerHTML = '';
  }

  // クリックカウンターを更新する
  clickCounter += 1;

  if (clickCounter === 1) {
    questionId = 1;
    sendMessage(questionId);
  }
  else if (1 < clickCounter && clickCounter <= 31) {
    questionId += 1;  // 質問IDを更新する
    sendMessage(questionId);
  }
  else {
    sendMessage(questionId, true);
  }
});

/**
 * 面接やり取り処理 回答→質問→回答...
 */
function sendMessage(questionId, isFinal = false) {
  const interviewAnswer = document.getElementById('id_interview_answer');
  const interviewAnswerValue = interviewAnswer.value.trim();
  const chatBody = document.getElementById('chat_body');

  // 送信メッセージを作成
  const senderIconElement = document.createElement('div');
  const senderMessageElement = document.createElement('div');
  const senderUserIcon = document.createElement('img');
  senderIconElement.classList.add('message-container', 'sender');
  senderMessageElement.classList.add('message', 'sender');
  senderUserIcon.classList.add('user-icon', 'sender');
  senderUserIcon.src = interviewerIconImageUrl;
  senderIconElement.appendChild(senderUserIcon);
  senderIconElement.appendChild(senderMessageElement);
  chatBody.appendChild(senderIconElement);

  senderMessageElement.textContent = interviewAnswerValue;

  // スクロールを最下部に
  chatBody.scrollTop = chatBody.scrollHeight;

  // 入力フィールドをクリア
  interviewAnswer.value = '';
  interviewAnswer.focus();

  if (isFinal) {
    setTimeout(() => {
      alert('お疲れさまでした！これにて模擬面接は終了となります。');
      window.location.href = nextUrl;
    }, 1000); // 1秒後に次のページに遷移
  }

  // ここで受信メッセージを追加する
  setTimeout(() => {
    const receivedIconElement = document.createElement('div');
    const receivedMessageElement = document.createElement('div');
    const receivedUserIcon = document.createElement('img');
    receivedIconElement.classList.add('message-container', 'receiver');
    receivedMessageElement.classList.add('message', 'receiver');
    receivedUserIcon.classList.add('user-icon', 'receiver');
    receivedUserIcon.src = receiverIconImageUrl;
    receivedIconElement.appendChild(receivedUserIcon);
    receivedIconElement.appendChild(receivedMessageElement);
    chatBody.appendChild(receivedIconElement);

    receivedMessageElement.textContent = response[questionId].content;

    // スクロールを最下部に
    chatBody.scrollTop = chatBody.scrollHeight;

  }, 1000); // 1秒後に受信メッセージを表示
}
