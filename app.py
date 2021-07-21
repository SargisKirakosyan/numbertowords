import random

ones = ("զրո", "մեկ", "երկու", "երեք", "չորս",
        "հինգ", "վեց", "յոթ", "ութ", "ինը")
tens = ("քսան", "երեսուն", "քառասուն", "հիսուն", "վաթսուն",
        "յոթանասուն", "ութսուն", "իննսուն", "հարյուր")
twos = ("տաս", "տասնմեկ", "տասներկու", "տասներեք", "տասնչորս",
        "տասնհինգ", "տասնվեց", "տասնյոթ", "տասնութ", "տասնինը")
suffixes = ("", "հազար", "միլիոն", "միլլիարդ", "տրիլիոն")


def process(number, index):
    length = len(number)  # The length of number from input
    number = number.zfill(3)  # Filling number from the left for processing
    words = []  # List for appending tranformed numbers
    houndred_digit = int(number[0])  # Get houndred digits
    ten_digit = int(number[1])  # Get ten digits
    points_digit = int(number[2])  # Get point digits

    if number[0] != "0":
        words.append(ones[houndred_digit])

    if len(words):
        words.append(" հարյուր ")

    if(ten_digit > 1):
        words.append(tens[ten_digit - 2])
        words.append(ones[points_digit])
    elif(ten_digit == 1):
        words.append(twos[(int(ten_digit+points_digit) % 10) - 1])
    elif(ten_digit == 0):
        words.append(ones[points_digit])

    if(words[-1] == "զրո"):
        words = words[:-1]
    else:
        words.append(" ")

    if(not len(words) == 0):
        words.append(suffixes[index])

    return "".join(words)


def numbers_to_words(number):
    length = len(str(number))

    if length > 15:  # Write how many digits you want to transform
        return 'This program supports only upto 15 digit numbers.'

    count = length // 3 if length % 3 == 0 else length // 3 + 1
    copy = count
    words = []  # List for appending processed numbers

    for i in range(length - 1, -1, -3):
        words.append(process(str(number)[0 if i - 2 < 0 else i - 2: i + 1],
                     copy - count))
        count -= 1
    final_words = []

    for s in reversed(words):  # Appending to string processed numbers of list
        final_words.append('{} '.format(s))
    return "".join(final_words)  # Return fully processed numbers in string


number = int(input())

if number != 0:
    print(numbers_to_words(number))
else:
    print("Please write a number that is greater than 0")

# if __name__ == "__main__":

#     def random_test():
#         for i in range(0, 200):
#             ran_num = random.randint(1, 10000000)
#             print(ran_num)
#             print(numbers_to_words(ran_num))
#     random_test()
