farz = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']
capital_farz = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

user_sentence = input("Zəhmət olmasa cümlənizi daxil edin: ")
while True:
    try:
        user_key = int(input("Zəhmət olmasa rəqəm ilə bir açar daxil edin (0-26): "))
        break
    except ValueError:
        print("Zəhmət olmasa nömrə daxil edin!")


def encryptor(sentence, key):
    list_sentence = list(sentence)
    generated_sentence = [] 
    for character in list_sentence:
        if character.isupper() == True: 
            position = capital_farz.index(character)
            new_position = (position + key) % 26
            generated_sentence.append(capital_farz[new_position]) 
        elif character.islower() == True:
            position = farz.index(character)
            new_position = (position + key) % 26
            generated_sentence.append(farz[new_position])
        else: 
            generated_sentence.append(character)

    return ''.join(generated_sentence)


new_sentence = encryptor(user_sentence, user_key)

print("Şifrələnmiş cümləniz:", new_sentence)
