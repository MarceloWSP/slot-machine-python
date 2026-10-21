import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {
    'A':2,
    'B':4,
    'C':6,
    'D':8
    }
symbol_value = {
    'A' : 5,
    'B' : 4,
    'C' : 3,
    'D' : 2
    }

def deposit():
    amount = 0
    while True:
        try:
            amount = int(input("What would you like to deposit? $"))
        except ValueError:
            print("Invalid value, please enter only whole numbers.")
            continue
        if amount > 0:
            return amount
            break
        else:
            print("Amount must be greater than 0.")

def get_amount_of_lines():
    while True:
        try:
            lines = int(input(f"Enter the amount of lines to bet on 1-{MAX_LINES} "))
        except ValueError:
            print("Invalid value, please enter only whole numbers.")
            continue
        if 1 <= lines <= MAX_LINES:
            return lines
            break
        else:
            print("Enter a valid number of lines.")

def get_bet():
    amount = 0
    while True:
        try:
            amount = int(input("What would you like to bet? $"))
        except ValueError:
            print("Invalid value, please enter only whole numbers.")
            continue
        if MIN_BET <= amount <= MAX_BET:
            return amount
            break
        else:
            print(f"Amount must be between {MIN_BET} and {MAX_BET}.")

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)
    
    #agora eu vou encher as linhas de simbolos, escolhendo um simbolo aleatorio de all_symbols, e ir tirando da lista de symbols (symbols.remove)
    columns = []
    for _ in range(cols):
        current_symbols = all_symbols[:]
        column = []
        for _ in range(rows):
            s = random.choice(current_symbols)
            column.append(s)
            current_symbols.remove(s)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row],end=" | ")
            else: 
                print(column[row],end="")
        print()

def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)
    return winnings,winning_lines


def spin(balance):
    lines = get_amount_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enought to bet that amount, your current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines}. Total bet is equal to {bet*lines}$")
    
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"You won {winnings}$ on lines ",*winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}.")
        
        ipt = input("Press enter to play (q to quit).")
        if ipt.lower() == 'q':
            break
        else:
            balance += spin(balance)
        if balance == 0:
            break
    print(f'You left with ${balance}.')

main()