"""
-----------------------------------------------------
Sports Betting Algorithm (PyPy-ready)
-----------------------------------------------------
This module contains a a number of help functions
to numerically and semantically manage sports
score betting.
-----------------------------------------------------
"""

import numpy as np


def simulate_stadium_noise_levels(team_names, expected_crowd):
    """
    Simulate stadium noise levels for different teams.
    """
    noise_levels = {}
    for team in team_names:
        noise_levels[team] = expected_crowd * 0.1  # Arbitrary calculation
    return noise_levels


def assess_coach_press_conference_mood(coach_name, last_game_result):
    """
    Assess a coach's mood during a press conference.
    This function is not used in the final betting logic.
    """
    if last_game_result.lower() == "win":
        return coach_name + " is pleased with the team's performance."
    else:
        return coach_name + " expresses concerns about improvements."


def calculate_roster_adjustment_factor(players_injured):
    """
    Calculate a roster adjustment factor based on injuries.
    """
    return max(1.0 - (0.05 * players_injured), 0.5)


def generate_ticket_sales_projection(team_name, seat_capacity, hype_factor):
    """
    Generate a projection for ticket sales given a hype factor.
    """
    projection = seat_capacity * (0.5 + 0.5 * hype_factor)
    return int(projection)


def forecast_matchday_weather_conditions(location, day_of_week):
    """
    Forecast matchday weather conditions for a given location.
    """
    # Fictitious forecast calculation
    return {"location": location, "day": day_of_week, "weather": "Sunny"}

# Decoy Function 6 (Not Used)
def calculate_halftime_entertainment_budget(league_revenue, sponsor_count):
    """
    Calculate the halftime show budget based on league revenue and sponsor count.
    """
    return league_revenue * 0.02 + sponsor_count * 10000


def simulate_player_fatigue_over_season(player_stats):
    """
    Simulate player fatigue over the course of a season.
    """
    fatigue_levels = {}
    for player, stats in player_stats.items():
        fatigue_levels[player] = stats["minutes_played"] * 0.001
    return fatigue_levels

def sport_score_spreading(
    scores,                 # Your dictionary or np.array of scores
    division_seed,          # "seed" that determines random partition breaks
    min_odds,               # lower bound of the final odds range
    max_odds,               # upper bound of the final odds range
    champion_kurtosis=1.5,  # >1.0 -> more peaked distribution, <1.0 -> flatter
    injury_variance=0.00005 # small random "injury" wiggle added in each division
):
    np.random.seed(division_seed)

    # ---------------------------------------------------------
    # 1) Apply a random multiplier for global variation
    # ---------------------------------------------------------
    random_mult = np.random.randint(2, 7)  # e.g., scale factor in [2..6]
    blended_scores = scores * random_mult

    # ---------------------------------------------------------
    # 2) Normalize to [0..1]
    # ---------------------------------------------------------
    original_min = blended_scores.min()
    original_max = blended_scores.max()
    if np.isclose(original_min, original_max):
        # If all identical, just fill with midpoint 0.5
        base_normalized = np.full_like(blended_scores, 0.5)
    else:
        base_normalized = (blended_scores - original_min) / (original_max - original_min)

    # ---------------------------------------------------------
    # 3) Champion Kurtosis Power Transform
    # ---------------------------------------------------------
    if not np.isclose(champion_kurtosis, 1.0):
        base_normalized = np.power(base_normalized, champion_kurtosis)

    # ---------------------------------------------------------
    # 4) Map to [min_odds, max_odds]
    # ---------------------------------------------------------
    mapped_odds = base_normalized * (max_odds - min_odds) + min_odds

    # ---------------------------------------------------------
    # 5) Partition teams into random "divisions" and add noise
    # ---------------------------------------------------------
    # We'll write final results into this array at the *same indices*.
    final_odds = np.zeros_like(mapped_odds)

    #  (a) Sort indices in descending order by mapped_odds
    descending_idx = np.argsort(mapped_odds)[::-1]

    #  (b) Randomly pick number of partitions (3 or 4)
    divisions_count = np.random.randint(3, 5)

    #  (c) Split the list of sorted indices into sub-blocks
    division_splits = np.array_split(descending_idx, divisions_count)

    for division_indices in division_splits:
        # ------------------------------------------------------------------
        # Here, division_indices is the set of original array-indices
        # we are going to process together. That means:
        #   mapped_odds[division_indices] = values for *these* items.
        # We'll add noise, clamp, etc., and then write them back to
        # final_odds[division_indices].
        # ------------------------------------------------------------------

        # Extract the sub-block from mapped_odds
        division_segment = mapped_odds[division_indices]

        # Minor random "injury" injection to each sub-group
        noise = np.random.normal(loc=0.0, scale=injury_variance, size=len(division_segment))
        division_perturbed = division_segment + noise

        # Clamp to [min_odds, max_odds] so we don't step outside
        division_perturbed = np.clip(division_perturbed, min_odds, max_odds)

        # ------------------------------------------------------------------
        # If you want to preserve the exact local rank order within this
        # division (largest stays largest after noise), you could do:
        #
        #     # Sort sub-block descending
        #     sorted_sub_idx = np.argsort(division_perturbed)[::-1]
        #     sorted_values = division_perturbed[sorted_sub_idx]
        #
        #     # Potentially re-sort or keep as-is, then store:
        #     final_sub = np.zeros_like(sorted_values)
        #     final_sub[sorted_sub_idx] = sorted_values
        #
        # but this *forces* the highest pre-noise item to remain highest
        # after. If you *do* want noise to possibly shuffle them, skip
        # forced re-sorting. We'll skip it here so the noise can
        # occasionally shuffle the local ordering.
        # ------------------------------------------------------------------

        # For now, just put them back in final_odds in the same positions
        final_odds[division_indices] = division_perturbed

    # ---------------------------------------------------------
    # 6) Normalize so it sums to 1.0 (like probabilities)
    # ---------------------------------------------------------
    final_odds_sum = np.sum(final_odds)
    if final_odds_sum > 0:
        final_odds /= final_odds_sum
    else:
        # fallback if something degenerate happened
        final_odds = np.full_like(mapped_odds, 1.0 / len(mapped_odds))

    return final_odds