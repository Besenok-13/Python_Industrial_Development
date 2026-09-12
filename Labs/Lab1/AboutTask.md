# Лабораторная работа 1: восстановление Team Board

Цель работы: последовательно восстановить установку приложения, исправить
ошибку в календарной утилите и найти расхождение между тестами и поведением
веб-страницы.

## Личный рабочий каталог

Каждый студент создаёт три независимых каталога: `task1`, `task2` и `task3` в
`Students/<student_id>/Lab1`. В каждом каталоге находится отдельный клон только
назначенной ветки и личная ветка для отправки решения. Используйте латинский
`student_id` без пробелов, например `Python-Pythonovich`.

1. Создайте личный каталог для лабораторной:

   ```bash
   mkdir -p Students/Python-Pythonovich/Lab1
   cd Students/Python-Pythonovich/Lab1
   ```

2. Для первой задачи скачайте только её стартовую ветку в каталог `task1` и
   создайте личную ветку:

   ```bash
   git clone --branch Lab1_task1 --single-branch https://github.com/Besenok-13/Python_Industrial_Development.git task1
   cd task1
   git switch --create students/Python-Pythonovich/Lab1_task1
   ```

   Код первой задачи редактируется только в
   `Students/Python-Pythonovich/Lab1/task1`. Не вносите изменения напрямую
   в `Lab1_task1`: это исходная ветка задания.

3. После ротации роли создайте аналогичный каталог для следующего задания.
   Пример для второй задачи:

   ```bash
   cd ../..
   git clone --branch Lab1_task2 --single-branch https://github.com/Besenok-13/Python_Industrial_Development.git task2
   cd task2
   git switch --create students/Python-Pythonovich/Lab1_task2
   ```

4. Для третьего задания используйте те же команды, заменив `task2` и
   `Lab1_task2` на `task3` и `Lab1_task3`. В результате структура будет такой:

   ```text
   Students/Python-Pythonovich/Lab1/
   task1/
   task2/
   task3/
   ```

5. Чтобы продолжить ранее начатую задачу, перейдите в её каталог. Переключать
   ветку не нужно, потому что у каждой задачи отдельный клон:

   ```bash
   cd Students/Python-Pythonovich/Lab1/task1
   git status
   ```

## Подготовка окружения

После перехода в каталог нужной задачи, например
`Students/<student_id>/Lab1/task1`, создайте окружение:

```bash
python -m venv .venv
```

В Linux и macOS активируйте окружение:

```bash
source .venv/bin/activate
```

В PowerShell используйте:

```powershell
.venv\Scripts\Activate.ps1
```

## Переход к следующей задаче

До перехода к следующей роли зафиксируйте и отправьте решение. Находясь в
каталоге нужной задачи, выполните:

```bash
git status
git add pyproject.toml packages src tests
git commit -m "Fix Lab1 task"
git push -u origin students/Python-Pythonovich/Lab1_task1
```

Для задач 2 и 3 замените номер в имени личной ветки. После push перейдите в
следующий каталог `taskN`; первая задача останется доступна в `task1`.

## Задача 1. Восстановить зависимости

1. Попробуйте установить корневой проект, тестовые зависимости и три локальных
   пакета одной командой:

   ```bash
   python -m pip install -e '.[dev]' -r requirements.txt
   ```

2. Прочитайте сообщение resolver: оно указывает на несовместимые диапазоны
   версий. Сравните декларации зависимостей в корневом проекте и локальных
   пакетах:

   ```bash
   grep -n "fastapi\|httpx" pyproject.toml packages/*/pyproject.toml
   ```

3. Измените ограничения так, чтобы для каждого пакета существовала общая
   версия. Повторите установку и проверьте согласованность окружения:

   ```bash
   python -m pip install -e '.[dev]' -r requirements.txt
   python -m pip check
   ```

4. Установка может завершиться успешно, но приложение всё ещё может быть
   несовместимо с выбранной версией библиотеки. Запустите сервер:

   ```bash
   uvicorn team_board.main:app --reload
   ```

5. Если при старте возникла ошибка аргумента клиента HTTP, найдите место его
   создания и сопоставьте используемый API с выбранным диапазоном HTTPX:

   ```bash
   grep -R -n "httpx\.Client\|httpx\.AsyncClient" packages src
   ```

6. После исправления остановите сервер `Ctrl+C` и выполните тесты:

   ```bash
   pytest
   ```

## Задача 2. Исправить календарную функцию

1. Запустите только падающий тест:

   ```bash
   pytest tests/test_schedule.py -q
   ```

2. Откройте тест, изучите его входные данные и ожидаемый результат. Затем
   найдите календарные операции в пакете:

   ```bash
   grep -R -n "timedelta" packages/task_workflow
   ```

3. Откройте её реализацию и сравните операцию с ожидаемой датой из теста.
   Исправляйте только расчёт даты, не меняя ожидание теста.

4. Проверьте исправление и затем весь набор тестов:

   ```bash
   pytest tests/test_schedule.py -q
   pytest
   ```

## Задача 3. Найти расхождение тестов и приложения

1. Убедитесь, что тесты метрики проходят:

   ```bash
   pytest tests/test_metrics.py -q
   ```

2. Прочитайте описание показателя выполнения в `README.md`, затем найдите,
   откуда в обработчике главной страницы поступает значение показателя:

   ```bash
   grep -R -n "completion" src packages tests
   ```

3. Проследите всю цепочку вызовов от `dashboard` до функции, которая считает
   процент. Сравните её формулу с функцией, покрытой тестами. Исправьте код,
   фактически используемый страницей, сохранив корректное поведение для
   пустого списка.

4. Запустите приложение и откройте главную страницу:

   ```bash
   uvicorn team_board.main:app --reload
   ```

   Перейдите по адресу `http://127.0.0.1:8000`, сравните отображаемый процент
   с данными задач и остановите сервер `Ctrl+C`.

5. Завершите проверку:

   ```bash
   pytest
   python -m pip check
   ```

## Отправка решения

Перед отправкой решения покажите изменённые файлы и убедитесь, что в коммит не
попало виртуальное окружение:

```bash
git status
git diff
git add pyproject.toml packages src tests
git commit -m "Fix Lab1 task"
git push -u origin students/Python-Pythonovich/Lab1_task1
```

Каждое изменение должно объясняться сообщением ошибки, тестом или фактическим
поведением веб-страницы.
