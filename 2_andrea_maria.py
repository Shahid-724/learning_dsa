def andrea_maria_game(maria_cards, andrea_cards, call):
    
    # Initialize scores
    andrea_score = 0
    maria_score = 0

    # Determine starting index based on call
    start_index = 0 if call.lower() == "even" else 1

    # Iterate through the relevant indices
    for i in range(start_index, len(maria_cards), 2):
        andrea_card = andrea_cards[i]
        maria_card = maria_cards[i]

        # Update scores
        andrea_score += andrea_card - maria_card
        maria_score += maria_card - andrea_card

    return andrea_score, maria_score

# Example usage
if __name__ == "__main__":
    maria_cards = [1, 2, 3]
    andrea_cards = [2, 1, 3]
    call = "Even"

    andrea_score, maria_score = andrea_maria_game(maria_cards, andrea_cards, call)
    print(f"Andrea's Score: {andrea_score}")
    print(f"Maria's Score: {maria_score}")
    if andrea_score > maria_score:
        print('Andrea')
    elif maria_score > andrea_score:
        print('Maria')
    else:
        print('Tie')

# Time Complexity: O(n)
# Space Complexity: O(1)