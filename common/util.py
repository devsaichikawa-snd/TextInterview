import copy


def replace_lineFeedCode(value: str) -> str:
    """受け取った値の中にある改行コードのエスケープを取り除く

    value(str): 例:'abc\\r\\ndef'みたいな文字列
    """
    tmp_text = copy.copy(value)
    new_value = tmp_text.replace("\\r\\n", "\r\n")

    return new_value
