import { groupBy, map } from 'lodash-es';

import { LeaderboardInsight, NotablesInsight } from '~/api/v3';

export const LEADERBOARD_NAME_TO_DISPLAY_NAME: Record<string, string> = {
  typed_leaderboard_blue_banners: 'Most Blue Banners',
  typed_leaderboard_most_matches_played: 'Most Matches Played',
  typed_leaderboard_highest_median_score_by_event: 'Highest Median Score',
  typed_leaderboard_highest_match_clean_score: 'Highest Clean Score',
  typed_leaderboard_highest_match_clean_combined_score:
    'Highest Clean Combined Score',
  typed_leaderboard_most_awards: 'Most Awards',
  typed_leaderboard_most_non_champs_event_wins:
    'Most Non-Championship Event Wins',
  typed_leaderboard_most_unique_teams_played_with_against:
    'Most Unique Teams Played With/Against',
  typed_leaderboard_notables_division_finals_appearances:
    'Most Division Finals Appearances',
  typed_leaderboard_notables_world_champions: 'Most World Championship Wins',
  typed_leaderboard_notables_division_winners: 'Most Division Wins',
};

export const NOTABLE_NAME_TO_DISPLAY_NAME: Record<string, string> = {
  notables_hall_of_fame: 'Hall of Fame',
  notables_world_champions: 'World Champions',
};

export function leaderboardFromNotable(
  notable: NotablesInsight,
): LeaderboardInsight {
  const valueToKeysMap = groupBy(
    notable.data.entries,
    (entry) => entry.context.length,
  );

  const rankings = map(valueToKeysMap, (entries, value) => ({
    value: parseInt(value, 10),
    keys: entries
      .map((entry) => entry.team_key)
      .sort((a, b) => parseInt(a.substring(3)) - parseInt(b.substring(3))),
  }));

  rankings.sort((a, b) => b.value - a.value);

  return {
    name: `typed_leaderboard_${notable.name}`,
    year: notable.year,
    data: {
      key_type: 'team',
      rankings: rankings,
    },
  };
}
