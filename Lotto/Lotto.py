"Lotto 6 z 49"

import random
list = [i + 1 for i in range(49)]
random_numbers = []
def random_lotto():
    while True:
        y = random.choice(list)
        if y in random_numbers:
            continue
        else:
            if len(random_numbers) != 6:
                random_numbers.append(y)
        if len(random_numbers) == 6:
            break

    return random_numbers
random_lotto()
print(random_numbers)
