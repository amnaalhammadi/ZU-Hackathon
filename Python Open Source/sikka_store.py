def general_repairs(houses, hotels):
    return 25 * houses + 100 * hotels


def street_repairs(houses, hotels):
    return 40 * houses + 115 * hotels


def birthday(playercount):
    return 10 * playercount


chance = {
    'Advance to "Go"': {
        "action": "move+",
        "value": 0
    },
    'Go to financial literacy. Move directly to the financial literacy. Do pass "Go". Do collect 200 AED': {
        "action": "move",
        "value": 10
    },
    'Advance to Dubai Aquarium & Underwater Zoo. If you pass "Go" collection 200 AED': {
        "action": "move+",
        "value": 11
    },
    'Take a trip to Emirates Towers Station and if you pass "Go" collect 200 AED': {
        "action": "move+",
        "value": 5
    },
    'Advance to Al Ain Zoo. If you pass "Go" collect 200 AED': {
        "action": "move+",
        "value": 24
    },
    'Advance to Mangrove National Park': {
        "action": "move",
        "value": 39
    },
    'Go back three spaces': {
        "action": "back",
        "value": 3
    },
    'Make general repairs on all of your houses. For each house pay 25 AED. For each hotel pay 100 AED': {
        "action": "payf",
        "value": general_repairs
    },
    'You are assessed for street repairs: 40 AED per house, 115 AED per hotel': {
        "action": "payf",
        "value": street_repairs
    },
    'Pay school fees of 150 AED': {
        "action": "pay",
        "value": 150
    },
    '"Coffee in charge" fine 20 AED': {
        "action": "pay",
        "value": 20
    },
    'Speeding fine 15 AED': {
        "action": "pay",
        "value": 15
    },
    'Your building loan matures. Receive 150 AED': {
        "action": "receive",
        "value": 150
    },
    'You have won a crossword competition. Collect 100 AED': {
        "action": "receive",
        "value": 100
    },
    'Bank pays you dividend of 50 AED': {
        "action": "receive",
        "value": 50
    },
}

community = {
    'Advance to "Go"': {
        "action": "move+",
        "value": 0
    },
    'Go back to Yas mall': {
        "action": "move",
        "value": 1
    },
    'Go to the financial literacy. Move directly to the financial literacy area. Do pass "Go". Do collect 200 AED': {
        "action": "move",
        "value": 10
    },
    'Pay hospital 100 AED': {
        "action": "pay",
        "value": 100
    },
    'Doctor\'s fee. Pay 50 AED': {
        "action": "pay",
        "value": 50
    },
    'Pay your insurance premium 50 AED': {
        "action": "pay",
        "value": 50
    },
    'Bank error in your favour. Collect 200 AED': {
        "action": "receive",
        "value": 200
    },
    'Annuity matures. Collect 100 AED': {
        "action": "receive",
        "value": 100
    },
    'You inherit 100 AED': {
        "action": "receive",
        "value": 100
    },
    'From sale of stock you get 50 AED': {
        "action": "receive",
        "value": 50
    },
    'Receive interest on 7% preference shares: 25 AED': {
        "action": "receive",
        "value": 25
    },
    'Income tax refund. Collect 20 AED': {
        "action": "receive",
        "value": 20
    },
    'You have won second prize in a beauty contest. Collect 10 AED': {
        "action": "receive",
        "value": 10
    },
    'It is your birthday. Collect 10 AED from each player': {
        "action": "birthday",
        "value": 10
    },
    'Pay a 10 AED fine or take a "Chance"': {
        "action": "pay",
        "value": 10
    }
}

properties = [
    1, 3, 5, 6, 8, 9, 11, 13, 14, 15, 16, 18, 19, 21, 23, 24, 25, 26, 27, 29, 31, 32, 34, 35, 37, 39
]

utilities = [
    12, 28
]

board = [
    'Go',
    'Yas Mall',
    'Sikka Community',
    'Burj Khalifa',
    'Developer hand-off',
    'Emirates youth',
    'Emirates Towers',
    'IMG Worlds of Adventure',
    'Chance',
    'Dubai Miracle Garden',
    'Burj Arab',
    'In financial literacy',
    'Dubai Aquarium & Underwater Zoo',
    'Professional Plan',
    'Dubai Frame',
    'Abu Dhabi Mall',
    'Constraints',
    'Zayed Centre',
    'Sikka Community',
    'Ferrari World Abu Dhabi',
    'Yas Marina Circuit',
    'Cofee Break',
    'Sheikh Zayed Mosque',
    'Chance',
    'Louvre Museum Abu Dhabi',
    'Al Ain Zoo',
    'Components',
    'Emirates Palace',
    'Emirates Park Zoo',
    'Organization Plan',
    'Yas Island',
    'Go to the financial literacy',
    'Yas Water World',
    'Warner Bros World',
    'Sikka Community',
    'Museum of the Future',
    'Expo 2020',
    'Chance',
    'Mangrove National Park',
    'Share your Coffee',
    'Etihad Towers'
]

