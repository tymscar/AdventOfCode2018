def get_winner(player1, player2):
    seen_before = {}

    while len(player1) > 0 and len(player2) > 0:

        current_setup = tuple(player1+[999]+player2)
        if current_setup in seen_before:
            return 1
        else:
            seen_before[current_setup] = True

        card1 = player1.pop(0)
        card2 = player2.pop(0)

        if card1 <= len(player1) and card2 <= len(player2):
            subgame_player1 = player1[:card1]
            subgame_player2 = player2[:card2]
            if get_winner(subgame_player1, subgame_player2) == 1:
                player1.append(card1)
                player1.append(card2)
            else:
                player2.append(card2)
                player2.append(card1)
        else:

            if card1 > card2:
                player1.append(card1)
                player1.append(card2)
            else:
                player2.append(card2)
                player2.append(card1)

    if len(player1) != 0:
        return 1
    else:
        return 2

def part_2():
    input_file = open('input.txt').read().split('\n\n')
    player1 = [int(card) for card in input_file[0].split(":\n")[1].split("\n")]
    player2 = [int(card) for card in input_file[1].split(":\n")[1].split("\n")]


    if get_winner(player1,player2) == 1:
        winner = player1
    else:
        winner = player2


    winner_score = 0

    for i in range(len(winner)):
        winner_score += (len(winner) - i) * winner[i]

    return winner_score


print(part_2())