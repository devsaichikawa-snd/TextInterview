/* Javascript Const */

export { REGEX_EMAIL, REGEX_PASSWORD, INQUIRY_DELETE_ACCOUNT_TEXT }


/* 正規表現 */
const REGEX_EMAIL = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
const REGEX_PASSWORD = /^(?=.*[A-Z])(?=.*[0-9])(?=.*[-!"#$%&()*,./:;?@[\]^_`{|}~+<=>])[A-Za-z0-9-!"#$%&()*,./:;?@[\]^_`{|}~+<=>]{8,}$/;

/* 文章 */
const INQUIRY_DELETE_ACCOUNT_TEXT = '\
以下アカウントの削除申請です。\n\
申請者氏名(新アカウント氏名):大根太郎\n\
削除対象氏名(旧アカウント氏名): 蓮根花子\n\
削除対象メールアドレス: renkon@renkon.ne.jp\n\n\
※旧アカウントのメールアドレスは必ずお伝えください。';
