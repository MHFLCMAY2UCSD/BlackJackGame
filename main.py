import random

# Global variables
CARD_NAMES = ('One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
              'Eight', 'Nine', 'Ten', 'Jack', 'King', 'Queen', 'Ace')

CARD_VALUES = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,
               'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
               'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

SUITS = ('Hearts', 'Spades', 'Clubs', 'Diamonds')


class Chips:
    # This class will generate 250 to 50,000 chips for the player to bet with.

    def __init__(self):
        self._total_chips = random.randint(250, 50000)

    def getting_total(self):
        return self._total_chips


class Deck:
    # List -> self.deck
    # While loop is going to loop til it hits 52 times.
    # The cards do not repeat it self after 4 iteration as to keep in touch with the original deck.

    def __init__(self):
        self.deck = []
        self.card = CARD_NAMES
        self.suits = SUITS

    def creating_deck(self):
        for i in range(len(CARD_NAMES)):

            for index in range(len(SUITS)):
                self.deck.append(self.card[i] + ' of ' + self.suits[index])

        random.shuffle(self.deck)

    def getting_deck(self):
        return self.deck


class Card:
    # This class is going to pop() the first item from the deck list and calculate it's the value.
    # When the card is pulled I want to to keep track of the score and the amount of aces in the player / dealer hand.

    def __init__(self, created_deck):
        self._created_deck = created_deck

        self._player = []

        self._list_a = []
        self._list_b = []

        self._dealer = []

        # Normal Player
        self._value = 0
        self._ace = 0

        # Split Player
        self._split_a = 0
        self._split_b = 0
        self._split_a_ace = 0
        self._split_b_ace = 0

        #  Normal Dealer
        self._d_value = 0
        self._d_ace = 0

    # Everytime you pop a card you also print down it's value.
    def setting_cards(self):
        pulling_card = self._created_deck.pop(0)
        self._player.append(pulling_card)

    def setting_cards_dealer(self):
        pulling_card = self._created_deck.pop(0)
        self._dealer.append(pulling_card)

    #  Made for just splitting, might combine with normal if there is time.
    def setting_split_a(self):
        pulling_card_a = self._created_deck.pop(0)
        self._list_a.append(pulling_card_a)

    def setting_split_b(self):
        pulling_card_b = self._created_deck.pop(0)
        self._list_b.append(pulling_card_b)

    # Keeping track of the aces and the values
    def setting_value(self):
        self._value = 0
        self._ace = 0
        for i in self._player:
            cards_value = i.split()
            # print(cards_value)  # TODO
            if cards_value[0] == 'Ace':
                self._ace += 1
                self._value += 11
            else:
                self._value += CARD_VALUES[cards_value[0]]

    # A
    def setting_split_value_a(self, list_split_a):
        self._list_a = list_split_a
        self._split_a = 0
        self._split_a_ace = 0
        for i in self._list_a:
            cards_value = i.split()
            # print(cards_value) # TODO
            if cards_value[0] == 'Ace':
                self._split_a_ace += 1
                self._split_a += 11
            else:
                self._split_a += CARD_VALUES[cards_value[0]]

    # B
    def setting_split_value_b(self, list_split_b):
        self._list_b = list_split_b
        self._split_b = 0
        self._split_b_ace = 0
        for i in self._list_b:
            cards_value = i.split()
            # print(cards_value) # TODO
            if cards_value[0] == 'Ace':
                self._split_b_ace += 1
                self._split_b += 11
            else:
                self._split_b += CARD_VALUES[cards_value[0]]

    # dealer value setter.
    def setting_value_dealer(self):
        self._d_value = 0
        self._d_ace = 0
        for i in self._dealer:
            cards_value_dealer = i.split()
            # print(cards_value_dealer) # TODO
            if cards_value_dealer[0] == 'Ace':
                self._d_ace += 1
                self._d_value += 11
            else:
                self._d_value += CARD_VALUES[cards_value_dealer[0]]

    # Converting aces to values that goes above 21
    def setting_aces(self):
        while True:
            if self._value > 21 and self._ace:
                self._value -= 10
                self._ace -= 1
            else:
                break

    # Split
    # A
    def setting_split_aces_a(self):
        while True:
            if self._split_a > 21 and self._split_a_ace:
                self._split_a -= 10
                self._split_a_ace -= 1
            else:
                break

    # B
    def setting_split_aces_b(self):
        while True:
            if self._split_b > 21 and self._split_b_ace:
                self._split_b -= 10
                self._split_b_ace -= 1
            else:
                break

    # Converting aces to values that foes above 21 or exactly 17
    def setting_aces_dealer(self):
        while True:
            if self._d_value == 17 or self._d_value > 21 and self._d_ace:
                self._d_value -= 10
                self._d_ace -= 1
            else:
                break

    # Player
    def getting_cards(self):
        return self._player

    def getting_score(self):
        return self._value

    def getting_ace(self):
        return self._ace

    # Split
    # A
    def getting_split_a(self):
        return self._list_a

    def getting_split_a_value(self):
        return self._split_a

    def getting_split_a_ace(self):
        return self._split_a_ace

    # B
    def getting_split_b(self):
        return self._list_b

    def getting_split_b_value(self):
        return self._split_b

    def getting_split_b_ace(self):
        return self._split_b_ace

    # Dealer
    def getting_cards_dealer(self):
        return self._dealer

    def getting_score_dealer(self):
        return self._d_value

    def getting_ace_dealer(self):
        return self._d_ace


