#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import BeautifulSoup
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import requests
import pandas as pd
import time
#Tutorials:
#https://medium.com/quick-code/python-web-scraping-tutorial-74ace70e01
#https://www.youtube.com/watch?v=88oMlkWSGz0
#file:///D:/Books/PyWebScrapingBook.pdf
##https://www.dataquest.io/blog/web-scraping-tutorial-python/


# <h1># Windows Users</h1>
# 

# In[3]:


#Set the chromedriver path
executable_path = {"executable_path": "/users/evaeb/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


# <font size="5">#Scrape the NASA Mars News</font>
# 
# # Visit the following URL: NASA url 
# #Scrape the NASA Mars News Site and collect the latest News Title and 
# #Paragraph Text. Assign the text to variables that you can reference later.
# url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
# browser.visit(url)
# time.sleep(1)

# In[4]:


#Visit the following URL: NASA url
#Scrape the NASA Mars News Site and collect the latest News Title and

#Paragraph Text. Assign the text to variables that you can reference later. 

url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
browser.visit(url)
time.sleep(1) 


# In[5]:


# Create BeautifulSoup object; parse with 'html.parser'
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[6]:


# Check result
print(soup.prettify())


# In[7]:


# Extract title text
#first article = index[0]
news_title = soup.find_all('div', class_='content_title')[0].find('a').text.strip()
print(news_title)


# In[8]:


# Print all Paragraphs
news_p = soup.find('div', class_="article_teaser_body")
news_p = news_p.text.strip()
print(news_p)


# In[9]:


#Use splinter to navigate the site and find the image url for the current
#Featured Mars Image and assign the url string to a variable called
#featured_image_url.

url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
time.sleep(1) 


# In[10]:


# create soup
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[11]:


# Display the image with IPython.display
#from IPython.display import Image
#Image(url='img.png')
# find the tag : <img ... >

image_link_url = soup.find(class_ = 'button fancybox')
image = image_link_url['data-fancybox-href']

image


# In[12]:


featured_image_url = 'https://www.jpl.nasa.gov' + image
featured_image_url


# <font size='5'>Mars Weather</font>
# 

# In[13]:


#Visit the Mars Weather twitter account here and scrape the latest Mars
# weather tweet from the page. Save the tweet text for the weather report
#as a variable called mars_weather.

url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)
time.sleep(1)


# In[14]:


# create soup
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[15]:


# Check info for elements
print(soup.prettify())


# In[16]:


mars_weather = soup.find(class_="tweet-text")
#
mars_weather = mars_weather.text.strip()
type(mars_weather)
mars_weather


# <h1>### Mars Facts</h1>

# In[17]:


#Visit the Mars Facts webpage here and use Pandas to scrape the table 
#containing facts about the planet including Diameter, Mass, etc.

url = 'https://space-facts.com/mars/'
browser.visit(url)
time.sleep(1)
browser.quit()
tables = pd.read_html(url)
tables


# In[18]:


tables_df = tables[0]
tables_df


# In[19]:


#Convert the data to a HTML table.
tables_df.columns = ['Mars-Earth Comparison', 'Mars', 'Earth']
tables_df.head()


# In[20]:


#Set the index to the Description column
tables_df.set_index('Mars-Earth Comparison', inplace = True)
tables_df


# In[21]:


type(tables_df)


# In[22]:


#Get HTML tables from DataFrames.

html_table = tables_df.to_html()
html_table


# In[23]:


#remove newlines to clean up the table.
mars_html_table = html_table.replace('\n', '')


# In[24]:


mars_html_table


# <h1>### Mars Hemispheres</h1>

# In[25]:


# ### Mars Hemispheres
# * Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
# * You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
# * Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. 
# Use a Python dictionary to store the data using the keys `img_url` and `title`.
# * Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
# ```python
# # Example:
# hemisphere_image_urls = [
#     {"title": "Valles Marineris Hemisphere", "img_url": "..."},
#     {"title": "Cerberus Hemisphere", "img_url": "..."},
#     {"title": "Schiaparelli Hemisphere", "img_url": "..."},
#     {"title": "Syrtis Major Hemisphere", "img_url": "..."},
# ]

# 

#Set the chromedriver path
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
time.sleep(1)


# In[26]:


# Retrieve page with the requests module
# Create soup
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
browser.quit()
# Check result for needed elements
print(soup.prettify())


# In[27]:


hemi_image_links = soup.find_all('div',class_ = 'description')
hemi_image_links


# In[28]:


type(hemi_image_links)


# In[29]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
url_marinerisHemi = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
browser.visit(url_marinerisHemi)   
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[30]:


image_marineris = soup.find_all("img", class_ = 'wide-image')
for image in image_marineris:
    img_marineris="https://astrogeology.usgs.gov"+image['src']

print(img_marineris)


# In[31]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
url_cerberusHemi = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
browser.visit(url_cerberusHemi)   
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[32]:


image_cerberus = soup.find_all("img", class_ = 'wide-image')
for image in image_cerberus:
    img_cerberus="https://astrogeology.usgs.gov"+image['src']

print(img_cerberus)


# In[33]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
url_schiaparelliHemi = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
browser.visit(url_schiaparelliHemi)   
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[34]:


image_schiaparelli = soup.find_all("img", class_ = 'wide-image')
for image in image_schiaparelli:
    img_schiaparelli="https://astrogeology.usgs.gov"+image['src']
print(img_schiaparelli)


# In[35]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
url_syrtisHemi = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
browser.visit(url_syrtisHemi)   
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[36]:


image_syrtis = soup.find_all("img", class_ = 'wide-image')
for image in image_syrtis:
    img_syrtis="https://astrogeology.usgs.gov"+image['src']
print(img_syrtis)


# In[37]:


hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": img_marineris},
    {"title": "Cerberus Hemisphere", "img_url": img_cerberus},
    {"title": "Schiaparelli Hemisphere", "img_url": img_schiaparelli},
    {"title": "Syrtis Major Hemisphere", "img_url": img_syrtis},
]

hemisphere_image_urls


# In[38]:


# Iterate over the image links to obtain dictionary of img titles and img urls

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
time.sleep(1)

hemi_image_links = soup.find_all('div',class_ = 'description')
#hemi_image_links


# In[39]:


# Iterate over the image links to obtain dictionary of img titles and img urls

dict = {}
hemi_dict_list =[]

hemi_url_link =[] 

for i in hemi_image_links:

    title = i.find('h3').text.strip()
    #hemi_dict_list.append(title)
    title = title.replace(' Enhanced', '')  
    
    dict['title'] = title

    url_img_link = i.find('a').attrs['href']
    url_link.append(url_img_link)

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    
    url = 'https://astrogeology.usgs.gov' + url_img_link
    #url_img_link.append(url)
    browser.visit(url)
    time.sleep(1)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hemi_img_urls = soup.find('div', class_="downloads")
    hemi_img_urls =  hemi_img_urls.find('a')["href"]
    
    dict['hemi_img_urls'] =  hemi_img_urls
    
    hemi_dict_list.append(dict)
    dict={}

    browser.quit()
    #print(hemi_dict_list)


# In[40]:


#print(hemisphere_image_urls)
mars_library = {}
mars_library['news_title'] = news_title
mars_library['news_p'] = news_p
mars_library['featured_image_url'] = featured_image_url
mars_library['mars_weather'] = mars_weather
mars_library['mars_facts'] = html_table
mars_library['mars_img_dict'] = hemi_dict_list

mars_library


# In[ ]:




