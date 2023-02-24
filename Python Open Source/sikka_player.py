import random, time
import numpy as np

def roll(count=0, doubles=0):
    if doubles == 3:
        return False
    roll_count = 0
    double_roll = False
    for _ in range(2):
        choice = random.choice([1, 2, 3, 4, 5, 6])
        if roll_count == choice:
            double_roll = True
        roll_count += choice
    
    if double_roll:
        again = roll(count + roll_count, doubles + 1)
        return again
    else:
        return count + roll_count


class Property:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None

    def calculate_rent(self):
        if self.owner is None:
            return 0
        else:
            return self.rent


class SuperPositionProperty(Property):
    def __init__(self, name, price, rent_card):
        super().__init__(name, price, None)
        self.rent_card = rent_card
        self.current_rent = 0

    def calculate_rent(self):
        if self.owner is None:
            return 0
        else:
            return self.current_rent

    def collapse_superposition(self):
        rent_values = list(self.rent_card.keys())
        probabilities = list(self.rent_card.values())
        prob_sum = sum(probabilities)
        normalized_probabilities = [p/prob_sum for p in probabilities]
        index = np.random.choice(len(rent_values), p=normalized_probabilities)
        self.current_rent = rent_values[index] / 10
        print(f"Rent value collapsed to {self.current_rent} AED.")


