from bs4 import BeautifulSoup

# Load the saved file
with open("full_page.html", "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')
re=soup.find_all(name=['h5','small','strong',]) 

for card in re:
    print(card.text)



#  to get more details i have to click on the "view details" buttons 
#  then fetch the details and print them out 
#  from home page/ or the project page i can't fetch all the details
#  there is GST no under the promoter details section its going to be long program
#  its going to be intresting
