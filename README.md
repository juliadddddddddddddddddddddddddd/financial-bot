Проект "Финансовый бот"

бОТ: @fjfjkkflBot

Цель: 
Контрол финансов пользователя.

Использованные технологии:
- язык программирования Python 3
- библиотека telegram
- СУБД SQLite

Сборка и запуск проекта:
Проект представлен в виде следующей системы файлов:
--|
  |- main.py   - программный код приложения
  |- data - папка с orm-моделями	
  |- sources- папка с вспомагательными файлами
     |
	 | - music - используемые в приложении звуки
	 |- pictures    - используемые в приложении изображения
  |- db - папка с базой данных

Для работы приложения требуется установка библиотек, перечисленных в файле
requirements.txt

Для удобства знакомства с приложением также представлен исполняемый файл
main.exe

Описание работы приложения:
1. При запуске бота появляются доступные опции: "Доходы", "Расходы", "Совет от бота", "Выбрать музыкальное сопровождение", "Фото"

2. При выборе опции "Доходы" появляются дополнительные опции:
   - Добавить доходы
   - Посмотреть доходы. Есть варинат посмотреть доходы за 1 неделю, 2 недели или месяц.

3. При выборе опции "Расходы" появляются дополнительные опции:
   - Добавить расходы. Можно добавить расход за определенную категорию
   - Статистика расходов. Можно выбрать категорию расходов и нужный период (1 неделя, 2 недели, месяц)

4. При выборе опции "Совет от бота" пользователь получит финансовый совет.

5. "Выбрать музыкальное сопровождение". Бот пришлет музыку. 

6. "Фото". Бот пришлет шутку про деньги.

Сфера применения приложения:
Повседневная жизнь. 
