def is_very_long(password):
    return False if len(password) < 12 else True

def has_digit(password):
    return any(letter for letter in password if letter.isdigit())

def has_upper_letters(password):
    return any(letter for letter in password if letter.isupper())

def has_lower_letters(password):
    return any(letter for letter in password if letter.islower())

def has_symbols(password):
    return any(letter for letter in password if not letter.isdigit() and not letter.isalpha())

def main():
    password = input("Введите пароль:")
    score = 0
    functions_list = [is_very_long, has_digit, has_upper_letters, has_lower_letters, has_symbols]
    for password_score in functions_list:
        if password_score(password):
            score += 2
    print("Рейтинг пароля:", score)

if __name__ == "__main__":
    main()