# Интерактивная карта загрязнения воздуха в г. Москва #
## проект дататона магистратуры "Науки о данных" на тему "Мониторинг экосистемы через IT-решения" ##

Данный проект реализует предсказание уровня загрязнения воздуха по данным станций с waqi.info. Предсказываются данные на следующий день и визуализируются на интерактивной карте.
Предсказывается агрегированный показатель(aqi) загрязнения воздуха, который рассчитывается как максимум из значений показателей pm10, pm2.5, CO и других, доступных на станции измерения (чем больше показание, тем загрязненнее воздух).

### Реализован функционал: ###
- Обработка полученных исторических данных со станций за веcь период
- Обучение модели ARIMA
- Получение предсказания на следующий день по каждой станции
- Интерполяция данных за последний день исторических данных и предсказанных данных
- Наложение данных по координатам на карту c цветовой дифференциацией по уровню загрязнения
- Реализация приложения на сервере Streamlit

### Структура проекта ###
Данные - папка weather_data

Работа с данными - weather.ipnb

Результат обработки данных - папка saved
 - last.html - страница с текущими данными по загрязнению воздуха
 - predicted.html - страница с предсказанными данными по загрязнению воздуха

Приложение с визуализацией на Streamlit- app.py

### Что можно доработать: ###
- автоматизация скачивания данных
- усовершенствовать очистку данных (обработка пропусков по датам)
- улучшить модель предсказаний для каждой станции подбором гиперпараметров ARIMA
- предсказания на насколько дней
- UI/UX - возможно GIF с анимации, таймлайн с визуализацией исторических данных, графики
- данные по другим городам

Альтренативное решение с графиком загрезненности воздуха по станциям https://github.com/eisakhanov/Datatone_WAQI_Moscow

Участники команды:
Эдуард Исаханов
Артем Смирнов
Яков Чибинин
Владимир Ульзутуев

![Animation](https://github.com/jchibinin/Datatone_WAQI_Moscow/assets/12885639/83916d82-9f98-4827-b31c-06db4a2728fa)



