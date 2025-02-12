from bs4 import BeautifulSoup
import sys
import requests
import datetime
from textblob import TextBlob

def wordle_finder(date):
    try:
        url = 'https://www.stadafa.com/2021/09/every-worlde-word-so-far-updated-daily.html'
        response = requests.get(url)
        soup = BeautifulSoup(response.text,"html.parser")
        body = soup.find('div',class_="post-body entry-content float-container")
        if body:
            lines = body.find_all('p')
            for line in lines:
                if date in line.get_text():
                    sentence = list(str(line))
                    word = []
                    for i, char in enumerate(sentence):
                        if char == "-":
                            word.pop()
                            break
                        word.append(char)
        for i in range (len(word)):
            if word[i] == " ":
                del word[0:i+1]
                break
        word_str = ("".join(word))
        attempts = 1
        print("Welcome to Ryan's Knockoff Wordle! To play this game, enter a 5 letter word. You have 6 chances to guess the word.")
        print("Ready?")
        while attempts <= 6:
            guess = input(f"Guess #{attempts}: ").upper()
            spellCheck = str(TextBlob(guess).correct()).upper()
            if guess != spellCheck:
                guess = (input(f"Guess #{attempts} (Try Again): ").upper())
            if len(guess) != 5:
                guess = (input(f"Guess #{attempts} (Try Again): ").upper())
                continue

            if guess == word_str:
                print(5*u'\u2705')
                print(f"You guessed the word: {word_str}")
                return
            else:
                closeness_str = ""
                guess = list(guess)
                for i in range (len(word)):
                    if word[i] == guess[i]:
                        closeness_str += u'\u2705'
                    elif word[i] in guess:
                        closeness_str += '\U0001F7E8'
                    else:
                        closeness_str += u'\u274C'
                print(closeness_str)
            attempts +=1
        print(f"The word was: {word_str}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to Fetch Data: {e}", file=sys.stderr)

date = datetime.datetime(2025,2,9)
month, day, year = date.strftime("%B"), int(date.strftime("%d")), date.strftime("%Y")
date_str = f"{day} {month} {year}"
wordle_finder(date_str)
