def create_email_body(user_name, email, inquery_type, body):
    res_body = f"利用者氏名:{user_name}\nメールアドレス:{email}\n問合せタイプ:{inquery_type}\n<本文>\n{body}"
    return res_body
