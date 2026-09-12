## Как Python находит и устанавливает код проекта

В промышленной разработке на Python часто встречается команда:

```bash
python -m pip install -e ".[dev]"
```

На первый взгляд кажется, что она просто скачивает зависимости. На самом деле здесь происходит больше.

Разберём команду по частям.

`python -m pip` запускает `pip` через конкретный интерпретатор Python. Это полезно, потому что так мы точно устанавливаем пакеты в то окружение, которым пользуемся.

`install` означает установить пакет.

`.` означает: установить Python-проект из текущей директории.

`[dev]` означает: кроме обычных зависимостей проекта установить дополнительную группу зависимостей с именем `dev`.

Например:

```toml
[project.optional-dependencies]
dev = [
    "pytest",
    "ruff",
    "mypy",
]
```

Тогда:

```bash
python -m pip install -e ".[dev]"
```

означает примерно:

```text
установить текущий проект
+
установить pytest, ruff, mypy
+
сделать установку editable
```

### Зачем вообще устанавливать собственный проект

Для одного небольшого файла установка обычно не нужна:

```bash
python script.py
```

Но промышленный проект обычно представляет собой пакет:

```text
project/
├── pyproject.toml
├── src/
│   └── myproject/
│       ├── __init__.py
│       ├── cv/
│       └── nlp/
└── tests/
```

Мы хотим, чтобы из тестов и других частей программы можно было писать:

```python
from myproject.cv.classifier import Classifier
```

То есть использовать собственный код так же, как любой другой установленный Python-пакет.

Именно для этого проект часто устанавливают в виртуальное окружение.

### Что меняет `-e`

Если выполнить:

```bash
python -m pip install .
```

`pip` собирает проект и устанавливает его обычным способом.

Упрощённо можно представить:

```text
исходники проекта
      ↓
сборка
      ↓
установленный пакет в окружении
```

После этого изменение файлов в репозитории не обязано менять уже установленную копию. Чтобы точно установить новую версию, потребуется снова выполнить `pip install .`.

В режиме разработки это неудобно.

Поэтому используют:

```bash
python -m pip install -e .
```

`-e` означает editable install.

Окружение начинает использовать исходный код из рабочей директории, поэтому разработчик может изменить:

```text
src/myproject/cv/classifier.py
```

и при следующем запуске Python эти изменения уже будут доступны без повторной установки проекта.

При этом сам пакет считается установленным.

Именно это сочетание и удобно:

```text
проект установлен как нормальный пакет
+
редактируем исходники прямо в репозитории
```

Техническая реализация editable install зависит от build backend и формата проекта, поэтому не стоит понимать её буквально как обычное копирование файлов или простое добавление одной строки в `sys.path`. Но концептуально окружение получает возможность находить пакет непосредственно в рабочем дереве проекта.

---

## Почему нельзя просто запускать все `.py`-файлы

Можно написать:

```bash
python src/myproject/cv/classifier.py
```

Но тогда Python запускает `classifier.py` как отдельный скрипт.

Это важно.

Если внутри файла есть:

```python
from .utils import preprocess
```

точка означает:

```text
импортировать utils из моего текущего пакета
```

Но при прямом запуске:

```bash
python src/myproject/cv/classifier.py
```

Python может не знать, что этот файл является модулем:

```text
myproject.cv.classifier
```

Для него это просто исполняемый файл `__main__`.

Из-за этого относительный импорт может закончиться ошибкой:

```text
ImportError: attempted relative import with no known parent package
```

Если же пакет установлен, модуль можно запустить как часть пакета:

```bash
python -m myproject.cv.classifier
```

Теперь Python знает его полное имя:

```text
myproject.cv.classifier
```

и понимает, относительно какого пакета нужно интерпретировать:

```python
from .utils import preprocess
```

---

## Как Python вообще находит модули

В основе механизма импорта находится `sys.path`.

Посмотреть его можно так:

```python
import sys

for path in sys.path:
    print(path)
```

`sys.path` — это список директорий, внутри которых Python ищет top-level модули и пакеты.

Например:

```python
import requests
```

означает примерно:

```text
для каждой директории в sys.path:
    ищем requests.py
    или requests/
```

Если подходящий модуль найден, Python использует его.

Важно понимать:

```text
sys.path содержит не сами пакеты,
а директории, внутри которых эти пакеты находятся.
```

Например, если пакет лежит здесь:

```text
/project/src/myproject/
```

то Python должен знать про:

```text
/project/src
```

а не про:

```text
/project/src/myproject
```

Тогда:

```python
import myproject
```

может найти:

```text
/project/src/myproject
```

---

## Откуда появляется проблема с `src`

Рассмотрим:

```text
project/
├── pyproject.toml
└── src/
    └── myproject/
        └── classifier.py
```

Если мы запустили Python из `/project`, в `sys.path` может присутствовать:

```text
/project
```

Но пакет находится не здесь:

```text
/project/myproject
```

а здесь:

```text
/project/src/myproject
```

Поэтому для:

```python
import myproject
```

Python нужен путь:

```text
/project/src
```

Можно было бы сделать:

```bash
PYTHONPATH=src python ...
```

или даже:

```python
import sys

sys.path.append("/project/src")
```

Но в нормальном проекте ручное изменение `sys.path` обычно не требуется.

Вместо этого проект устанавливают:

```bash
python -m pip install -e .
```

После этого окружение знает, как найти `myproject`.

---

## Почему существует структура `src/`

Можно было бы сделать:

```text
project/
├── myproject/
└── tests/
```

и тогда при запуске Python из корня проекта пакет часто находился бы просто потому, что `/project` присутствует в `sys.path`.

