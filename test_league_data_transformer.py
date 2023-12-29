import unittest
from unittest.mock import patch, MagicMock
from league_data_transformer import LeagueDataTransformer
from fixtures.full_player1_stats import p1_stats
from fixtures.full_player2_stats import p2_stats


class TestLeagueDataTransformer(unittest.TestCase):

    def setUp(self):
        mock_player1 = self.generate_player_mock(12, 8, 'QB', 'OP', p1_stats)
        mock_player2 = self.generate_player_mock(114, 6, 'TE', 'BE', p2_stats)

        mock_players_home = [mock_player1]
        mock_players_away = [mock_player2]

        mock_box_score_home = MagicMock()
        mock_box_score_away = MagicMock()

        mock_box_score_home.home_lineup = mock_players_home
        mock_box_score_away.away_lineup = mock_players_away

        mock_league = MagicMock()

        mock_league.box_scores = MagicMock(return_value=[mock_box_score_home, mock_box_score_away])

        self.transformer = LeagueDataTransformer(mock_league, 12)

    def generate_player_mock(self, points, onTeamId, position, slot_position, stats):
        mock_player = MagicMock()
        mock_player.points = points
        mock_player.onTeamId = onTeamId
        mock_player.position = position
        mock_player.slot_position = slot_position
        mock_player.stats = stats

        return mock_player

    def test_process_player_stats_returns_empty_dict_when_no_stats(self):
        self.assertEqual(self.transformer.process_player_stats({}), {})

    def test_process_player_stats_happy_path(self):
        self.assertEqual(self.transformer.process_player_stats(p1_stats),
                         {'points': 27.3, 'breakdown': {'rushingAttempts': 16.0, 'rushingYards': 91.0, 'rushingTouchdowns': 1.0, '27': 18.0, '28': 9.0, '29': 4.0, '30': 3.0, '31': 1.0, '33': 3.0, '34': 1.0, 'rushingYardsPerAttempt': 5.688, 'receivingReceptions': 3.0, 'receivingYards': 32.0, 'receivingTouchdowns': 1.0, '47': 6.0, '48': 3.0, '49': 1.0, '50': 1.0, 'receivingTargets': 6.0, 'receivingYardsAfterCatch': 19.0, 'receivingYardsPerReception': 10.667, 'teamWin': 1.0, 'pointsScored': 12.0, '180': 1.0, '185': 1.0, '210': 1.0, '212': 6.0, '213': 1.0}})

    def test_generate_scoring_data_no_player_processing_if_no_team_id_is_associated(self):
        bad_team_id = 0

        mock_player1 = self.generate_player_mock(12, bad_team_id, 'QB', 'OP', p1_stats)

        mock_player2 = self.generate_player_mock(114, 6, 'TE', 'BE', p2_stats)

        mock_players_home = [mock_player1]
        mock_players_away = [mock_player2]

        mock_box_score_home = MagicMock()
        mock_box_score_away = MagicMock()

        mock_box_score_home.home_lineup = mock_players_home
        mock_box_score_away.away_lineup = mock_players_away

        mock_league = MagicMock()

        mock_league.box_scores = MagicMock(return_value=[mock_box_score_home, mock_box_score_away])

        transformer = LeagueDataTransformer(mock_league, 12)

        self.assertEqual(transformer.generate_scoring_data(),
                         [
                             (114, 6, {'points': 4.8, 'breakdown': {'receivingReceptions': 3.0, 'receivingYards': 18.0, '47': 3.0, '48': 1.0, 'receivingTargets': 5.0, 'receivingYardsAfterCatch': 12.0, 'receivingYardsPerReception': 6.0, 'teamWin': 1.0, '210': 1.0, '213': 2.0}}, 'BE', 'TE')
                         ])

    def test_generate_scoring_data_happy_path(self):
        # print(self.transformer.generate_scoring_data())
        self.assertEqual(self.transformer.generate_scoring_data(),
                         [
                             (12, 8, {'points': 27.3, 'breakdown': {'rushingAttempts': 16.0, 'rushingYards': 91.0, 'rushingTouchdowns': 1.0, '27': 18.0, '28': 9.0, '29': 4.0, '30': 3.0, '31': 1.0, '33': 3.0, '34': 1.0, 'rushingYardsPerAttempt': 5.688, 'receivingReceptions': 3.0, 'receivingYards': 32.0, 'receivingTouchdowns': 1.0, '47': 6.0, '48': 3.0, '49': 1.0, '50': 1.0, 'receivingTargets': 6.0, 'receivingYardsAfterCatch': 19.0, 'receivingYardsPerReception': 10.667, 'teamWin': 1.0, 'pointsScored': 12.0, '180': 1.0, '185': 1.0, '210': 1.0, '212': 6.0, '213': 1.0}}, 'OP', 'QB'),
                             (114, 6, {'points': 4.8, 'breakdown': {'receivingReceptions': 3.0, 'receivingYards': 18.0, '47': 3.0, '48': 1.0, 'receivingTargets': 5.0, 'receivingYardsAfterCatch': 12.0, 'receivingYardsPerReception': 6.0, 'teamWin': 1.0, '210': 1.0, '213': 2.0}}, 'BE', 'TE')
                         ])


if __name__ == '__main__':
    unittest.main()
