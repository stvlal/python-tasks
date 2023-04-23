#todo: Дан генетический код ДНК (строка, состоящая из букв G, C, T, A)
# Постройте РНК, используя принцип замены букв: G → C, C → G, T → A, A→T.
# Напишите функцию, которая на вход получает ДНК, и возвращает РНК. Например:
# Ввод: GGCTAA
# Вывод: CCGATT

convertion_rules = dict(G='C', C='G', T='A', A='T')

def dna_to_rna(dna):
    return ''.join(list(map(lambda x: convertion_rules[x], dna)))

print(dna_to_rna('GGCTAA'))