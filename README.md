# L5_API - Expected Salary

This script accesses data from HeadHunter and SuperJob to predict and analyze salaries for jobs in IT based on most popular programming languages. 

Currently used API sources:

[HeadHunter API](https://dev.hh.ru/)

[SuperJob API](https://api.superjob.ru/)

### Installation guidelines


You must have Python3 installed on your system.
You may use `pip` (or `pip3` to avoid conflict with Python2) to install dependencies.
```
pip install -r requirements.txt
```
It is strongly advised to use [virtualenv/venv](https://docs.python.org/3/library/venv.html) for project isolation.

This script uses `.env` file in root folder to store variables neccessary for operation. So, do not forget to create one!

Below you can find how contents of your `.env` file should look like, and 

```
SJ_API_KEY = 'putyoursecretkeyhere'
```

`SJ_API_KEY` is required for fetching from SuperJob Api endpoints. You'll need to register to get your secret key ([get it here](https://api.superjob.ru/info/)).


### Basic usage (for the lack of any other...)

```
py main.py 
```

Script might take some time due to extensive fetching. Your output will look similar to that:

``` 
>py main.py
┌Вакансии на HeadHunter─┬──────────────┬──────────────────┬─────────────────────┬──────────────────┐
│ Язык программирования │ Расположение │ Вакансий найдено │ Вакансий обработано │ Средняя зарплата │
├───────────────────────┼──────────────┼──────────────────┼─────────────────────┼──────────────────┤
│ JavaScript            │ Москва       │ 2000             │ 856                 │ 189328           │
│ Java                  │ Москва       │ 2000             │ 464                 │ 245313           │
│ Python                │ Москва       │ 2000             │ 488                 │ 208630           │
│ Ruby                  │ Москва       │ 211              │ 56                  │ 201412           │
│ PHP                   │ Москва       │ 1563             │ 708                 │ 164376           │
│ C++                   │ Москва       │ 1557             │ 433                 │ 193408           │
│ C#                    │ Москва       │ 1711             │ 441                 │ 203727           │
│ C                     │ Москва       │ 2000             │ 764                 │ 177342           │
│ Go                    │ Москва       │ 923              │ 198                 │ 240142           │
│ Objective-C           │ Москва       │ 184              │ 49                  │ 242551           │
└───────────────────────┴──────────────┴──────────────────┴─────────────────────┴──────────────────┘

┌Вакансии на SuperJob───┬──────────────┬──────────────────┬─────────────────────┬──────────────────┐
│ Язык программирования │ Расположение │ Вакансий найдено │ Вакансий обработано │ Средняя зарплата │
├───────────────────────┼──────────────┼──────────────────┼─────────────────────┼──────────────────┤
│ JavaScript            │ Москва       │ 103              │ 74                  │ 146151           │
│ Java                  │ Москва       │ 45               │ 28                  │ 149091           │
│ Python                │ Москва       │ 75               │ 52                  │ 148449           │
│ Ruby                  │ Москва       │ 6                │ 6                   │ 138666           │
│ PHP                   │ Москва       │ 65               │ 46                  │ 145333           │
│ C++                   │ Москва       │ 41               │ 29                  │ 165275           │
│ C#                    │ Москва       │ 31               │ 21                  │ 160523           │
│ C                     │ Москва       │ 30               │ 16                  │ 187312           │
│ Go                    │ Москва       │ 14               │ 11                  │ 283363           │
│ Objective-C           │ Москва       │ 2                │ 2                   │ 225000           │
└───────────────────────┴──────────────┴──────────────────┴─────────────────────┴──────────────────┘
```

### Project goals

This project was created for educational purposes as part of [dvmn.org](https://dvmn.org/) Backend Developer course.