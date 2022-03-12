import os
from dotenv import load_dotenv
from terminaltables import SingleTable

from research_hh import summarize_hh_vacancies
from research_sj import summarize_sj_vacancies


def convert_to_table_content(data_rows):
    rows = [[
        'Язык программирования',
        'Расположение',
        'Вакансий найдено',
        'Вакансий обработано',
        'Средняя зарплата'
        ]]
    for data_row in data_rows:
        rows.append(data_row.values())
    return rows


def main():
    load_dotenv()
    sj_api_key = os.getenv('SJ_API_KEY')

    langs = [
        'JavaScript',
        'Java',
        'Python',
        'Ruby',
        'PHP',
        'C++',
        'C#',
        'C',
        'Go',
        'Objective-C'
        ]

    hh_data = summarize_hh_vacancies(langs, 'Москва')
    sj_data = summarize_sj_vacancies(langs, 'Москва', sj_api_key)

    hh_table_content = convert_to_table_content(hh_data)
    hh_table = SingleTable(hh_table_content, "Вакансии на HeadHunter")
    print(hh_table.table)
    print()

    sj_table_content = convert_to_table_content(sj_data)
    sj_table = SingleTable(sj_table_content, "Вакансии на SuperJob")
    print(sj_table.table)


if __name__ == '__main__':
    main()
