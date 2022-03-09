from itertools import count
import requests


def predict_hh_rub_salary(vacancy):
    salary = None
    if vacancy['salary'] and vacancy['salary']['currency'] == 'RUR':
        low_limit = vacancy['salary']['from']
        high_limit = vacancy['salary']['to']

        if low_limit and high_limit:
            salary = (int(high_limit) + int(low_limit))/2
        elif low_limit:
            salary = int(low_limit)*1.2
        elif high_limit:
            salary = int(high_limit)*0.8
    return salary


def analyze_hh_for_language(lang, area):
    result = {
        'lang': lang,
        'area': area,
        'vacancies_found': 0,
        'vacancies_processed': 0,
        'salary_average': 0,
    }
    salary_sum = 0

    url = 'https://api.hh.ru/vacancies/'

    payload = {
        'text': f'Программист {lang} {area}',
        'period': 30,
    }

    for page in count(0):
        payload['page'] = page

        response = requests.get(url, params=payload)
        response.raise_for_status()

        vacancies = response.json()['items']

        for vacancy in vacancies:
            if vacancy['area']['name'] == area:
                result['vacancies_found'] += 1
                salary = predict_hh_rub_salary(vacancy)
                if salary:
                    result['vacancies_processed'] += 1
                    salary_sum += salary

        if (page >= response.json()['pages'] or
                result['vacancies_found'] >= 2000):
            break

    result['salary_average'] = int(salary_sum / result['vacancies_processed'])
    return result


def summarize_hh_vacancies(langs, area):
    result = []
    for lang in langs:
        data = analyze_hh_for_language(lang, area)
        result.append(data)
    return result
