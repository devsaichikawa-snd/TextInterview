
/**
 * 質問集を取得するAPIを呼び出す
 * @param {String} url 'http//127.0.0.1:8000/textinterview/~'
 * @returns data_Dict
 */
export async function getQuestion(url) {
  let dataDict = {};

  let response = await fetch(url);
  let results = await response.json();

  results.forEach(element => {
    let index = 0;
    index = element.question_id;
    dataDict[index] = element;
  });

  return dataDict;
}
