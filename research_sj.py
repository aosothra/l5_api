from itertools import count
import requests

from datetime import datetime, timedelta

from predict_salary import predict_rub_salary


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
            salary = predict_rub_salary(
                        vacancy['currency'],
                        vacancy['payment_from'],
                        vacancy['payment_to'])
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
