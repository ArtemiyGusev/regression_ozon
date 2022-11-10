## Проект по тестированию: 

#### WEB - https://www.bmw.ru/
#### MOBILE - https://vkusvill.ru/
#### API - http://shop.bugred.ru/
  

## Технологии, используемые в данном проекте

</br>
<p>
<img width="50px" title="Allure" src="resources/image/logo/Allure.svg">
<img width="50px" title="Appium" src="resources/image/logo/Android.svg">
<img width="50px" title="Appium" src="resources/image/logo/Appium.svg">
<img width="50px" title="Pytest" src="resources/image/logo/Browserstack.svg">
<img width="50px" title="Github" src="resources/image/logo/GitHub.svg">
<img width="50px" title="Jenkins" src="resources/image/logo/Jenkins.svg">
<img width="50px" title="Selenoid" src="resources/image/logo/Selenoid.svg">
<img width="50px" title="PyCharm" src="resources/image/logo/pycharm.png">
<img width="50px" title="Pytest" src="resources/image/logo/pytest.png">
<img width="50px" title="Python" src="resources/image/logo/python.png">
<img width="50px" title="Requests" src="resources/image/logo/requests.png">
<img width="50px" title="Selene" src="resources/image/logo/selene.png">
<img width="50px" title="Selenium" src="resources/image/logo/selenium.png">
<img width="50px" title="Telegram" src="resources/image/logo/Telegram.svg">
</p>
<br>

В данном проекте автотесты написаны на **Python** с использованием фреймворка для тестирования **Selene\Selenium**.

Запуск тестов выполняется из **Jenkins**. **Selenoid** используется для запуска браузеров в контейнерах **Docker**. 

**Browserstack** используется для запуска мобильных тестов, для запуска на эмуляторе используются **Android Studio** и **Appium**. 

**Allure Report** и **Telegram Bot** используются для визуализации результатов тестирования.

<br>

## Тест кейсы

### Тест кейсы для UI тестирования

✓ Тест на проверку элементов навигации на главной странице

✓ Тест на поиск вакансии

✓ Тест на просмотр определенной модели авто

✓ Тест на поиск компании Kodix

✓ Тест проверки локации


### Тест кейсы для api тестирования

✓ Тест создания элемента

✓ Тест на проверку созданного элемента

✓ Тест на обновление элемента

✓ Тест на проверку элемента в БД

✓ Тест на удаление элемента


### Тест кейсы для mobile тестирования

✓ Тест swipe основных элементов

✓ Тест на определение локации

✓ Тест на удаления информации

✓ Тест на просмотр контактов

✓ Тест просмотра программы лояльности

<br>


## Информация о тестах в [Allure report](https://jenkins.autotests.cloud/job/Elieeeya_qa_guru_final/allure/)

### Главное окно

![](resources/image/logo/Снимок%20экрана%202022-11-07%20в%2003.08.11.png)

### Окно с тестовыми кейсами

![](resources/image/logo/Снимок%20экрана%202022-11-07%20в%2003.11.12.png)

### Окно с графиками

![](resources/image/logo/Снимок%20экрана%202022-11-07%20в%2003.11.22.png)







## Уведомление в Telegram

После завершения тестов отчет о прохождении приходит в Telegram с помощью заранее созданного бота
![](resources/image/logo/Снимок%20экрана%202022-11-07%20в%2003.16.14.png)

### Видео прохождения UI тестов (пример)

![](resources/image/logo/07cd2e36d877f671728f30bf0bcf2a98.gif)

### Видео прохождения mobile тестов (пример)

![](resources/image/logo/video-e75d486ef3366f54d000daa012cf64329880041e.gif)