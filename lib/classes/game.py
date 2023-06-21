class Game:
    def __init__(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise Exception

        self._results = []
        self._players = []

    @property
    def title(self):
        return self._title

    def results(self, new_result=None):
        from classes.result import Result

        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results

    def players(self, new_player=None):
        from classes.player import Player

        if new_player and isinstance(new_player, Player):
            self._players.append(new_player)
        return self._players

    def average_score(self, player):
        return sum(
            [result.score for result in self._results if result.player == player]
        ) / len(self._results)
