"""review-lab 的被审查对象：故意很小，但边界不少。"""


def normalize_user_id(raw: str) -> str:
    """把用户输入规范成小写、去首尾空白、去前导零的 ID。

    规则：
    - 空字符串 / None 一律报错（不要静默返回空）
    - 纯数字的 ID 去前导零，"000" -> "0"
    - 非数字的前导零不去（例如 "007abc" 保持原样）
    """
    if raw is None or not raw.strip():
        raise ValueError("user_id 不能为空")

    value = raw.strip().lower()

    if value.isdigit():
        return value.lstrip("0") or "0"

    return value


def is_valid_user_id(raw: str) -> bool:
    """宽松校验：3–32 个字符，只允许字母、数字、下划线和短横线。"""
    if not raw:
        return False
    candidate = raw.strip()
    if not (3 <= len(candidate) <= 32):
        return False
    return all(ch.isalnum() or ch in "_-" for ch in candidate)
