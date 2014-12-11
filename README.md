jrscraper
=========

Deployment notes:

1. Activate virtual enviroment using source venv/bin/activate
2. Install requirements using pip install -r requirements.txt
3. Open folder jrscraper
4. Run the command python manage.py crawl to crawl justrentals search page
5. Run the command python manage.py runserver and enter the url /listing/search/

Notes:
* The code assumes default elasticsearch installation on localhost
* The crawl command takes optional --count param to specify number of crawled documents
* The search page takes optional count param to specify number of view documents
