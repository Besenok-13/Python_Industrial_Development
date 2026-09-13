# Выполнение и отправка лабораторной работы

## Итоговая структура

Каждый студент выполняет все задания лабораторной работы в **одной рабочей ветке** своего fork.

После выполнения лабораторной работы в репозитории должна получиться структура:

```text
Students/
└── <Фамилия-ИО>/
    └── Lab1/
        ├── task1/
        ├── task2/
        └── task3/
```

Например:

```text
Students/
└── Pythonovich-PP/
    └── Lab1/
        ├── task1/
        ├── task2/
        └── task3/
```


> Необходимый формат: фамилия и инициалы латиницей, без пробелов, например `Pythonovich-PP`.

---

## 1. Создайте fork и клонируйте его

На странице исходного репозитория:

```text
Besenok-13/Python_Industrial_Development
```

нажмите **Fork**.

После этого склонируйте **свой fork**:

```bash
git clone https://github.com/<github-login>/Python_Industrial_Development.git
cd Python_Industrial_Development
```

Подключите исходный репозиторий преподавателя как `upstream`:

```bash
git remote add upstream https://github.com/Besenok-13/Python_Industrial_Development.git
git fetch upstream
```

Проверить подключённые репозитории можно командой:

```bash
git remote -v
```

Должно быть два remote:

```text
origin    -> ваш fork
upstream  -> репозиторий преподавателя
```

---

## 2. Создайте одну рабочую ветку для всей лабораторной работы

Рабочую ветку создавайте от актуального `upstream/main`:

```bash
git fetch upstream
git switch --create lab1/<github-login> upstream/main
```

Например:

```bash
git switch --create lab1/ivanov upstream/main
```

Для `Lab1` используется **одна ветка**. Не создавайте отдельные ветки для `task1`, `task2` и `task3`.

---

## 3. Создайте папки для всех заданий

Из корня репозитория выполните:

```bash
mkdir -p Students/<Фамилия-ИО>/Lab1/task1
mkdir -p Students/<Фамилия-ИО>/Lab1/task2
mkdir -p Students/<Фамилия-ИО>/Lab1/task3
```

Например:

```bash
mkdir -p Students/Pythonovich-PP/Lab1/task1
mkdir -p Students/Pythonovich-PP/Lab1/task2
mkdir -p Students/Pythonovich-PP/Lab1/task3
```

---

## 4. Скопируйте стартовые файлы заданий

Стартовые версии заданий находятся в ветках исходного репозитория:

```text
Lab1_task1
Lab1_task2
Lab1_task3
```

Обновите информацию о ветках:

```bash
git fetch upstream
```

Скопируйте содержимое каждой ветки в соответствующую папку:

```bash
git archive upstream/Lab1_task1 | tar -x -C Students/<Фамилия-ИО>/Lab1/task1
git archive upstream/Lab1_task2 | tar -x -C Students/<Фамилия-ИО>/Lab1/task2
git archive upstream/Lab1_task3 | tar -x -C Students/<Фамилия-ИО>/Lab1/task3
```

Например:

```bash
git archive upstream/Lab1_task1 | tar -x -C Students/Pythonovich-PP/Lab1/task1
git archive upstream/Lab1_task2 | tar -x -C Students/Pythonovich-PP/Lab1/task2
git archive upstream/Lab1_task3 | tar -x -C Students/Pythonovich-PP/Lab1/task3
```

После этого структура должна выглядеть так:

```text
Students/
└── Pythonovich-PP/
    └── Lab1/
        ├── task1/
        │   └── ...
        ├── task2/
        │   └── ...
        └── task3/
            └── ...
```

Не изменяйте ветки `Lab1_task1`, `Lab1_task2` и `Lab1_task3`. Они используются только как источник стартовых файлов.

---

## 5. Выполните задания локально

Работайте только внутри своей папки:

```text
Students/<Фамилия-ИО>/Lab1/
```

