/* Models.js */

/**
 * 質問モデル
 */
class QuestionModel {
  // フィールド
  questionId;
  categoryId;
  content;
  categoryName;

  // コンストラクタ
  constructor(questionId, categoryId, content, categoryName) {
    this.questionId = questionId;
    this.categoryId = categoryId;
    this.content = content;
    this.categoryName = categoryName;
  }
}

