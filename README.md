# smart-hotel
Инструкция
----------

1. Откройте проект в PyCharm или другой IDE
2. В терминале убедитесь что вы в папке проекта и зайдите активируйте вашу виртуальную среду
3. Зайдите в Виртуальную среду ----> Scripts и пропишите pip install -r requirements.txt
4. После установки всех requirements идите в Run ----> Edit Configurations ----> Выберите файл для заупуска
	app.py если вы в проекте BACK_END и recognition.py если вы в проекте FACE_RECOGNITION
	
5. Нажмите run и программа запустится

**Важно!!!** Сначала запустите BACK_END (app.py). В адресной строке пропишите photos/new/ далее откроется форма регистрации юзера
Зарегестрируйте юзера и загрузите фотографию в форму
Далее запустите FACE_RECOGNTION (recognition.py) и откроется камера, которая распознает зарегистрированных юзеров и выводит имя пользователя с количеством дней до конца резервации

************************************************************

Могут быть проблемы с установкой dlib и cmake при установке библиотеки face_recognition 

Чтобы избежать сделайте следующее:
***
**Шаг 1 (установите cmake на ваш компьютер):**
***
Вариант 1:

* Установить через графически инстоллер с сайта cmake.org/downloads

* Убедитесь что поставили галочку add cmake to path for all users
***
Вариант2:

* Установите Visual Studio на ваш компьютер и перейдите во вкладку Individual Components

* Там поставьте галочку напротив Visual C++ tools for СMake

**Шаг2 (установите dlib на ваш компьютер):**
***
* Перейдите по ссылке https://pypi.org/project/dlib/19.18.0/#files and download dlib и загрузите dlib
* Разорхивируйте, перейдите в папку dlib-19.19.0 и скопируйте все что внутри
***
* Перейдите в виртуальную среду ---> Lib ---> site-packages и вставьте скопированное сюда
***

**Шаг3:**
***
Перейдите в папке Scripts в виртуальной среде и пропишите:
* pip install cmake
* pip install dlib 
***

**Шаг4:**
***
Теперь находясь в среде установите все requirements.txt
* pip install -r requirements.txt
***

**Шаг5:**
***
* После того как все requirements.txt установлены перейдите в Run ---> Edit Configurations и выберите файл для запуска
***
**Шаг6:**
***
* Запустите проект
***


----------------------------------------------------------------------------------------------------------------------------------------
Instruction
-----------
1. open project in PyCharm or other IDE
2. in terminal activate your virtual environment go to Scripts and run: pip install -r requirements.txt
3. after installing all requirements go to Run ---> Edit Configurations and Select the file
from which you want to run the code (in our case: app.py in back_end/main.py in face_recognition)


***********************************************************
Some problems with dlib and cmake may occur when installing face_recognition library.
To avoid do the following (for Windows):

**Step one (install cmake on your computer):**
Way1: 
*Install cmake. To do this, download a graphical installer from cmake.org/downloads.
*When installing, make sure to tick the box add cmake to path for all users, or this guide won't work.
Way2:
*Install Visual Studio on your computer and during installation go to Individual components and select
*Visual C++ tools for CMake
	
	After that go to Scripts folder of your virtual environment and run: pip install cmake
**Step two (install dlib on your computer):**
*Go to https://pypi.org/project/dlib/19.18.0/#files and download dlib
*Unarchivate it and go to folder dlib-19.19.0 and copy everything inside this folder
*Go to your virtual environment ---> Lib ---> site-packages and paste copied data here

**Step three:**
Go to Scripts of your Virtual Environment and run:
* pip install cmake
* pip install dlib

**Step four:**
Now inside the Scripts of your Virtual Environment run:
*pip install -r requirements.txt  

**Step five:**
After all requirements are installed go to:
*Run ---> Edit Configuration and select the python file to run the program from
*app.py (in BACK_END project) and face_recogintion.py (in FACE_RECOGNITION project)

	


