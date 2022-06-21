import random
from matplotlib import pyplot as plt
import math


def main():
    nPlayers = int(input('how many players should play?'))
    money = int(input('how much money should each player have?'))
    winningProb = float(input('what should the winning probability be? (in percent)'))
    minPrice = int(input('what should be the minimum amount for a bet?'))

    players = list(range(nPlayers))
    nGames = calculateNResults(money=money, minPrice=minPrice)
    results = [0] * (nGames + 1)
    results = conductExperiment(players = players, results = results, winningProb = winningProb)

    nLoosingPlayers = results[-1]
    loosingProb = calculateLoosingProbability(lostPlayers=nLoosingPlayers, totalPlayers=nPlayers)
    casinoEarnigns = calculateTotalMoneyTransaction(lostPlayers=nLoosingPlayers, totalPlayers=nPlayers, nGames=nGames, minPrice=minPrice)

    print(f'probability of loosing: {loosingProb}\Money earned by casino: {casinoEarnigns}€\Money earned by casino per person: {casinoEarnigns / nPlayers}€')
    plotResults(results)
 


def calculateNResults(money, minPrice):

    return math.floor(math.log2((money / minPrice) + 1))


def conductExperiment(players, results, winningProb):

    for i in range(len(results) - 1):
        for j in range(len(players) - 1, -1, -1):
            randomNumber = random.randint(1, 1000) / 10

            if(randomNumber <= winningProb):
                results[i] += 1
                players.remove(players[j])

    results[-1] = len(players)

    print(results)
    return results


def plotResults(results):

    plt.bar(range(len(results)), results)
    
    plt.title('Can you defeat a casino?')
    plt.xlabel('Number of games')
    plt.ylabel('outcomes')
    plt.show()
    

def calculateLoosingProbability(lostPlayers, totalPlayers):

    return lostPlayers / totalPlayers


def calculateTotalMoneyTransaction(lostPlayers, totalPlayers, nGames, minPrice):

    winningPlayers = totalPlayers - lostPlayers

    lostMoney = winningPlayers * minPrice
    wonMoney = (lostPlayers * (2**(nGames) - 1)) * minPrice

    totalMoney = wonMoney - lostMoney
    print(totalMoney)
    return totalMoney



if(__name__ == "__main__"):
    main()
