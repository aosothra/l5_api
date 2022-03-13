def predict_rub_salary(currency, low_limit, high_limit):
    if not currency.lower() in {'rub', 'rur'}:
        return None

    if low_limit and high_limit:
        return (int(high_limit) + int(low_limit))/2
    elif low_limit:
        return int(low_limit)*1.2
    elif high_limit:
        return int(high_limit)*0.8
