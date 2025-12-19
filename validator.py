

def validate_vitals(vitals):
    errors = {}
    is_valid = True

    heart_rate = vitals.get("heart_rate")
    breaths_per_minute = vitals.get("breaths_per_minute")

    if heart_rate is None:
        errors["heart_rate"] = "Heart rate is required"
        is_valid = False
    elif not isinstance(heart_rate, (int, float)):
        errors["heart_rate"] = "Heart rate must be a number"
        is_valid = False
    elif not 50 <= heart_rate <= 180:
        errors["heart_rate"] = "Heart rate must be between 50 and 180 bpm"
        is_valid = False

    if breaths_per_minute is None:
        errors["breaths_per_minute"] = "Breaths per minute is required"
        is_valid = False
    elif not isinstance(breaths_per_minute, (int, float)):
        errors["breaths_per_minute"] = "Breaths per minute must be a number"
        is_valid = False
    elif not 10 <= breaths_per_minute <= 30:
        errors["breaths_per_minute"] = "Breaths per minute must be between 10 and 30"
        is_valid = False

    return is_valid, errors