class Player:
    def __init__(self, board):
        # Board data
        self.board = board
        self.player_id = len(self.board.players)

        self.rent = 0

        # Position on the board from 0-39
        self.position = 0
        self.properties = []

        # Starting money
        self.money = 500

        # Status: 1 = Playing, 0 = Bankrupt
        self.status = 1

        # Turns spent in financial literacy or "None"
        self.financial_literacy = None

        # Get out of financial_literacy free cards
        self.chance_financial_literacy_card = False
        self.community_chest_financial_literacy_card = False

        # Add to player list
        self.board.add_player(self)

    def pay(self, x):
        self.money -= x
        if self.money < 0:
            self.bankrupt()

    def receive(self, x):
        self.money += x

    def bankrupt(self):
        self.status = 0
        self.money = 0
        for k in self.board.properties:
            property_ = self.board.properties[k]
            if property_["owned"] == self.player_id:
                self.board.log("Lost %s" % self.board.properties[k]["name"])
                self.board.properties[k]["owned"] = None
                self.board.houses += self.board.properties[k]["houses"]
                self.board.properties[k]["houses"] = 0
                self.board.hotels += 1 if self.board.properties[k]["hotel"] else 0
                self.board.properties[k]["hotel"] = False
        self.board.log("\033[1m\033[4mIs bankrupt\033[0m")
        if self.board.log_:
            time.sleep(5)

    def chance_community_chest(self):
        location = self.board.squares[self.position]

        pile = None
        if location == "Chance":
            pile = "chance_set"
        elif location == "Community":
            pile = "community_set"

        if pile != None:
            card = getattr(self.board, pile)[0]
            getattr(self.board, pile).append(card)
            getattr(self.board, pile).pop(0)

            starting = self.position

            # Movement
            if card["action"] == "move" or card["action"] == "move+":
                self.position = card["value"]
                if card["value"] == 10:
                    self.financial_literacy = 0
            elif card["action"] == "back":
                self.position = self.position - card["value"]

            # Money
            if card["action"] == "move+" and self.position < starting:
                self.money += 200

            if card["action"] == "pay":
                self.pay(card["value"])

            if card["action"] == "receive":
                self.money += card["value"]

            if card["action"] == "birthday":
                self.money += len(self.board.players) * 10
                for k in self.board.players:
                    self.board.players[k].pay(10)

                self.board.log("It's my birthday")
                if self.board.log_:
                    time.sleep(1)

            # financial_literacy
            if card["action"] == "financial_literacy card":
                del getattr(self.board, pile)[-1]
                if location == "Chance":
                    self.chance_financial_literacy_card = True
                elif location == "Community":
                    self.community_chest_financial_literacy_card = True

    def buy_property(self):
        property_ = self.board.properties[self.position]

        # If the player has over double the price of the property
        # or over £600, buy the property
        if self.money > 600 or self.money > (2 * property_["value"]):
            self.pay(property_["value"])
            self.board.properties[self.position]["owned"] = self.player_id

    def build_houses(self):

        # Check which sets are owned by the player
        sets = {}
        for k in self.board.properties:
            property_ = self.board.properties[k]
            if property_["owned"] == self.player_id and property_["colour"] != "Station":
                if property_["colour"] in sets.keys():
                    sets[property_["colour"]].append(property_)
                else:
                    sets[property_["colour"]] = [property_]
        for set_colour in sets:
            set_ = sets[set_colour]
            cards_in_set = 3
            if set_colour == "Brown" or set_colour == "Dark blue":
                cards_in_set = 2

            # Check if the set is complete
            if len(set_) == cards_in_set:
                for p in set_:
                    self.build(p)

    def build(self, property_):

        # Minimum money left over after building houses
        base_money = 200

        if property_["hotel"] == True:
            return

        if property_["houses"] == 0:
            max_houses = 3
        else:
            max_houses = 5

        houses = max_houses - property_["houses"]

        if houses != 0 and self.money / property_["house_price"] > houses:
            if max_houses == 5 and self.board.hotels > 0:
                if self.money - (property_["house_price"] * houses) > base_money:
                    self.board.hotels -= 1
                    self.pay(property_["house_price"] * houses)
                    properties = self.board.properties
                    for k in properties:
                        if properties[k]["name"] == property_["name"]:
                            self.board.houses += properties[k]["houses"]
                            self.board.log("Built a hotel on %s. %s houses left." % (property_["name"], self.board.houses))
                            if self.board.log_:
                                time.sleep(3)
                            properties[k]["houses"] = 0
                            properties[k]["hotel"] = True
                    self.board.properties = properties
            elif max_houses < 5:
                houses = min(self.board.houses, houses)
                if houses != 0 and self.money - (property_["house_price"] * houses) > base_money:
                    self.board.houses -= houses
                    self.board.log("Built %s house(s) on %s. %s houses left." % (houses, property_["name"], self.board.houses))
                    if self.board.log_:
                        time.sleep(1.5)
                    self.pay(property_["house_price"] * houses)
                    properties = self.board.properties
                    for k in properties:
                        if properties[k]["name"] == property_["name"]:
                            properties[k]["houses"] += houses
                    self.board.properties = properties

    def pay_rent(self):
        owner = self.board.players[self.board.properties[self.position]["owned"]]
        property_ = self.board.properties[self.position]
        rent_multiplier = 5 if property_["hotel"] else property_["houses"]
        if property_["rent"]:
            owner.receive(property_["rent"][rent_multiplier])
            self.pay(property_["rent"][rent_multiplier])

    def move(self):
        dice = roll()
        self.board.log("Dice total: %s" % dice)
        if dice != False:
            self.position = (self.position + dice)  % 40
        else: # financial_literacy
            self.financial_literacy = 0
            self.position = 10

        self.board.log("Moved to \033[1m%s\033[0m" % self.board.squares[self.position])

        self.board.log("Total money: %s AED" % self.money)

        if self.position == 30:
            self.financial_literacy = 0
            self.position = 10

    def play(self):
        if self.status == 0:
            return

        self.board.log("\033[1m\033[4mPlayer %s's turn\033[0m" % str(self.player_id + 1))

        if self.financial_literacy != None and self.financial_literacy < 3:
            if self.chance_financial_literacy_card:
                self.chance_financial_literacy_card = False
                self.board.chance_set.append({"action": "financial_literacy card","value": None})
                self.board.log("Used get out of financial_literacy free card")
                self.financial_literacy = None
            elif self.community_chest_financial_literacy_card:
                self.community_chest_financial_literacy_card = False
                self.board.community_set.append({"action": "financial_literacy card","value": None})
                self.board.log("Used get out of financial_literacy free card")
                self.financial_literacy = None
            elif self.money > 150:
                self.pay(50)
                self.board.log("Paid $50 to get out of financial_literacy")
                self.financial_literacy = None
            else:
                self.board.log("Turn spent in financial_literacy")
                self.financial_literacy += 1
                return
        elif self.financial_literacy != None:
            self.financial_literacy = None

        starting = self.position
        self.move()

        if self.position < starting:
            self.money += 200

        self.chance_community_chest()

        if self.position in self.board.properties.keys():
            if self.board.properties[self.position]["owned"] == None:
                self.buy_property()
            else:
                self.pay_rent()

        self.position = self.position % 40

        self.build_houses()

    def land_on_property(self, property):
        if isinstance(property, SuperPositionProperty):
            print(f"{self.player_id} landed on a property with superposition value.")
            rent_card = property.rent_card
            rent_values = list(rent_card.keys())
            probabilities = list(rent_card.values())
            print(f"Possible rent values and their probabilities: {rent_card}")
            roll = self.roll_dice()
            property.collapse_superposition(roll)
        else:
            self.rent = property.calculate_rent()
            print(f"{self.player_id} landed on {property.name}. Rent value is {self.rent} AED.")
            self.pay_rent(property.owner, self.rent)