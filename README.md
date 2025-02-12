# notwordle

I used *some* help from gpt and deepseek to make the game, but for the most part, the logic was written by myself. I built the game by first getting a list of all past wordle games by scrapping it using bs4 library. Then, I used the datetime module to support users being able to call specifics dates and the solution on that day. For example, if they typed:

```
date_input = input("Type Date: ") #(2025,2,9)
month, day, year = datetime.strftime(%B), int(datetime.strftime(%d), datetime.strftime(%Y))
date_str = f"{day} {month} {year}" #2 February 2025
wordle(date_str) #Calls function using the date string
```

In short, we create an input for the user to type in a numerical string-type value and convert it into words as a string using the datetime module and then insert it to be called in the function wordle(date) which takes in a value of the date

Next, in the actual function, I scrape data from a site that contains a list of past wordles by first getting the html file through requests and then parse the file in order to access the text through bs4.

Afterwards, I inspect the page to find which div and class the text is stored in, thankfully it is all contained inside one class and separated also inside p tags. This saves me the trouble of doing more stuff that I had to use chat for.


```
wordle(date):
	...
	body = soup.find('div', class_= 'name_of_class')
	if body:
		lines = body.find_all('p')
		for line in lines:
			if date in line.get_text():
				word = []
				sentence = list(str(line))
```

This important section establishes that if this class exists in the first place, which it does, since I inspect elemented it, then find all lines in the html file inside of this class of tag p. However, since I want to specifically locate the text containing the date which has the wordle solution, I have to iterate through ALL the text, at least until I reach it. Once I do, I store this as a 'sentence' and convert it into list. I know this increases the time complexity of the code, but like who cares! (I'm a noob cut me some slack)

```
word = []
sentence = list(str(line))
for i, char in enumerate(sentence):
	if char == "-":
		word.pop()
		break
	word.append(char)
```

I enumerate in order to append the sentence list to the word list. But the most important thing is that it constantly adds letters until it reaches the character '-,' which is excluded from the word list. 

Ex. 1331. BONUS ==-== 9 February 2025 - I got it on the 3rd try. My current streak is 212.

On this wordle day, or any wordle at all, I stop where the highlight mark is because the rest I do not need, I am solely trying to get the word "BONUS." The word.pop() also removes the extra whitespace at the end of the index

This is what is left of the string now: 1331. BONUS; However, after including the for loop:

```
for i in range (len(word)):
	if word[i] == " ":
		del word[0:i+1]
		break
```

All characters including the space before the word are removed so we are left with: BONUS

---
Now that we have established the word to solve, we can easily create the infamous wordle game.

Here was my approach:

```
1. If guess == word: You win!
2. Else:
	1. If guess[i] == word[i]
	2. If guess[i] in word: Yellow Text
	3. Else: Red Text
```

This was fairly easy to implement 

```
word_str = ("".join(word))
attempts = 1

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
```

While it might seem overwhelming, it is simply just prompting the user to provide a guess, if it is 5 characters, then the user sees if their guess was accurate, and then loops 6 times until it stops and the player loses.

---
Problems:
1. The main problem I am struggling with is implementing a library to check whether the user is typing valid words!
2. I realized I did not put a losing message
3. Player can not play again: Very simply to implement - While True loop

Improvements:
1. Add unique words: User can add own dictionary, or add a more words in general
2. Create randomizer to automatically select wordle game
3. Implement on a website to make an actual wordle copy


2/10/2025
