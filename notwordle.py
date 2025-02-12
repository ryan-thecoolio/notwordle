from bs4 import BeautifulSoup
import sys
import requests
import datetime
import time

def spellingBee(date):
    url = f"https://ladypuzzle.pro/spelling-bee-answers-hints/{date}"
    response = requests.get(url)

    soup = BeautifulSoup(response.text,"html.parser")
    divs = soup.find_all('div',class_="tracking-widest font-bold hidden")
    divs += soup.find_all('div', class_="tracking-widest font-semibold")

    words = []
    for div in divs:
        word = div.get('data-word')
        words.append(word)

    texts = soup.find_all('text', class_="cell-letter svelte-y879vq")
    
    letters = []
    for text in texts:
        letter = text.text.strip()
        letters.append(letter)
    points = 0
    print(f"YOU NEED TO INCLUDE THE FIRST LETTER: {letters[0]}\nCAN BE ANYWHERE IN THE WORD...\n")
    time.sleep(5)
    while True:
        guess = (input(f"{letters}\nGuess the Word (q to quit): ").upper())
        if guess == "Q":
            print("YOU GIVE UP")
            total_points = points
            for word in range (len(words)):
                total_points += len(words[word])
            print(f"TOTAL POINTS: {points}/{total_points}")
            print("WORDS you did not guess:")
            time.sleep(1)
            print(f"{words}")
            break
        while len(guess)<4 or guess not in words:
            guess = (input(f"\n{letters}\nPlease Try Again (q to quit): ").upper())
            if guess == "Q":
                print("YOU GIVE UP")
                total_points = points
                for word in range (len(words)):
                    total_points += len(word)
                print(f"TOTAL POINTS: {points}/{total_points}")
                print("WORDS you did not guess:")
                time.sleep(1)
                print(f"{words}")
                break            
        else:
            if len(guess) == 4:
                points+=1
            else:
                points+=len(guess)
            print(f"Points: {points}")
            words.remove(guess)

date_year = int(input("Enter year (ex. 2025): "))
date_month = int(input("Enter month (ex. 1-12): "))
date_day = int(input("Enter day (ex. 1-31): "))
date_input = datetime.datetime(date_year,date_month,date_day)
year, month, day = date_input.strftime("%Y"), date_input.strftime("%m"), date_input.strftime("%d")
date_str = f"{year}-{month}-{day}"
spellingBee(date_str)