property_info = [
  {
    "colour": "light purple",
    "index": 1,
    "name": "Yas Mall",
    "value": 600,
    "house_price": 30,
    "rent": [2, 10, 30, 90, 160, 250]
  },
  {
    "colour": "light purple",
    "index": 3,
    "name": "Burj Khalifa",
    "value": 600,
    "house_price": 30,
    "rent": [4, 20, 60, 180, 320, 450]
  },
  {
    "colour": "Station",
    "index": 5,
    "name": "Emirates Towers",
    "value": 200,
    "house_price": None,
    "rent": None
  },
  {
    "colour": "Light blue",
    "index": 6,
    "name": "IMG Worlds of Adventure",
    "value": 100,
    "house_price": 50,
    "rent": [6, 30, 90, 270, 400, 550]
  },
  {
    "colour": "Light blue",
    "index": 8,
    "name": "Dubai Miracle Garden",
    "value": 100,
    "house_price": 50,
    "rent": [6, 30, 90, 270, 400, 550]
  },
  {
    "colour": "Light blue",
    "index": 9,
    "name": "Burj Arab",
    "value": 120,
    "house_price": 60,
    "rent": [8, 40, 100, 300, 450, 600]
  },
  {
    "colour": "purple",
    "index": 11,
    "name": "Dubai Aquarium & Underwater Zoo",
    "value": 140,
    "house_price": 70,
    "rent": [10, 50, 150, 450, 625, 750]
  },
  {
    "colour": "purple",
    "index": 13,
    "name": "Dubai Frame",
    "value": 140,
    "house_price": 70,
    "rent": [10, 50, 150, 450, 625, 750]
  },
  {
    "colour": "purple",
    "index": 14,
    "name": "Abu Dhabi Mall",
    "value": 160,
    "house_price": 80,
    "rent": [12, 60, 180, 500, 700, 900]
  },
  {
    "colour": "Station",
    "index": 15,
    "name": "Constraints",
    "value": 200,
    "house_price": None,
    "rent": None
  },
  {
    "colour": "Orange",
    "index": 16,
    "name": "Zayed Centre",
    "value": 180,
    "house_price": 90,
    "rent": [14, 70, 200, 550, 750, 950]
  },
  {
    "colour": "Orange",
    "index": 18,
    "name": "Ferrari World Abu Dhabi",
    "value": 180,
    "house_price": 90,
    "rent": [14, 70, 200, 550, 750, 950]
  },
  {
    "colour": "Orange",
    "index": 19,
    "name": "Yas Marina Circuit",
    "value": 200,
    "house_price": 100,
    "rent": [16, 80, 220, 600, 800, 1000]
  },
  {
    "colour": "Red",
    "index": 21,
    "name": "Sheikh Zayed Mosque",
    "value": 220,
    "house_price": 110,
    "rent": [18, 90, 250, 700, 875, 1050]
  },
  {
    "colour": "Red",
    "index": 23,
    "name": "Louvre Museum Abu Dhabi",
    "value": 220,
    "house_price": 110,
    "rent": [18, 90, 250, 700, 875, 1050]
  },
  {
    "colour": "Red",
    "index": 24,
    "name": "Al Ain Zoo",
    "value": 240,
    "house_price": 120,
    "rent": [20, 100, 300, 750, 925, 1100]
  },
  {
    "colour": "Station",
    "index": 25,
    "name": "Components",
    "value": 200,
    "house_price": None,
    "rent": None
  },
  {
    "colour": "Yellow",
    "index": 26,
    "name": "Emirates Palace",
    "value": 260,
    "house_price": 130,
    "rent": [22, 110, 330, 800, 975, 1150]
  },
  {
    "colour": "Yellow",
    "index": 27,
    "name": "Emirates Park Zoo",
    "value": 260,
    "house_price": 130,
    "rent": [22, 110, 330, 800, 975, 1150]
  },
  {
    "colour": "Yellow",
    "index": 29,
    "name": "Yas Island",
    "value": 280,
    "house_price": 140,
    "rent": [22, 120, 360, 850, 1025, 1200]
  },
  {
    "colour": "Green",
    "index": 31,
    "name": "Yas Water World",
    "value": 300,
    "house_price": 150,
    "rent": [26, 130, 390, 900, 1100, 1275]
  },
  {
    "colour": "Green",
    "index": 32,
    "name": "Warner Bros World",
    "value": 300,
    "house_price": 150,
    "rent": [26, 130, 390, 900, 1100, 1275]
  },
  {
    "colour": "Green",
    "index": 34,
    "name": "Museum of the Future",
    "value": 320,
    "house_price": 160,
    "rent": [28, 150, 450, 1000, 1200, 1400]
  },
  {
    "colour": "Station",
    "index": 35,
    "name": "expo 2020",
    "value": 200,
    "house_price": None,
    "rent": None
  },
  {
    "colour": "Dark blue",
    "index": 37,
    "name": "Mangrove National Park",
    "value": 350,
    "house_price": 175,
    "rent": [35, 175, 500, 1100, 1300, 1500]
  },
  {
    "colour": "Dark blue",
    "index": 39,
    "name": "Etihad Towers",
    "value": 400,
    "house_price": 200,
    "rent": [50, 200, 600, 1400, 1700, 2000]
  }
]