Но это может скрывать ошибки упаковки.

Поэтому часто используют:

```text
project/
├── pyproject.toml
├── src/
│   └── myproject/
└── tests/
```

Теперь исходники не импортируются случайно только потому, что мы находимся в корне репозитория.

Мы должны корректно установить пакет.

Это помогает тестировать проект в условиях, более близких к реальному использованию:

```text
разработчик:
pip install -e .

пользователь:
pip install myproject
```

В обоих случаях используется пакет `myproject`, а не случайно найденная директория из репозитория.

---

## А что тогда означает `import src.requests`

Импорт:

```python
import src.requests
```

означает, что Python считает `src` первым компонентом имени модуля.

Он делает примерно следующее:

```text
найти src через sys.path
↓
внутри src найти requests
```

Например:

```text
/project/
└── src/
    └── requests.py
```

Если `/project` находится в `sys.path`, то:

```python
import src.requests
```

может сработать.

Но при классическом `src`-layout это обычно не то, чего мы хотим.

Если структура такая:

```text
project/
└── src/
    └── myproject/
        └── classifier.py
```

`src` — это не часть публичного имени пакета. Это просто каталог, где физически лежат исходники.

Мы хотим:

```python
import myproject
```

а не:

```python
import src.myproject
```

После правильной установки `/project/src` становится source root для пакетов, и `myproject` становится top-level именем.

---

## Что происходит, если модулей с одинаковым именем несколько

Предположим:

```text
sys.path:

1. /project
2. /shared
3. /venv/lib/python3.12/site-packages
```

И существует:

```text
/project/classifier.py
/shared/classifier.py
```

Тогда:

```python
import classifier
```

обычно найдёт первый подходящий `classifier`.

Порядок `sys.path` имеет значение.

То же самое может неожиданно произойти с библиотеками:

```text
project/
├── requests.py
└── app.py
```

В `app.py`:

```python
import requests
```

может импортироваться локальный:

```text
/project/requests.py
```

вместо установленной библиотеки `requests`.

Это называется shadowing.

Проверить, что реально импортировалось, можно:

```python
import requests

print(requests.__file__)
```

Ещё до импорта можно посмотреть, что будет найдено:

```python
import importlib.util

spec = importlib.util.find_spec("requests")
print(spec.origin)
```

Кроме того, после первого успешного импорта модуль обычно сохраняется в:

```python
sys.modules
```

Поэтому повторный:

```python
import requests
```

обычно возвращает уже загруженный модуль, а не выполняет весь поиск заново.

---

## Что делать, если у нас два `classifier`

Допустим, проект устроен так:

```text
src/
└── myproject/
    ├── cv/
    │   └── classifier.py
    └── nlp/
        └── classifier.py
```

Это абсолютно нормальная структура.

Python различает модули не только по имени файла, а по полному имени:

```text
myproject.cv.classifier
myproject.nlp.classifier
```

Поэтому CV-классификатор можно импортировать:

```python
from myproject.cv.classifier import Classifier
```

а NLP-классификатор:

```python
from myproject.nlp.classifier import Classifier
```

Если оба нужны одновременно:

```python
from myproject.cv.classifier import Classifier as CVClassifier
from myproject.nlp.classifier import Classifier as NLPClassifier
```

Теперь:

```python
cv_model = CVClassifier()
nlp_model = NLPClassifier()
```

Никакого конфликта нет, потому что полные имена модулей различаются.

Можно импортировать и сами модули:

```python
from myproject.cv import classifier as cv_classifier
from myproject.nlp import classifier as nlp_classifier
```

а затем:

```python
cv_classifier.Classifier()
nlp_classifier.Classifier()
```

---

## Абсолютные и относительные импорты

Внутри:

```text
myproject/cv/pipeline.py
```

можно написать:

```python
from .classifier import Classifier
```

`.` означает текущий пакет:

```text
myproject.cv
```

Поэтому фактически речь идёт о:

```python
from myproject.cv.classifier import Classifier
```

Если из `cv` нужно импортировать NLP-классификатор, технически можно написать:

```python
from ..nlp.classifier import Classifier
```

Здесь:

```text
.   → myproject.cv
..  → myproject
```

Но для зависимостей между крупными компонентами проекта часто удобнее абсолютная форма:

```python
from myproject.nlp.classifier import Classifier
```

Она сразу показывает, от какого компонента зависит текущий код.

---

## Итоговая модель

Всю эту тему удобно держать в голове как несколько правил.

`pip install .` устанавливает не только зависимости, но и сам текущий проект.

`pip install -e .` устанавливает проект в режиме разработки, чтобы изменения исходников использовались без постоянной переустановки.

`[dev]` означает дополнительную группу зависимостей:

```bash
python -m pip install -e ".[dev]"
```

— установить проект editable и добавить инструменты разработки.

При импорте Python не ищет файлы по всему диску. Он использует систему импорта и каталоги из `sys.path`.

Для:

```python
import myproject.cv.classifier
```

модель поиска можно представить так:

```text
sys.path
   ↓
найти myproject
   ↓
внутри найти cv
   ↓
внутри найти classifier
```

Если два файла называются одинаково:

```text
cv/classifier.py
nlp/classifier.py
```

это не проблема, потому что их полные имена различаются:

```text
myproject.cv.classifier
myproject.nlp.classifier
```

И наконец, отдельный `.py`-файл и модуль внутри установленного пакета — не совсем одно и то же. Поэтому в промышленном проекте обычно стараются работать с пакетами, запускать модули через `python -m ...`, использовать корректную структуру импортов и устанавливать проект в виртуальное окружение через `pip`.
