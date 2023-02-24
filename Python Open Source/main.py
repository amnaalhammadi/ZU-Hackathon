from sikka_board import Board

b = Board(player_count=4, log=True)  # only 4 players can play
b.play(turns=10)  # the game will stop after 200 turns
