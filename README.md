### Очень простой прокси

Применение:
```
mkdir cbr_test && cd $_
git clone https://github.com/beatum/cbrproxy.git
python3.7 -m venv env
source env/bin/activate
pip install pipenv
pipenv install
```
или так
```
pip install -r reuirements.txt
```
запускаем
```
flask run
```
проверяем
```
http://127.0.0.1:5000/api/scripts/XML_daily.asp?date_req=02/03/2003
```
нужную дату указываем в формате date_req=02/03/2003