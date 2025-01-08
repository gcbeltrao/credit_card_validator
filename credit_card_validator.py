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