class GameLogic:

    def __init__(self, p_val, p_list, d_ace, bet):
        self._p_val = p_val
        self._p_list = p_list
        self._d_ace = d_ace
        self._options = ('\nOptions:', 'Hit', 'Double', 'Split', 'Insurance', 'Stand', 'Surrender')
        self._side = 0
        self._bet = bet
        self._will = ''

        # print(p_val, d_ace, "Player and dealer")  # TODO

    def getting_options(self):
        # Splitting List
        new_p_list = [i.split() for i in self._p_list]

        # Giving player the options base on their cards and the dealer's cards
        if new_p_list[0][0] == new_p_list[1][0] and self._d_ace:  # (H,D,S,I,S,S)
            print(*self._options, sep='\n')
            user_choice = input("\nPlease enter you option here: ").lower().capitalize()
            while user_choice != self._options[1] and user_choice != self._options[2] \
                    and user_choice != self._options[3] and user_choice != self._options[4] \
                    and user_choice != self._options[5] and user_choice != self._options[6]:
                print("Sorry, that was not one of the options.  Please try again.")
                user_choice = input("\nPlease enter you option here: ").lower().capitalize()
            return user_choice

        elif new_p_list[0][0] == new_p_list[1][0]:  # (H,D,S,S,S)
            print(*self._options[0: 4], *self._options[5: 7], sep='\n')
            user_choice = input("\nPlease enter you option here: ").lower().capitalize()
            while user_choice != self._options[1] and user_choice != self._options[2] \
                    and user_choice != self._options[3] and user_choice != self._options[5] \
                    and user_choice != self._options[6]:
                print("Sorry, that was not one of the options.  Please try again.")
                user_choice = input("\nPlease enter you option here: ").lower().capitalize()
            return user_choice

        elif self._d_ace:  # (H,D,I,S,S)
            print(*self._options[0: 3], *self._options[4: 7], sep='\n')
            user_choice = input("\nPlease enter you option here: ").lower().capitalize()
            while user_choice != self._options[1] and user_choice != self._options[2] \
                    and user_choice != self._options[4] and user_choice != self._options[5] \
                    and user_choice != self._options[6]:
                print("Sorry, that was not one of the options.  Please try again.")
                user_choice = input("\nPlease enter you option here: ").lower().capitalize()
            return user_choice

        else:  # (H,D,S,S)
            print(*self._options[0: 3], *self._options[5: 7], sep='\n')
            user_choice = input("\nPlease enter you option here: ").lower().capitalize()
            while user_choice != self._options[1] and user_choice != self._options[2] \
                    and user_choice != self._options[5] and user_choice != self._options[6]:
                print("Sorry, that was not one of the options.  Please try again.")
                user_choice = input("\nPlease enter you option here: ").lower().capitalize()
            return user_choice

    def normal_case(self):
        print(*self._options[0: 2], *self._options[5: 6], sep='\n')
        user_choice = input("\nPlease enter you option here: ").lower().capitalize()
        while user_choice != self._options[1] and user_choice != self._options[5] and user_choice != self._options[6]:
            print("Sorry, that was not one of the options.  Please try again.")
            user_choice = input("\nPlease enter you option here: ").lower().capitalize()
        return user_choice

    def setting_insurance_count(self):
        while True:
            try:
                print("Please enter the your side bet.")
                self._side = round(float(input()), 2)
            except TypeError:
                print("Please enter a integer.")
                continue
            except ValueError:
                print("Please enter a integer.")
                continue
            else:
                if self._side > self._bet / 2:
                    print("\nPlease only enter the maximum of half of your original bet of:", self._bet)
                else:
                    break

    def setting_play(self):
        print("\nDo you want to keep playing?")
        self._will = input().lower()
        while self._will != 'yes' and self._will != 'y' and self._will != 'no' and self._will != 'n':
            print("Please enter yes or no.")
            self._will = input().lower()

    def getting_insurance_count(self):
        return self._side

    def getting_play(self):
        return self._will == 'y' or self._will == 'yes'


