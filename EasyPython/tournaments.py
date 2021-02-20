# def tournamentWinner(competitions, results):
#     # Write your code here.
#     homeTeam = 1
#     print(results)
#     currentBestTeam = ""
#     scores = {currentBestTeam: 0}
#
#     for idx, competition in enumerate(competitions):
#         result = results[idx]
#         home, away = competition
#         winningTeam = home if result == homeTeam else away
#
#         updateScores(winningTeam, 3, scores)
#         if scores[winningTeam] > scores[currentBestTeam]:
#             currentBestTeam = winningTeam
#     return currentBestTeam
#
# def updateScores(team, points, scores):
#     if team not in scores:
#         scores[team] = 0
#     scores[team] += points
# tournamentWinner([["one","two"],["one","three"],["Two","three"]],[0,0,1])
























def tournamentWinner(competitions, results):
    # Write your code here.
    homeTeam = 1
    awayTeam = 0
    winningTeam = ""
    Score = {winningTeam:""}
    # keep in mind that results array is the same length as competitions
    for indx, comp in enumerate(competitions):
        result = results[idx]
        home, away = comp
        winner = home if result == homeTeam else awayTeam

        updateBest(winner, 3, scores)
        if scores[winner] > scores[winningTeam]:
            winninTeam = winner

    return winningTeam

    def updateBest(team, points, scores):
        if team not in scores:
            scores[team] = 0
        scores += points
