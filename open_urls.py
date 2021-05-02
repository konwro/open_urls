# Task: Open urls list from input .txt, .xlsx, .csv file in new browser tabs

# Step 0: imports
import pandas as pd 
import webbrowser
import time

# Step 1: load the input file with URLs to open (with 'url' column name)
urls_to_open = pd.read_csv(r'/filepath/urls.txt')
# urls_to_open = pd.read_excel(r'/filepath/urls.xlsx')
# print(urls_to_open.head())

# Step 2: specify browser
c = webbrowser.get('firefox')
c.open_new('https://duckduckgo.com')

# Step 3: open urls in browser
for url in urls_to_open['url']:
    c.open_new_tab(url)
    print(url)
    time.sleep(4)

# Step 4: operation summary
print('======================All URLs have been opened======================')
print('No. of opened URLs: %d' %(len(urls_to_open)))
