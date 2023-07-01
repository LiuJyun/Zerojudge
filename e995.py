def get_nth_character(n):
    digit_length = 1
    count = 9
    start = 1

    while n > digit_length * count:
        n -= digit_length * count
        digit_length += 1
        count *= 10
        start *= 10

    start += (n - 1) // digit_length
    num_str = str(start)
    return int(num_str[(n - 1) % digit_length])


while True:
    try:
        n = int(input())
        character = get_nth_character(n)
        print(character)
    except EOFError:
        break