То есть:

```text
Students/<Фамилия-ИО>/Lab1/task1/
Students/<Фамилия-ИО>/Lab1/task2/
Students/<Фамилия-ИО>/Lab1/task3/
```

Можно выполнить сначала `task1`, затем `task2` и `task3`, не отправляя изменения на GitHub.

Проверить изменения можно командой:

```bash
git status
```

Также можно делать локальные commits во время работы. Отправлять (`push`) их на GitHub до окончания лабораторной работы необязательно.

---

## 6. После выполнения всех заданий создайте commit

Перейдите в корень репозитория и проверьте изменения:

```bash
git status
git diff -- Students/<Фамилия-ИО>/Lab1
```

Добавьте **только свою папку лабораторной работы**:

```bash
git add Students/<Фамилия-ИО>/Lab1
```

Например:

```bash
git add Students/Pythonovich-PP/Lab1
```

Создайте commit:

```bash
git commit -m "Complete Lab1"
```

Если во время работы вы уже создавали локальные commits, создавать ещё один общий commit необязательно. Главное — убедитесь, что все изменения сохранены в commits:

```bash
git status
```

Перед отправкой должно быть:

```text
nothing to commit, working tree clean
```

---

## 7. Синхронизируйте ветку с актуальным `main`

Перед первым `push` рекомендуется получить последние изменения моего репозитория:

```bash
git fetch upstream
git rebase upstream/main
```

Если возникнут конфликты, исправьте их, затем выполните:

```bash
git add <исправленные-файлы>
git rebase --continue
```

---

## 8. Отправьте лабораторную работу в свой fork

После выполнения **всех трёх заданий** отправьте рабочую ветку в свой GitHub fork:

```bash
git push -u origin lab1/<github-login>
```

Например:

```bash
git push -u origin lab1/ivanov
```

После этого выполненные задания будут находиться в вашем fork в ветке:

```text
lab1/<github-login>
```

в папках:

```text
Students/<Фамилия-ИО>/Lab1/task1/
Students/<Фамилия-ИО>/Lab1/task2/
Students/<Фамилия-ИО>/Lab1/task3/
```

---

## 9. Создайте Pull Request

Откройте свой fork на GitHub.

Нажмите **Contribute -> Open pull request**.

Проверьте параметры Pull Request:

```text
base repository:    Besenok-13/Python_Industrial_Development
base branch:        main

head repository:    <github-login>/Python_Industrial_Development
compare branch:     lab1/<github-login>
```

Таким образом, один Pull Request содержит всю лабораторную работу:

```text
Students/<Фамилия-ИО>/Lab1/
├── task1/
├── task2/
└── task3/
```

---

## 10. Если `main` изменился после создания Pull Request

Если я обновил `main` до того, как ваш Pull Request был принят, обновите свою ветку:

```bash
git fetch upstream
git switch lab1/<github-login>
git rebase upstream/main
```

После успешного rebase обновите ветку в своём fork:

```bash
git push --force-with-lease origin lab1/<github-login>
```

Используйте именно `--force-with-lease`, а не обычный `--force`.

---

## Краткая схема работы

```text
Исходный репозиторий преподавателя
Besenok-13/Python_Industrial_Development
            │
            │ Fork
            ▼
Ваш GitHub fork
<github-login>/Python_Industrial_Development
            │
            │ Clone
            ▼
Локальный компьютер
            │
            ├── создать ветку lab1/<github-login>
            │
            ├── Students/<Фамилия-ИО>/Lab1/task1
            ├── Students/<Фамилия-ИО>/Lab1/task2
            ├── Students/<Фамилия-ИО>/Lab1/task3
            │
            ├── выполнить все задания
            ├── commit
            │
            │ push
            ▼
Ваш GitHub fork
ветка lab1/<github-login>
            │
            │ Pull Request
            ▼
Besenok-13/Python_Industrial_Development
main
```
