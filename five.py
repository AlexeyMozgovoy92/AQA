def check_password(password):
    rule_no_space=False
    rule_is_upper=False
    rule_is_lower=False
    rule_is_digit=False
    rule_has_symbol=False
    rule_is_alpha=False

    for elem in password:
        if not elem.isspace():
            rule_no_space=True
        if elem.isupper():
            rule_is_upper=True
        if elem.islower():
            rule_is_lower=True
        if elem.isdigit():
            rule_is_digit=True
        if not elem.isalnum():
            rule_has_symbol=True
        if elem.isalpha():
            rule_is_alpha=True

    if " " in password:
        rule_no_space=False

    if len(password)<8:
        print("пароль должен быть более 8 символов")
    if not rule_no_space:
        print("В пароле не должно быть пробелов")
    if not rule_is_upper:
        print("В пароле должны быть заглавные буквы")
    if not rule_is_lower:
        print("В пароле должны быть буквы в нижнем регистре")
    if not rule_is_digit:
        print("В пароле должны быть цифры")
    if not rule_has_symbol:
        print("Пароль должен содержать символы")
    if not rule_is_alpha:
        print("Пароль должен содержать буквы")

    if rule_no_space and rule_is_upper and rule_is_lower and rule_is_digit and rule_has_symbol and rule_is_alpha:
        return True
    else:
        return False
