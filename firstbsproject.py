from bs4 import BeautifulSoup
import requests

headers = {'User-agent': 'Mozilla/5.0' }


bbcrequest = requests.get('https://www.bbc.com/news', headers=headers)
reutersrequest = requests.get('https://www.reuters.com/world', headers=headers)

bbchtml = bbcrequest.content
reutershtml = reutersrequest.content

bbcsoup = BeautifulSoup(bbchtml, 'html.parser')
reuterssoup = BeautifulSoup(reutershtml, 'html.parser')
#print(bbcsoup.prettify())

def bbc_news_scraper():
	news_list =[]
	summary_list = []

	for t in bbcsoup.findAll('h3', class_='gs-c-promo-heading__title'):
		news_title = t.contents[0]
		if news_title not in news_list:
			if 'BBC' not in news_title:
				news_list.append(news_title)
	phrases = ['The latest global news, sport, weather and documentaries', 'BBC', 'Stories from around the world']
	for s in bbcsoup.findAll('p', class_='gs-c-promo-summary'):
		news_summary = s.contents[0]
		if news_summary not in summary_list:
			if 'BBC' in news_summary:
				break
			elif 'The latest global news, sport, weather and documentaries' in news_summary:
				break
			elif 'Stories from around the world' in news_summary:
				break
			summary_list.append(news_summary)

	print("BBC NEWS-------------- \n")		
	for i, title in enumerate(news_list):
		print(i + 1, ':',title)
		if i < len(summary_list):
			print('Summary: ', summary_list[i], '\n')
bbc_news_scraper()

def keyword_bbc_news_scraper(keyword):
	news_list =[]

	for h in bbcsoup.findAll('h3', class_='gs-c-promo-heading__title'):
		news_title = h.contents[0].lower()

		if news_title not in news_list:
			if 'BBC' not in news_title:
				news_list.append(news_title)

	no_of_news = 0
	keyword_list = []
	for i, title in enumerate(news_list):
		text = ''
		if keyword.lower() in title:
			text = ' < -------- KEYWORD'
			no_of_news += 1
			keyword_list.append(title)
		print(i + 1, ':',title, text)
	print(f'\n-----Total Mentions of "{keyword}" = {no_of_news} ------')
	for i, title in enumerate(keyword_list):
		print(i + 1, ':', title)
#keyword_bbc_news_scraper('covid')





def reuters_news_scraper():
	news_list =[]
	summary_list = []

	for t in reuterssoup.findAll('span', class_='MediaStoryCard__title___2PHMeX'):
		news_title = t.contents[0]
		if news_title not in news_list:
				news_list.append(news_title)
	print("REUTERS NEWS-------------- \n")			
	for i, title in enumerate(news_list):
		print(i + 1, ':',title)#
reuters_news_scraper()