# Nifty50-Web-Scraping

1. pip install -r requirements.txt
2. cd Zero
3. celery -A tasks worker --loglevel=info (background periodic worker for scraping)
4. run python app.py in a new terminal session
5. open localhost:8080
