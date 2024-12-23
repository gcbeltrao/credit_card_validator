import re

credit_card_patterns = {
    'Elo': r'^(4011|4312|4389)\d{12}$',
    'Visa': r'^4\d{15}$',
    'Mastercard': r'^(5[1-5]\d{14}|22[2-9][1-9]\d{12}|22[3-6]\d{13}|27[0-1]\d{13}|2720\d{12})$',
    'American Express': r'^3[47]\d{13}$',
    'Hipercard': r'^6062\d{12}$',
    'Discover': r'^(6011\d{12}|65\d{14}|64[4-9]\d{13})$'
}

card_flag_counts = {
    'Visa': 0,
    'Mastercard': 0,
    'American Express': 0,
    'Hipercard': 0,
    'Discover': 0,
    'Elo': 0,
}

with open('credit-card-numbers.txt', 'r') as file:
    card_numbers  = [''.join(line.split()) for line in file.readlines()]

for card_number in card_numbers:
    for card_flag, pattern in credit_card_patterns.items():
        if re.match(pattern, card_number):
            card_flag_counts[card_flag] += 1
            break

for card_flag, count in card_flag_counts.items():
    print(f'{card_flag}: {count}')
print(f'Total amount of credit cards: {len(card_numbers)}')

def null():
    return None
    # def validate_credit_card(card_number):
    #     card_number = str(card_number)
    #     number = int(card_number)
    #     if re.match(r'4011[0-9]{12}$', card_number) or re.match(r'4312[0-9]{12}$', card_number) or re.match(r'4389[0-9]{12}$', card_number):
    #         return 'Elo'
    #     elif 4000000000000000 <= number <= 4999999999999999:
    #         return 'Visa'
    #     elif 5100000000000000 <= number <= 5599999999999999 or 2221000000000000 <= number <= 2720999999999999:
    #         return 'Mastercard'
    #     elif 340000000000000 <= number <= 349999999999999 or 370000000000000 <= number <= 379999999999999:
    #         return 'American Express'
    #     elif number >= 6062000000000000:
    #         return 'Hipercard'
    #     elif 6011000000000000 <= number <= 6011999999999999 or 6500000000000000 <= number <= 6599999999999999 or 6440000000000000 <= number <= 6499999999999999:
    #         return 'Discover'
    #     return 'Unkonwn'

    # def validate_credit_card(card_number):
    #     card_number = str(card_number)
    #     number = int(card_number)
    #     if re.match(r'4011[0-9]{12}$', card_number) or re.match(r'4312[0-9]{12}$', card_number) or re.match(r'4389[0-9]{12}$', card_number):
    #         return 'Elo'
    #     elif re.match(r'4[0-9]{15}$', card_number):
    #         return 'Visa'
    #     elif re.match(r'5[1-5][0-9]{14}$', card_number):
    #         return 'Mastercard'
    #     elif re.match(r'34[0-9]{13}$', card_number) or re.match(r'37[0-9]{13}$', card_number):
    #         return 'American Express'
    #     elif re.match(r'6062[0-9]{12}$', card_number):
    #         return 'Hipercard'
    #     elif re.match(r'6011[0-9]{12}$', card_number) or re.match(r'65[0-9]{14}$', card_number):
    #         return 'Discover'
    #     elif 2221000000000000 <= number <= 2720999999999999:
    #         return 'Mastercard'
    #     elif 6440000000000000 <= number <= 6499999999999999:
    #         return 'Discover'
    #     return 'Unkonwn'