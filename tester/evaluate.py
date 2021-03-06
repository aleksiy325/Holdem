import platform
import traceback
from itertools import combinations_with_replacement
from random import shuffle

from poker_game import PokerGame
from naive_bots import *
from bots import RFT, RaiseTwentyBot

MAX_PLAYERS = 4
NUM_SHUFFLES = 1
NUM_TESTS = 1

def evaluate(bot_under_test):

    class TestBot(bot_under_test):
        pass

    seed = 0
    results = {}
    bots = [FoldBot,RandomBet,MinBet,AllIn,RandomBot,RaiseTwentyBot]
    bots += [bot_under_test]

    for num_players in range(1,MAX_PLAYERS-1):
        results[str(num_players) + "_players"] = []
        for combination in combinations_with_replacement(bots,num_players):
            test_group = list(combination) + [TestBot]
            for i in range(NUM_SHUFFLES):
                shuffle(test_group)
                for i in range(NUM_TESTS):
                    game = PokerGame(bots=test_group, seed=seed)
                    results[str(num_players) + "_players"].append(game.run())
                    seed += 1


    testclasses = bots + [TestBot]

    win_percentages = {}
    total_winnings = {}
    winnings_over_time = {}

    for player_count, outcome in results.iteritems():
        wincounts = dict(zip(testclasses, [0]*len(testclasses)))
        winnings = dict(zip(testclasses, [0]*len(testclasses)))
        winnings_array = dict(zip(testclasses, [[]]*len(testclasses)))

        running_winnings = 0

        for elem in outcome:
            for botclass in testclasses:
                if isinstance(elem[0],botclass):
                    wincounts[botclass] += 1
                    winnings[botclass] += elem[1]

                    running_winnings += elem[1]
                    winnings_array[botclass].append(running_winnings)
                else:
                    winnings_array[botclass].append(running_winnings)

        for testclass in testclasses:
            wincounts[testclass] /= len(outcome)

        total_winnings[player_count] = winnings
        win_percentages[player_count] = wincounts
        winnings_over_time[player_count] = winnings_array



    return win_percentages, total_winnings, winnings_over_time


def main():
    results = evaluate(AllIn)
    import matplotlib.pyplot as plt

    print(str(results[0]) + "\n\n")
    print(str(results[1])

    for bot_count, bot_dict in results[2].iteritems():

        for player, list in bot_dict.iteritems():
            x_axis = range(len(list))
            plt.plot(x_axis, list, label=str(player))
        plt.xlabel('Radius/Side')
        plt.ylabel('Area')
        plt.title('Area of Shapes')
        plt.legend()
        plt.show()



if __name__ == "__main__":
    import sys
    try:
        sys.exit(main())
    except Exception, e:
        print ""
        traceback.print_exc()
    if platform.system() == 'Windows':
        raw_input('\nPress enter to continue')
