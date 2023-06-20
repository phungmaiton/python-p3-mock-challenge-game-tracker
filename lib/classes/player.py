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
        from classes.result import Result

        for result in Result.all:
            if self == result.player and game == result.game:
                return True
        else:
            return False

    def num_times_played(self, game):
        from classes.result import Result

        game_list = [
            result.game
            for result in Result.all
            if result.game == game and result.player == self
        ]
        return len(game_list)

    @classmethod
    def highest_scored(cls, game):
        if cls.all:
            max_player = None
            max_score = 0
            for player in cls.all:
                if game.average_score(player) > max_score:
                    max_player = player
                    max_score = game.average_score(player)
            return max_player
        else:
            return None
