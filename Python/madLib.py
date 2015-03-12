noun1 = "cat"
noun2 = "dog"
num1 = "4"
num2 = "8"

word_list = [noun1, noun2, num1, num2]
def mad_lib(n):
    word_array = []
    for i in n:
        word_array.append(i)
    print "The " + word_array[0] + " and the " + word_array[1] + " met to battle in the arena. The " + word_array[0] + "'s fans threw him " + word_array[2] + " powerful magical potions. The " + word_array[1] + "'s fans threw down " + word_array[3] + " pillows."

mad_lib(word_list)
