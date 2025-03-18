## 1\. Файловая структура проекта

---

```plaintext
├── data/                   # Директория для хранения данных.
    ├──locators/            # Директория для хранения локаторов страниц.
    ├── assertions          # Doesn`t exists yet. Файл для хранения функций проверки ожиданий.
    ├── main_page_data      # Doesn`t exists yet. Файл для формализации используемых данных.
    ├── urls                # Файл для хранения url.
├── pages/                  # Директория с модулями страниц.
    ├── base_page           # Класс и методы базовой страницы.
    ├── ...                 # Классы и методы конкретных страниц.
├── tests/                  # Исполняемые тесты.
    ├── ...
├── .gitignore  
├── README.md               # Информационный файл. Вы находитесь здесь:)
├── pytest.ini              # Конфигурационный файл для фреймворка pytest.
├── requirements.txt        # Список используемых библиотек и плагинов.
```
---

## 2. Порядок построения фреймворка:
1. Создать conftest.py и инициализировать драйвер.
2. Создать директорию pages:

    2.1  В модуле base_page прописать методы, общие для всех страниц:

   - open_page, find_element;
   - click, double_click, right_click;
   - send_keys;
   - element_is_visible/present etc.

    2.2 В модулях страниц прописать методы, уникальные для конкретной страницы:

    - fill_form;
    - login, forgot_password, switch_to_registration;
    - accept_terms_and_conditions;
    - apply_promo_code etc.
   
3. Создать директорию locators. Локаторы каждой страницы описываются отдельно.
4. Создать директорию data.
5. Создать директорию tests.

---


## 3. Инструкция для запуска автоматизированных тест-кейсов.

---

1.  Убедитесь, что на Вашем компьютере установлен Python. В терминале выполните команду:
    
    *   для Windows:
        
        ```plaintext
        python --version
        ```
        
    *   для MacOS:
        
        ```plaintext
        python3 --version
        ```

    Если Python установлен, то вы увидите сообщение с версией.
    
    Если он не установлен, то установите с официального [сайта Python](https://www.python.org/downloads/), выбрав подходящую версию для Вашей операционной системы, и пройдите шаг сначала. В процессе установки обязательно поставьте галочку в чекбоксе "Add python.exe to PATH". Иначе, у Вас не будет корректно отображаться версия Python.

    
2.  Откройте терминал, перейдите в нужную Вам директорию с помощью команды:
    
    ```plaintext
    cd <здесь укажите путь до директории с проектом>
    ```
    
3.  Склонируйте к себе репозиторий, в котором хранится проект тестового задания, через выполнение команды в терминале:
    
    ```plaintext
    git clone https://github.com/YuriKey/practice_simbirsoft.git
    ```
    
    и перейдите в директорию проекта:
    
    ```plaintext
    cd practice_simbirsoft
    ```
    
4.  Создайте виртуальное окружение командой:
    
    *   для Windows:
        
        ```plaintext
        python -m venv .venv
        ```
        
    *   для MacOS:
        
        ```plaintext
        python3 -m venv .venv
        ```
        
        и активируйте его:
        
    *   для Windows:
    
    ```plaintext
    .venv\Scripts\activate
    ```
    
    ```plaintext
    source .venv/bin/activate
    ```
    
5.  Установите зависимости, указанные в файле **requirements.txt**:
    
    ```plaintext
    pip install -r requirements.txt
    ```
    
6.  Запустите тесты в консоли командой:
    
    ```python
    pytest
    ```

7. После завершения тестов выполните в консоли команду:

    ```python
    allure serve allure_results
    ```