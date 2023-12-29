from espn_api_client import ESPNApiClient
from league_data_transformer import LeagueDataTransformer
from postgres_api import PostgresApi

if __name__ == '__main__':
    current_week = 7
    # postgres_api = PostgresApi()
    # postgres_api.delete_table()
    # postgres_api.create_table()

    espn_api = ESPNApiClient(league_year=2023, league_id=973157822)

    league = espn_api.get_league_data()
    # print(league.box_scores(12)[0].home_lineup[0])
    # print(league.box_scores(12)[0].home_lineup[0].onTeamId)
    # print(league.box_scores(12)[0].away_lineup[1].onTeamId)
    # # print(league.box_scores(12)[0].home_lineup[0].stats)
    print(league.box_scores(12)[0].away_lineup[0].stats)
    # print(type(league.box_scores(12)[0].away_lineup[0].stats))

    # lineups = league.box_scores(12)[0].away_lineup
    # for lineup in lineups:
    #     print(lineup.slot_position)
    #     print(lineup.position)
    #     print("-----------")

    # league_data_transformer = LeagueDataTransformer(league)

    # postgres_api.insert_data(league_data_transformer.get_flat_data_list(current_week))
