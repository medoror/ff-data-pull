import os

from espn_api_client import ESPNApiClient
from league_data_transformer import LeagueDataTransformer
from postgres_api import PostgresApi

if __name__ == '__main__':
    database_url = os.getenv("DATABASE_URL")
    league_year = os.getenv("LEAGUE_YEAR")
    league_id = os.getenv("LEAGUE_ID")

    current_week = 7

    postgres_api = PostgresApi(database_url)
    postgres_api.delete_table()
    postgres_api.create_table()

    espn_api = ESPNApiClient(league_year=league_year, league_id=league_id)

    league = espn_api.get_league_data()

    league_data = LeagueDataTransformer(league, current_week)

    payload = league_data.generate_scoring_data()
    postgres_api.insert_fantasy_football_data(payload)


    # print(league.box_scores(12)[0].home_lineup[0])
    # print(league.box_scores(12)[0].home_lineup[0].onTeamId)
    # print(league.box_scores(12)[0].away_lineup[1].onTeamId)
    # # print(league.box_scores(12)[0].home_lineup[0].stats)
    # print(league.box_scores(12)[0].away_lineup[0].stats)
    # print(type(league.box_scores(12)[0].away_lineup[0].stats))

    # lineups = league.box_scores(12)[0].away_lineup
    # for lineup in lineups:
    #     print(f"slot: {lineup.slot_position}")
    #     print(f"position: {lineup.position}")
    #     print("-----------")

    # box_scores = league.box_scores(12)
    # for box_score in box_scores:
    #     print(f"id: {box_score.home_lineup[0].onTeamId} name: {box_score.home_team}")
    #     print(f"id: {box_score.away_lineup[0].onTeamId} name: {box_score.away_team}")
    #     print("-----------")

    # league_data_transformer = LeagueDataTransformer(league)

    # postgres_api.insert_data(league_data_transformer.get_flat_data_list(current_week))
