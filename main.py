import urwid

password = str()


def is_very_long(password):
    return len(password) >= 12


def has_digit(password):
    return any(i.isdigit() for i in password)


def has_letters(password):
    return any(i.isalpha() for i in password)


def has_upper_letters(password):
    return any(i.isupper() for i in password)


def has_lower_letters(password):
    return any(i.islower() for i in password)


def has_symbols(password):
    return any(not i.isdigit() and not i.isalpha() for i in password)


def rating_score(password):
    score = 0
    func_list = [
    is_very_long,
    has_digit,
    has_letters,
    has_upper_letters,
    has_lower_letters,
    has_symbols
]
    for func in func_list:
        if func(password):
            score += 2
    return score


def on_ask_change(reply, edit, new_edit_text):
    score = rating_score(new_edit_text)
    reply.set_text("Рейтинг пароля: " + str(score))


def main():
    ask = urwid.Edit('Введите пароль: ', mask='*')
    reply = urwid.Text(password)
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change, weak_args=[reply])
    urwid.MainLoop(menu).run()


if __name__ == "__main__":
    main()






        



    






    
        
        


        
    
        

