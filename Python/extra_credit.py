word = "view"

def vowels(s):
    vowel_list = []
    for i in s:
        if i == "e":
            vowel_list.append(i)
        elif i == "i":
            vowel_list.append(i)
        elif i == "o":
            vowel_list.append(i)
        elif i == "u":
            vowel_list.append(i)
        elif i == "a":
            vowel_list.append(i)
        elif len(vowel_list) == 0:
            return "No Vowels"
    return vowel_list


print vowels(word)