import re


def valid_emailaddress(email: str) -> bool:
    """メールアドレスをRFC 5322に沿っているかチェックする

    ユーザー名部分には、英数字と一部の記号（._%+-）が許可されます。
    ドメイン部分は、少なくとも1つの.を含み、2文字以上のアルファベットで構成されます。
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    result = re.match(pattern, email)
    if result is None:
        return False
    else:
        return True
