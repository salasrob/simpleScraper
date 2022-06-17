from bs4 import BeautifulSoup
import os
import functions
import requests



def main_scraper(url, directory):
	functions.create_directory(directory)
	source_code = requests.get(url)
	source_text = source_code.text
	soup = BeautifulSoup(source_text, "html.parser")
	articles = soup.find_all("article", {'class':'w-full'})
	for a in articles:
		print(a.text)
		print(a.a.get('href'))
		print()
		article_formatted = a.a.get('href') + "\n" + a.text 
		if functions.does_file_exist(directory+"/articles.txt") is False:
			functions.create_new_file(directory+"/articles.txt")
		functions.write_to_file(directory+"/articles.txt", article_formatted)
		


main_scraper("https://www.tenethealth.com/locations", "TenetHealth")


functions.read_lines("Orthofix/articles.txt", 5)

def get_details(url):
	source_code = requests.get(url)
	source_text = source_code.text
	soup = BeautifulSoup(source_text, "html.parser")
	divEntry = soup.find("div", {'class': 'entry'})
	soup = BeautifulSoup(str(divEntry), 'html.parser')
	paragraphs = soup.find_all("p")
	print("")
	print("Paragraphs:")
	functions.write_to_file("Orthofix/articles.txt", "Paragraphs: \n\n")
	for p in paragraphs:
		if p.string is not None:
			if "coffee" in p.string:
				print(p.string)
			functions.write_to_file("Orthofix/articles.txt", p.string)
		print("---------------------------")
		print("---------------------------")
		print("---------------------------")
		functions.write_to_file("Orthofix/articles.txt", "--------------------------- \n\n")




