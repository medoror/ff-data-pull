import unittest
from unittest.mock import patch, MagicMock
from league_data_transformer import LeagueDataTransformer
import json
from full_player1_stats import p1_stats
from full_player2_stats import p2_stats


class TestLeagueDataTransformer(unittest.TestCase):

    @patch('espn_api.football.League')
    def setUp(self, mock_league):
        mock_player1 = MagicMock()
        # mock_player1.name = 'Player 1'
        mock_player1.points = 12
        mock_player1.onTeamId = 8
        mock_player1.position = 'QB'
        mock_player1.slot_position = 'OP'
        mock_player1.stats = p1_stats

        mock_player2 = MagicMock()
        # mock_player2.name = 'Player 2'
        mock_player2.points = 114
        mock_player2.onTeamId = 6
        mock_player2.position = 'TE'
        mock_player2.slot_position = 'BE'
        mock_player2.stats = p2_stats

        # Create the mock player objects
        mock_players_home = [mock_player1]
        mock_players_away = [mock_player2]

        # Create the mock box score objects
        mock_box_score_home = MagicMock()
        mock_box_score_away = MagicMock()

        mock_box_score_home.home_lineup = mock_players_home
        mock_box_score_away.away_lineup = mock_players_away

        # Create the mock league object
        mock_league = MagicMock()

        # Define the behavior for the box_scores method
        # to return our mock box score object
        mock_league.box_scores = MagicMock(return_value=[mock_box_score_home, mock_box_score_away])

        # Lounge mock league object into the class we're testing
        self.transformer = LeagueDataTransformer(mock_league, 12)

    def test_process_player_stats(self):
        self.assertEqual(self.transformer.process_player_stats(p1_stats),
                         {'points': 27.3, 'breakdown': {'rushingAttempts': 16.0, 'rushingYards': 91.0, 'rushingTouchdowns': 1.0, '27': 18.0, '28': 9.0, '29': 4.0, '30': 3.0, '31': 1.0, '33': 3.0, '34': 1.0, 'rushingYardsPerAttempt': 5.688, 'receivingReceptions': 3.0, 'receivingYards': 32.0, 'receivingTouchdowns': 1.0, '47': 6.0, '48': 3.0, '49': 1.0, '50': 1.0, 'receivingTargets': 6.0, 'receivingYardsAfterCatch': 19.0, 'receivingYardsPerReception': 10.667, 'teamWin': 1.0, 'pointsScored': 12.0, '180': 1.0, '185': 1.0, '210': 1.0, '212': 6.0, '213': 1.0}})

    def test_convert_week_payload(self):
        self.assertEqual(self.transformer.convert_week_payload(),
                         [
                             (12, 8, {'points': 27.3, 'breakdown': {'rushingAttempts': 16.0, 'rushingYards': 91.0, 'rushingTouchdowns': 1.0, '27': 18.0, '28': 9.0, '29': 4.0, '30': 3.0, '31': 1.0, '33': 3.0, '34': 1.0, 'rushingYardsPerAttempt': 5.688, 'receivingReceptions': 3.0, 'receivingYards': 32.0, 'receivingTouchdowns': 1.0, '47': 6.0, '48': 3.0, '49': 1.0, '50': 1.0, 'receivingTargets': 6.0, 'receivingYardsAfterCatch': 19.0, 'receivingYardsPerReception': 10.667, 'teamWin': 1.0, 'pointsScored': 12.0, '180': 1.0, '185': 1.0, '210': 1.0, '212': 6.0, '213': 1.0}}, 'OP', 'QB'),
                             (114, 6, {'points': 4.8, 'breakdown': {'receivingReceptions': 3.0, 'receivingYards': 18.0, '47': 3.0, '48': 1.0, 'receivingTargets': 5.0, 'receivingYardsAfterCatch': 12.0, 'receivingYardsPerReception': 6.0, 'teamWin': 1.0, '210': 1.0, '213': 2.0}}, 'BE', 'TE')
                         ])


if __name__ == '__main__':
    unittest.main()
