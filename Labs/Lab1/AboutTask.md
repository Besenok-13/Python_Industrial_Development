# Лабораторная работа 1: восстановление Team Board

Цель работы: последовательно восстановить установку приложения, исправить
ошибку в календарной утилите и найти расхождение между тестами и поведением
веб-страницы.

## Fork, ветка и рабочая папка

Каждый студент работает в своём fork и создаёт отдельную ветку и Pull Request
для каждой задачи. В коммит попадают файлы из
`Students/<github-login>/Lab1/taskN`, поэтому работы разных студентов не
пересекаются. Используйте свой GitHub login в нижнем регистре вместо
`<github-login>`.

1. На странице исходного репозитория нажмите **Fork**. Затем склонируйте свой
   fork и подключите исходный репозиторий как `upstream`:

   ```bash
   git clone https://github.com/<github-login>/Python_Industrial_Development.git
   cd Python_Industrial_Development
   git remote add upstream https://github.com/Besenok-13/Python_Industrial_Development.git
   git fetch upstream
   ```

2. Создайте ветку для назначенной задачи от актуального `upstream/main`.
   Пример для первой задачи:

   ```bash
   git switch --create lab1/<github-login>/task1 upstream/main
   mkdir -p Students/<github-login>/Lab1/task1
   git archive upstream/Lab1_task1 | tar -x -C Students/<github-login>/Lab1/task1
   cd Students/<github-login>/Lab1/task1
   ```

   `git archive` копирует стартовое состояние только назначенной задачи в вашу
   папку. Не изменяйте ветки `Lab1_task1`, `Lab1_task2` и `Lab1_task3`.

3. Для следующей роли вернитесь в корень клона, получите изменения преподавателя
   и создайте новую ветку и новую папку. Пример для второй задачи:

   ```bash
   cd ../../../..
   git fetch upstream
   git switch --create lab1/<github-login>/task2 upstream/main
   mkdir -p Students/<github-login>/Lab1/task2
   git archive upstream/Lab1_task2 | tar -x -C Students/<github-login>/Lab1/task2
   cd Students/<github-login>/Lab1/task2
   ```

4. Для третьей задачи замените `task2` и `Lab1_task2` на `task3` и
   `Lab1_task3`. В результате в вашей ветке появятся только ваши каталоги:

   ```text
   Students/<github-login>/Lab1/
   task1/
   task2/
   task3/
   ```

## Подготовка окружения

После перехода в каталог нужной задачи, например
`Students/<github-login>/Lab1/task1`, создайте окружение:

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

## Задача 1. Восстановить зависимости

1. Попробуйте установить корневой проект, тестовые зависимости и три локальных
   пакета одной командой. Если это не получится - нужно понять почему, кто виноват и что делать.

2. После того как получилось сбилдить пакет, попробуйте его запустить
   ```bash
   uvicorn team_board.main:app --reload
   ```

3. Задание считается выполненым, когда пакет успешно запущен и вам удалось открыть главную страницу получившегося сайта


## Задача 2. Исправить календарную функцию

1. Что-то пошло не так. Программисты соседнего отдела говорят, что какой-то тест упал. Может, получится понять в чём проблема, если сбилдить их пакет и запустить тесты...

Тесты запускаются следующим образом:
   ```bash
   pytest
   ```

Если хочется узнать что-то конкретное -
   ```bash
   pytest <путь_до_файла_с_тестами> -q
   ```

Задание считается выполненым, когда все тесты проходят и при этом, их количество и вызовы остались неизмменными.

## Задача 3. Найти расхождение тестов и приложения


1. Что-то на главной странице явно не так... 2/6, это, кажется, чуть больше чем 29%... Но при этом, команда которая отдала вам этот репозиторий утверждает, что у них все тесты проходят... А ещё, они утверждают, что у них классная ридмишка! И её даже можно почитать. Я слышал, что они хвалились, что они классные программисты и хорошо описывают поведение программы в ридмим.

   ```bash
   pytest tests/test_metrics.py -q
   ```

2. Запустите приложение и откройте главную страницу:

   ```bash
   uvicorn team_board.main:app --reload
   ```

   Перейдите по адресу `http://127.0.0.1:8000`, сравните отображаемый процент
   с данными задач.


## Отправка решения через Pull Request

Из корня клона добавьте только папку своей задачи, создайте commit и отправьте
ветку в свой fork. Пример для первой задачи:

```bash
cd ../../../..
git status
git diff -- Students/<github-login>/Lab1/task1
git add Students/<github-login>/Lab1/task1
git commit -m "Complete Lab1 task 1"
git push -u origin lab1/<github-login>/task1
```

На GitHub откройте страницу своего fork и нажмите **Contribute**, затем
**Open pull request**. В форме PR выберите:

- base repository: `Besenok-13/Python_Industrial_Development`;
- base branch: `main`;
- head repository: ваш fork;
- compare branch: `lab1/<github-login>/task1`.

Для задач 2 и 3 замените номер во всех путях, имени ветки и сообщении commit.
Не отправляйте изменения напрямую в `main`.

Если перед слиянием преподаватель обновил `main`, синхронизируйте свою ветку:

```bash
git fetch upstream
git rebase upstream/main
git push --force-with-lease
```
