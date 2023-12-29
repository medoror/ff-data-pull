import json
class LeagueDataTransformer:

    def __init__(self, league, current_week):
        self.league = league
        self.current_week = current_week

    def generate_scoring_data(self):
        box_scores = self.league.box_scores(self.current_week)
        payload = []
        for box_score in box_scores:
            self.extract_team_data(box_score.home_lineup, payload)
            self.extract_team_data(box_score.away_lineup, payload)

        print(json.dumps(payload, indent=4))
        return payload

    def extract_team_data(self, team, payload):
        for player in team:
            if player.onTeamId == 0:
                continue
            team_id = player.onTeamId
            points = player.points
            stats = self.process_player_stats(player.stats)
            slot_position = player.slot_position
            position = player.position
            payload.append((points, team_id, stats, slot_position, position))

    def process_player_stats(self, json_payload):
        if not json_payload:
            return {}
        json_payload = json_payload[self.current_week]
        keys_to_remove = ['projected_breakdown', 'projected_avg_points', 'projected_points', 'avg_points']

        # using dictionary comprehension to construct new dictionary
        cleaned_payload = {k: v for k, v in json_payload.items() if k not in keys_to_remove}

        return cleaned_payload