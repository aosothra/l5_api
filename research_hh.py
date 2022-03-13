from itertools import count
import requests

from predict_salary import predict_rub_salary


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

        response_data = response.json()
        vacancies = response_data['items']

        for vacancy in vacancies:
            result['vacancies_found'] += 1
            
            if not vacancy['salary']:
                continue

            salary = predict_rub_salary(
                        vacancy['salary']['currency'],
                        vacancy['salary']['from'],
                        vacancy['salary']['to'])
            if salary:
                result['vacancies_processed'] += 1
                salary_sum += salary

        if (page >= response_data['pages'] or
                result['vacancies_found'] >= 2000):
            break

    if result['vacancies_processed']:
        result['salary_average'] = int(salary_sum / result['vacancies_processed'])
    else:
        result['salary_average'] = 0
    return result


def summarize_hh_vacancies(langs, area):
    result = []
    for lang in langs:
        data = analyze_hh_for_language(lang, area)
        result.append(data)
    return result
