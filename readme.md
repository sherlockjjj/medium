## Medium Recommender Project

### Install Requirements:
1. conda create env -n medium
2. source activate medium
3. conda install -c conda-forge scrapy
4. conda install pymongo

### sample command: 
1. cd medium/mediumScrapder
2. mongod --dbpath ~/data/db
3. scrapy crawl my_scraper -o sample.jl -a tag='datascience' -a date='2018/01/01/'

### Web App Install Requirements:
1. npm install -g @angular/cli
2. cd my-medium-app
3. ng serve 

