from liar import BSPokerGame, Card, simulate_probabilities

def main():
    game = BSPokerGame(num_players=4)
    game.start_game()

    # Example: Calculate probabilities with 3 known cards
    known_cards = [Card('spades', 'J'), Card('clubs', 'Q'), Card('hearts', '3')]
    probabilities = simulate_probabilities(100000, known_cards)
    print("Probabilities with 3 known cards:", probabilities)

    # General results for 15 cards from one deck
    general_probabilities = simulate_probabilities(100000, [])
    print("General probabilities with 15 cards:", general_probabilities)

if __name__ == "__main__":
    main()