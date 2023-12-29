from espn_api.football import League


class ESPNApiClient:

    def __init__(self, league_year=2023, league_id=""):
        self.league_year = league_year
        self.league_id = league_id

    def get_league_data(self):
        return League(league_id=self.league_id, year=self.league_year)
