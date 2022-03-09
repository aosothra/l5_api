from itertools import count
import requests

from datetime import datetime, timedelta


def predict_sj_salary(vacancy):
    salary = None
    if vacancy['currency'] != 'rub':
        return salary

    low_limit = vacancy['payment_from']
    high_limit = vacancy['payment_to']

    if low_limit > 0 and high_limit > 0:
        salary = (low_limit + high_limit) / 2
    elif low_limit > 0:
        salary = low_limit * 1.2
    elif high_limit > 0:
        salary = high_limit * 0.8

    return salary


def analyze_sj_for_language(lang, area, api_key):
    result = {
        'lang': lang,
        'area': area,
        'vacancies_found': 0,
        'vacancies_processed': 0,
        'salary_average': 0,
    }
    salary_sum = 0

    url = 'https://api.superjob.ru/2.0/vacancies/'

    headers = {
        'X-Api-App-Id': api_key
    }

    date_from = datetime.now()
    date_from -= timedelta(days=30)

    payload = {
        'town': area,
        'keyword': f'Программист {lang}',
        'count': 100,
        'date_published_from': int(date_from.timestamp())
    }

    for page in count(0):
        payload['page'] = page

        response = requests.get(url, headers=headers, params=payload)
        response.raise_for_status()

        vacancies = response.json()['objects']
        for vacancy in vacancies:
            result['vacancies_found'] += 1
            salary = predict_sj_salary(vacancy)
            if salary:
                result['vacancies_processed'] += 1
                salary_sum += salary

        if not response.json()['more']:
            break

    result['salary_average'] = int(salary_sum / result['vacancies_processed'])
    return result


def summarize_sj_vacancies(langs, area, api_key):
    result = []
    for lang in langs:
        data = analyze_sj_for_language(lang, area, api_key)
        result.append(data)
    return result
