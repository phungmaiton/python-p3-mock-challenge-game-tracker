class Player:
    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception

    def results(self, new_result=None):
        from classes.result import Result

        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results

    def games_played(self, new_game=None):
        from classes.game import Game

        if new_game and isinstance(new_game, Game):
            self._games_played.append(new_game)
        return self._games_played

    def played_game(self, game):
        if game in self._games_played:
            return True
        else:
            return False

    def num_times_played(self, game):
        return len(
            [game_played for game_played in self._games_played if game_played == game]
        )

    @classmethod
    def highest_scored(cls, game):
        from classes.game import Game

        if len(cls.all) > 0:
            avg_score = {}

            for player in cls.all:
                avg = Game.average_score(game, player)
                avg_score[player] = avg

            return max(avg_score, key=avg_score.get)
        else:
            return None
