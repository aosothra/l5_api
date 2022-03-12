def predict_rub_salary(currency, low_limit, high_limit):
    salary = None
    if currency.lower() in {'rub', 'rur'}:
        if low_limit and high_limit:
            salary = (int(high_limit) + int(low_limit))/2
        elif low_limit:
            salary = int(low_limit)*1.2
        elif high_limit:
            salary = int(high_limit)*0.8

    return salary
