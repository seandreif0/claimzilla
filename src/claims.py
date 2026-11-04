def member_copay(total: float, copay_rate: float) -> float:
    """Return the member's share of a claim, rounded to cents."""
    return round(total * copay_rate, 2)
