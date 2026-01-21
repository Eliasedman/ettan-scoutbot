import pandas as pd
from typing import Dict

class ScoringEngine:
    """
    A simple scoring engine to compute Fit Scores for players.
    """
    def __init__(self, weights: Dict[str, float] = None):
        # Default weights for score components: RollFit, AgePotential, Availability, GapScore
        self.weights = weights or {"roll": 0.45, "age": 0.25, "availability": 0.2, "gap": -0.1}

    def compute_rollfit(self, player_stats: pd.Series, role_profile: Dict[str, float]) -> float:
        """
        Compute a RollFit score based on player stats and role profile weights.
        This is a placeholder implementation using a weighted sum of selected stats.
        """
        score = 0.0
        for stat, weight in role_profile.items():
            stat_value = player_stats.get(stat, 0)
            score += weight * stat_value
        return score

    def compute_age_potential(self, age: float) -> float:
        """
        Compute an AgePotential score. Younger players get higher scores.
        """
        if age <= 26:
            return 100.0
        # Linear decline after age 26
        decline = max(0.0, 1 - (age - 26) / 10)
        return 100.0 * decline

    def compute_availability(self, minutes_played: float, max_minutes: float = 3000.0) -> float:
        """
        Compute an Availability score based on minutes played relative to a maximum.
        """
        return min(100.0, (minutes_played / max_minutes) * 100.0)

    def compute_gap_score(self, gaps: int) -> float:
        """
        Compute a GapScore penalty for long gaps in squad appearances.
        """
        return -min(20.0, gaps * 2.0)

    def compute_fit_score(self, player_stats: pd.Series, role_profile: Dict[str, float]) -> float:
        """
        Compute the final Fit Score combining all components with their weights.
        """
        rollfit = self.compute_rollfit(player_stats, role_profile)
        age_pot = self.compute_age_potential(player_stats.get("age", 0))
        availability = self.compute_availability(player_stats.get("minutes_played", 0))
        gap_score = self.compute_gap_score(player_stats.get("long_gaps", 0))

        # Normalize component scores to 0-100 range if necessary
        components = {
            "roll": rollfit,
            "age": age_pot,
            "availability": availability,
            "gap": gap_score,
        }
        fit_score = 0.0
        for key, value in components.items():
            weight = self.weights.get(key, 0)
            fit_score += weight * value
        # Ensure the score is within 0-100
        return max(0.0, min(100.0, fit_score))