def main():
    # The Only thing we want to initialize but not get rid of if player wants to play again.
    print("Note:  This is a pre build, split does not work and in result will cause an error if user input 'Split'.")
    total_bet = Chips()

    cash_vault = total_bet.getting_total()

    keep_playing = True
    while keep_playing:

        deck_cards = Deck()

        user_bet = 0  # Declaration

        print("Your Total:", cash_vault)
        print("Please place a bet.  Note: the minimum bet is 250.")

        while True:
            try:
                user_bet = round(int(input("Please your bet: ")), 2)
            except ValueError:
                print("\nPlease enter an integer.")
                continue
            else:
                if user_bet > cash_vault:
                    print("\nSorry, your bet exceeds your balance.")
                elif user_bet < 250:
                    print("\nSorry, we only accept minimum bets of 250.")
                else:
                    break

        # Create/ Shuffle the deck
        deck_cards.creating_deck()
        playing_deck = deck_cards.getting_deck()

        # Grab cards from the created deck.
        single_card = Card(playing_deck)

        # Player
        single_card.setting_cards()
        single_card.setting_cards()
        single_card.setting_value()
        player_list = single_card.getting_cards()

        print("\nPlayer's hand:", *player_list, sep='\n')

        # Dealer
        single_card.setting_cards_dealer()
        single_card.setting_value_dealer()
        dealer_list = single_card.getting_cards_dealer()

        print(f"\nDealer's hand:", *dealer_list, "*Face Down Card*", sep='\n')

        # Get values for options
        # print(single_card.getting_score(), "Player score 318")  # TODO
        player_value = single_card.getting_score()
        # print(player_value, "Player values line 311")  # TODO
        # print(single_card.getting_score_dealer(), "Dealer Score line 321")  # TODO
        dealer_ace = single_card.getting_ace_dealer()
        # print(dealer_ace, "Dealer Ace values line 314")  # TODO

        # Get choice for dealer respond.
        game_on = GameLogic(player_value, player_list, dealer_ace, user_bet)
        game_choice = game_on.getting_options()

        # game_choice = 'Split'
        user_side_piece = 0
        # Priming read for BlackJack
        player_score = single_card.getting_score()
        while True and game_choice != 'Zero' and user_side_piece > -1:

            # Normal Hit
            if game_choice == 'Hit':
                single_card.setting_cards()
                player_list = single_card.getting_cards()
                print("\nPlayer's hand:", *player_list, sep='\n')
                single_card.setting_value()
                single_card.setting_aces()
                player_score = single_card.getting_score()
                # print(player_score, "Player line 340")  # TODO
                if player_score > 21:
                    cash_vault -= user_bet
                    print("\nYou've busted, your total:", cash_vault)
                    break

            # Double
            if game_choice == 'Double':
                single_card.setting_cards()
                player_list = single_card.getting_cards()
                print("\nPlayer's hand:", *player_list, sep='\n')
                single_card.setting_value()
                player_score = single_card.getting_score()

                if player_score > 21:
                    cash_vault -= (2 * user_bet)
                    print("\nYou've busted, your total:", cash_vault)
                    break
                else:
                    game_choice = 'D Stand'

            # # Split
            # if game_choice == 'Split':
            #     new_list_a = []
            #     new_list_b = []
            #     new_list_a.append(player_list[0])
            #     new_list_b.append(player_list[1])
            #
            #     # First iteration of Split
            #     single_card.setting_split_a()
            #     single_card.setting_split_b()
            #
            #     new_list_a.append(''.join(single_card.getting_split_a()))
            #     new_list_b.append(''.join(single_card.getting_split_b()))
            #
            #     print(new_list_a)
            #     print(new_list_b)
            #
            #     if len(new_list_a) > 1:
            #         single_card.setting_split_value_a(new_list_a)
            #         split_a_list = single_card.getting_split_a()
            #         split_a_value = single_card.getting_split_a_value()
            #
            #         print("\nPlayer Split A:", *split_a_list, sep='\n')
            #
            #         split_a_on = GameLogic(split_a_value, split_a_list, 0, user_bet)
            #
            #         split_a_options = split_a_on.getting_options()
            #
            #         split_branch(split_a_list, split_a_value, split_a_options)

            # Insurance
            if game_choice == 'Insurance':
                game_on.setting_insurance_count()
                user_side_piece = game_on.getting_insurance_count()

            # Normal Stand
            if game_choice == 'Stand' or game_choice == 'D Stand':

                while True:
                    # print(player_score, "Black Jack")  # TODO

                    # If player say Stand off the bat (Edge-Case)
                    single_card.setting_aces()
                    player_score = single_card.getting_score()
                    if player_score > 21:
                        cash_vault -= user_bet
                        print("\nYou've busted, your total:", cash_vault)
                        break

                    # Dealer's card process
                    single_card.setting_cards_dealer()
                    dealer_list = single_card.getting_cards_dealer()
                    print("\nDealer's hand:", *dealer_list, sep='\n')

                    single_card.setting_value_dealer()
                    single_card.setting_aces_dealer()
                    dealer_score = single_card.getting_score_dealer()
                    # print(dealer_score, "Dealer Score line 408")  # TODO
                    # print(player_score, "Player score line 409")  # TODO

                    # Priming for Natural 21 (Insurance)
                    d_list = [i.split() for i in dealer_list]
                    dealer_black_jack = CARD_VALUES[d_list[0][0]] + CARD_VALUES[d_list[1][0]]
                    # print(dealer_black_jack, "Dealer Black line 384")  # TODO

                    if player_score == 21 and player_score > dealer_score:  # Hit
                        cash_vault += user_bet
                        print("\nBlackJack!  You've won!, payout 1:1, your total:", cash_vault)

                        if dealer_black_jack == 21 and user_side_piece:
                            cash_vault += 2 * user_side_piece
                            print("\nYou've won insurance!  Your total:",
                                  cash_vault)  # TODO try to reduce the insurance code line.

                        elif user_side_piece:
                            cash_vault -= user_side_piece
                            print("\nYou've lose insurance!  Your total:", cash_vault)
                        break

                    elif dealer_score > 21 or dealer_score == 17:  # Hit
                        cash_vault += 3 * (round(user_bet, 2) / 2)
                        print("\nYou've won!, payout 3:2, your total:", cash_vault)

                        if dealer_black_jack == 21 and user_side_piece:
                            cash_vault += 2 * user_side_piece
                            print("\nYou've won insurance!  Your total:",
                                  cash_vault)  # TODO try to reduce the insurance code line.

                        elif user_side_piece:
                            cash_vault -= user_side_piece
                            print("\nYou've lose insurance!  Your total:", cash_vault)
                        break

                    elif dealer_score > player_score:  # Hit
                        cash_vault -= user_bet
                        print("\nYou've lose, your total:", cash_vault)

                        if dealer_black_jack == 21 and user_side_piece:
                            cash_vault += 2 * user_side_piece
                            print("\nYou've won insurance!  Your total:",
                                  cash_vault)  # TODO try to reduce the insurance code line.

                        elif user_side_piece:
                            cash_vault -= user_side_piece
                            print("\nYou've lose insurance!  Your total:", cash_vault)
                        break

                    elif game_choice == 'D Stand' and dealer_score > 21 or dealer_score == 17:  # Double
                        cash_vault += 2 * user_bet
                        print("\nYou've won double, your total:", cash_vault)
                        break

                    elif game_choice == 'D Stand' and dealer_score > player_score:  # Double
                        cash_vault -= 2 * user_bet
                        print("\nYou've lost double, your total:", cash_vault)
                        break

                    elif player_score == dealer_score:  # Push
                        print("\nPush, your total:", cash_vault)

                        if dealer_black_jack == 21 and user_side_piece:
                            cash_vault += 2 * user_side_piece
                            print("\nYou've won insurance!  Your total:",
                                  cash_vault)  # TODO try to reduce the insurance code line.

                        elif user_side_piece:
                            cash_vault -= user_side_piece
                            print("You've lose insurance!  Your total:", cash_vault)
                        break

                    else:
                        pass
                break

            # Surrender
            if game_choice == 'Surrender':
                cash_vault -= user_bet / 2
                print("\nSurrender!  Your total:", cash_vault)
                break

            # Will continue asking for hit or spilt after entering a option(s) that let you continue.
            game_choice = game_on.normal_case()

        # Make sure the user still have cash before letting them continue
        if cash_vault > 0:
            game_on.setting_play()
            keep_playing = game_on.getting_play()
        elif cash_vault < 0:
            print("\nYou do not have the sufficient funds to continue.")
            break

    print("Thank you for playing, hope to see you again.")


