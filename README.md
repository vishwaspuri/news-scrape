# news-scrape

### This API was built for GoI website during March-April 2020 and would be of no use now other than learning purposes.

Create virtual environment
```
virtualenv env
source env/bin/activate
```

Download requirements 
```
pip install -r requirements.txt
```

Change into api directory
```
cd news_api
```

Make migrations and migrate
```
python manage.py migrate
python manage.py makemigrations
```
Runserver
```
python manage.py runserver
```


