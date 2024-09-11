VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    score = 0
    number_of_aces = 0

    if len(hand) > 5 or len(hand) < 2: #  A hand, an array of Card values, must be between 2 and 5 items inclusive
        return "Invalid"

    for card in hand:
        if card == 'Jack' or card == 'Queen' or card == 'King':
            score += 10
        elif card == 'Ace':
            number_of_aces += 1
            score += 11
        elif card in VALID_CARDS:
            score += card
        else:
            return "Invalid"

    for ace in range(number_of_aces):
        if score > 21:
            score -= 10 # subtract 10, so that Ace only counts for 1
            
    if score > 21:
        return "Bust"
    
    return score