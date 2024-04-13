import random
cards_value = {"2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 10, "Jack" : 10, "Queen" : 10, "King" : 10, "Ace" : 11}
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suits = ["Spades", "Hearts", "Diamond", "Clubs"]
card_count = 0

# Pre-game UI
print("Hello! Care for a game of blackjack?")
entry_flag = True
while entry_flag == True:
    entry_input = input('Enter "Y" / "N": ')
    if entry_input.upper() == "N":
        print("I guess not everyone is in the mood to play blackjack ):. If you ever do change your mind just rerun the programme.")
        entry_flag = False
    elif entry_input.upper() != "N" and entry_input.upper() != "Y" and entry_input.upper() != "SLOTS WHERE":
        print("Invalid input. Try again")
    elif entry_input.upper() == "SLOTS WHERE":
        print("Slots function not available yet. Give the creator some time to learn his code.""\n""In the meantime, Why don't you play Blackjack?")
    else:
        break

# Gameplay ( woohoo ): )
if entry_flag != False:

    # Giving out the cards
    # Computer side
    gone_cards  = []
    drawn_cards = []
    total_counter = 0
    comp_total_face = []
    while card_count < 2:
        random_value = random.choice(cards)
        drawn_cards.append(random_value)
        random_suit = random.choice(suits)
        random_card = random_value + " " + random_suit
        if random_card in gone_cards:
            continue
        else:
            gone_cards.append(random_card)
            comp_total_face.append(str(random_value))
            total_counter += cards_value[random_value]
            card_count += 1
            #print(comp_total_face)

    # Computer decides whether to draw or not
    if cards[-1] in comp_total_face:
        cp_number_of_aces = comp_total_face.count(cards[-1])
        if total_counter < 22:
            pass
        else:
            for player_ace_count in range(cp_number_of_aces):
                if total_counter > 21:
                    total_counter -= 10

    if total_counter < 14:
        random_value = random.choice(cards)
        total_counter += cards_value[random_value]
        random_suit = random.choice(suits)
        random_card = random_value + " " + random_suit
        if random_card in gone_cards:
            pass
        else:
            gone_cards.append(random_card)
            comp_total_face.append(str(random_value))
            card_count += 1
    elif total_counter == 14 or total_counter == 15 or total_counter == 16 or total_counter == 17:
        coin = random.randint(1, 2)
        if coin == 1:
            random_value = random.choice(cards)
            total_counter += cards_value[random_value]
            random_suit = random.choice(suits)
            random_card = random_value + " " + random_suit
            if random_card in gone_cards:
                pass
            else:
                gone_cards.append(random_card)
                comp_total_face.append(str(random_value))
                card_count += 1
        else:
            pass
    else:
        pass

    # Player side
    print("These are your cards:")
    player_card_count = 0
    player_cards = []
    player_count = 0
    player_total_face = []
    while player_card_count < 2:
        random_value = random.choice(cards)
        random_suit = random.choice(suits)
        random_card = random_value + " " + random_suit
        if random_card in gone_cards:
            continue
        else:
            gone_cards.append(random_card)
            player_cards.append(random_card)
            player_total_face.append(str(random_value))
            player_count += cards_value[random_value]
            player_card_count += 1
            print(random_card)
            #print(player_total_face)
    print(f"Current cards: {player_cards}")
    print(f"Computer's top card: {gone_cards[1]}")

    #Additional cards
    draw_flag = True
    while draw_flag == True:
        print("Will you like to draw another card?")
        draw_input = input('Enter "Y" / "N": ')
        if draw_input.upper() != "N" and draw_input.upper() != "Y" :
            print("Invalid input. Try again")
        elif draw_input.upper() == "Y":
            random_value = random.choice(cards)
            random_suit = random.choice(suits)
            random_card = random_value + " " + random_suit
            if random_card in gone_cards:
                continue
            else:
                gone_cards.append(random_card)
                player_cards.append(random_card)
                player_total_face.append(str(random_value))
                player_count += cards_value[random_value]
                player_card_count += 1
                #print(player_count)
                print(random_card)
                print(f"Current cards: {player_cards}")
        else:
            break

    # Computation
    # Computer total value : total_counter
    # Player total value: player_count
    # Player's cards: player_total_face
    # Computer's cards : comp_total_face
    # Computer: card_count
    # Player: player_card_count
    if cards[-1] in player_total_face:
        player_number_of_aces = player_total_face.count(cards[-1])
        if player_count < 22:
            pass
        else:
            for player_ace_count in range(player_number_of_aces):
                if player_count > 21:
                    player_count -= 10
    if card_count > 4 and total_counter < 22:
        print("Computer wins since computer draws more than 4 cards")
        print(player_card_count)
        print(card_count)
    elif player_card_count > 4 and player_count < 22:
        print("Player wins since computer draws more than 4 cards")
        print(player_card_count)
        print(card_count)
    elif total_counter > 21:
        if player_count > 21:
            print(f"Your total count: {player_count}")
            print(f"Computer's total count: {total_counter}")
            print("No one wins. Both players busted")
        elif player_count < 22:
            print(f"Your total count: {player_count}")
            print(f"Computer's total count: {total_counter}")
            print("You win. Compurer busted")
    if total_counter < 21:
        if player_count > 21:
            print(f"Your total count: {player_count}")
            print(f"Computer's total count: {total_counter}")
            print("You lost. You busted")
        elif player_count < 22:
            if total_counter > player_count:
                print(f"Your total count: {player_count}")
                print(f"Computer's total count: {total_counter}")
                print("Computer wins")
            else:
                print(f"Your total count: {player_count}")
                print(f"Computer's total count: {total_counter}")
                print("You win")

