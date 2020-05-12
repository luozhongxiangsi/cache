import random


def generate_code(code_len=4):
    """
    随机生成验证码
    """

    all_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    last_post = len(all_chars)-1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_post)
        code += all_chars[index]
    return code


if __name__ == "__main__":
    print(generate_code(10))