# def split_branch(player_card_value, player_cards, player_decision):
#
#     # Split Stand
#     game_choice = 'Split'
#     user_side_piece = 0
#     # Priming read for BlackJack
#     player_score = single_card.getting_score()
#     while True and game_choice != 'Zero' and user_side_piece > -1:
#
#         # Normal Hit
#         if game_choice == 'Hit':
#             single_card.setting_cards()
#             player_list = single_card.getting_cards()
#             print("\nPlayer's hand:", *player_list, sep='\n')
#             single_card.setting_value()
#             single_card.setting_aces()
#             player_score = single_card.getting_score()
#             print(player_score, "Player line 340")
#             if player_score > 21:
#                 cash_vault -= user_bet
#                 print("\nYou've busted, your total:", cash_vault)
#                 break
#
#         # Double
#         if game_choice == 'Double':
#             single_card.setting_cards()
#             player_list = single_card.getting_cards()
#             print("\nPlayer's hand:", *player_list, sep='\n')
#             single_card.setting_value()
#             player_score = single_card.getting_score()
#
#             if player_score > 21:
#                 cash_vault -= (2 * user_bet)
#                 print("\nYou've busted, your total:", cash_vault)
#                 break
#             else:
#                 game_choice = 'D Stand'
#
#         # Insurance
#         if game_choice == 'Insurance':
#             game_on.setting_insurance_count()
#             user_side_piece = game_on.getting_insurance_count()
#
#         # Normal Stand
#         if game_choice == 'Stand' or game_choice == 'D Stand':
#
#             while True:
#                 print(player_score, "Black Jack")  # TODO
#
#                 # If player say Stand off the bat (Edge-Case)
#                 single_card.setting_aces()
#                 player_score = single_card.getting_score()
#                 if player_score > 21:
#                     cash_vault -= user_bet
#                     print("\nYou've busted, your total:", cash_vault)
#                     break
#
#                 # Dealer's card process
#                 single_card.setting_cards_dealer()
#                 dealer_list = single_card.getting_cards_dealer()
#                 print("\nDealer's hand:", *dealer_list, sep='\n')
#
#                 single_card.setting_value_dealer()
#                 single_card.setting_aces_dealer()
#                 dealer_score = single_card.getting_score_dealer()
#                 print(dealer_score, "Dealer Score line 408")
#                 print(player_score, "Player score line 409")
#
#                 # Priming for Natural 21 (Insurance)
#                 d_list = [i.split() for i in dealer_list]
#                 dealer_black_jack = CARD_VALUES[d_list[0][0]] + CARD_VALUES[d_list[1][0]]
#                 print(dealer_black_jack, "Dealer Black line 384")
#
#                 if player_score == 21 and player_score > dealer_score:  # Hit
#                     cash_vault += user_bet
#                     print("\nBlackJack!  You've won!, payout 1:1, your total:", cash_vault)
#
#                     if dealer_black_jack == 21 and user_side_piece:
#                         cash_vault += 2 * user_side_piece
#                         print("You've won insurance!  Your total:",
#                               cash_vault)
#
#                     elif user_side_piece:
#                         cash_vault -= user_side_piece
#                         print("You've lose insurance!  Your total:", cash_vault)
#                     break
#
#                 elif dealer_score > 21 or dealer_score == 17:  # Hit
#                     cash_vault += 3 * (round(user_bet, 2) / 2)
#                     print("\nYou've won!, payout 3:2, your total:", cash_vault)
#
#                     if dealer_black_jack == 21 and user_side_piece:
#                         cash_vault += 2 * user_side_piece
#                         print("You've won insurance!  Your total:",
#                               cash_vault)
#
#                     elif user_side_piece:
#                         cash_vault -= user_side_piece
#                         print("You've lose insurance!  Your total:", cash_vault)
#                     break
#
#                 elif dealer_score > player_score:  # Hit
#                     cash_vault -= user_bet
#                     print("\nYou've lose, your total:", cash_vault)
#
#                     if dealer_black_jack == 21 and user_side_piece:
#                         cash_vault += 2 * user_side_piece
#                         print("You've won insurance!  Your total:",
#                               cash_vault)
#
#                     elif user_side_piece:
#                         cash_vault -= user_side_piece
#                         print("You've lose insurance!  Your total:", cash_vault)
#                     break
#
#                 elif game_choice == 'D Stand' and dealer_score > 21 or dealer_score == 17:  # Double
#                     cash_vault += 2 * user_bet
#                     print("\nYou've won double, your total:", cash_vault)
#                     break
#
#                 elif game_choice == 'D Stand' and dealer_score > player_score:  # Double
#                     cash_vault -= 2 * user_bet
#                     print("\nYou've lost double, your total:", cash_vault)
#                     break
#
#                 elif player_score == dealer_score:  # Push
#                     print("\nPush, your total:", cash_vault)
#
#                     if dealer_black_jack == 21 and user_side_piece:
#                         cash_vault += 2 * user_side_piece
#                         print("You've won insurance!  Your total:",
#                               cash_vault)
#
#                     elif user_side_piece:
#                         cash_vault -= user_side_piece
#                         print("You've lose insurance!  Your total:", cash_vault)
#                     break
#
#                 else:
#                     pass
#             break


main()

# TODO We need to find a way to combine the usage of the split and normal functions, because it looks way too busy.
# TODO Need to make an entire module for split.

#  TODO sometimes it does not display the correct events when fund == 0
