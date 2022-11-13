# Функция просто разделитель

def get_sep(sep, sep_len):
    return sep * sep_len

print('моя первая функция')
print(get_sep('*', 100))
print('функция sep разделитель')
print(get_sep('-', 100))

# меняем знак разделителя
print(get_sep('+', 75))

# используем разделитель в тексте
sep=get_sep('-', 50)
text = 'hello {} Func {}'.format(sep, sep)

print(text)