from main import blackjack_score
import pytest

def test_score_for_pair_of_number_cards():
  # Arrange
  hand = [3, 4]

  # Act
  score = blackjack_score(hand)

  # Assert <-- Write assert statement here
  assert score == 7

def test_facecards_have_values_calculated_correctly():
  hand = ["Jack", "King", "Ace"]
  assert blackjack_score(hand) == 21

def test_calculates_aces_as_11_where_it_does_not_go_over_21():
    hand = ["Ace", 2, 3]
    assert blackjack_score(hand) == 16

def test_calculates_aces_as_1_where_11_would_bust():
    hand = ["Ace", "Ace", 9, "Jack"]
    assert blackjack_score(hand) == 21

def test_returns_invalid_for_invalid_cards():
    hand = [1, 'ace']
    assert blackjack_score(hand) == "Invalid"

def test_returns_invalid_for_list_length_greater_than_5():
    hand = [2, 3, 4, 5, 6, 7]
    assert blackjack_score(hand) == "Invalid"

def test_returns_bust_for_scores_over_21():
    hand = ["Jack", 3, "King"]
    assert blackjack_score(hand) == "Bust"

def test_returns_12_for_ace_ace_king():
    hand = ["Ace", "Ace", "King"]
    assert blackjack_score(hand) == 12

def test_returns_14_for_ace_ace_ace_ace():
    hand = ["Ace", "Ace", "Ace", "Ace"]
    assert blackjack_score(hand) == 14