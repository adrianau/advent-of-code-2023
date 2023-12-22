from functools import cmp_to_key


def hand_cmp(hand_rank_a, hand_rank_b):
    # [0] = hand, [1] = hand ranking

    # Tie breaker for rank
    if hand_rank_a[1] == hand_rank_b[1]:
        hand_a = hand_rank_a[0]
        hand_b = hand_rank_b[0]

        # Iterate through each hand comparing card values
        for idx in range(len(hand_a)):
            if hand_a[idx] == hand_b[idx]:
                continue
            return card_values[hand_a[idx]] - card_values[hand_b[idx]]

    return hand_rank_a[1] - hand_rank_b[1]


# Populate card values
card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
for num in range(2, 10):
    card_values[str(num)] = num


if __name__ == '__main__':
    with open('day7-input.txt', 'r') as f:
        lines = f.readlines()

    hand_score_map = {}
    hand_bid_map = {}
    for line in lines:
        hand, bid = line.split()
        hand_bid_map[hand] = bid
        card_count = {}

        # Count occurrence of each card
        for card in hand:
            if card in card_count:
                card_count[card] += 1
            else:
                card_count[card] = 1

        # Sort by card occurrence in descending order
        card_occurrences = sorted(card_count.values(), reverse=True)

        # Initial score is set to highest occurrence with 10x weighting
        # 10x is arbitrary, it ensures max occurrence takes precedence
        hand_score = card_occurrences[0] * 10

        # Add to score for each pair or more
        for occurrence in card_occurrences:
            if occurrence > 1:
                hand_score += occurrence

        hand_score_map[hand] = hand_score

    # Sort hands based on scoring, subsort based on card value
    ranked_hands = [
        hand
        for hand, _ in sorted(
            hand_score_map.items(),
            key=cmp_to_key(hand_cmp)
        )
    ]

    # Calculate based on hand ranking and its bid
    winnings = []
    for idx, hand in enumerate(ranked_hands):
        ranking = idx + 1
        winnings.append(ranking * int(hand_bid_map[hand]))

    # Get total winnings
    print(sum(winnings))  # 248836197
