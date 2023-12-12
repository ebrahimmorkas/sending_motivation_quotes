# This project will send you motivation quote on every monday.
# Logic:
# Select 10 quotes from internet and store it in .txt file. Open that file in read mode. Now don't read the whole file at once but using for-in loop, loop the file using readline() method which returns the single line of the file and we will store in it the variable. Above the loop we will create the list in which in every iteration we will append that variable to list which is holding the single quote and this way the list will contain all the quotes. Now using datetime module we will get the current day and we will get the current day in english words and we will compare that. If  that day is equal to monday then we will send the email using smtplib module

import random
import datetime as dt
import smtplib
# Opening the quotes file
try:
    quotes_file = open("quotes.txt", 'r')
except FileNotFoundError:
    print("Quotes file not found")
else:
    # print(quotes_file.read())

    # Creating the list that will hold all the quotes
    quotes_list = []
    for line in quotes_file:
        single_quote = quotes_file.readline()
        quotes_list.append(single_quote)

    # print(quotes_list)

    # Generating the random qute from the list
    random_quote = random.choice(quotes_list)
    # print(random_quote)

    # Getting the current date
    current_date = dt.datetime.now()
    # print(current_date.strftime("%A"))
    day_in_words = current_date.strftime("%A")
    if day_in_words == "Monday":
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login("morkasebrahim3@gmail.com", "alhd fcpw miau jyxb")
        connection.sendmail(from_addr="morkasebrahim3@gmail.com",
                            to_addrs="morkasebrahim3@gmail.com",
                            msg=f"Subject: Sending the motivation quote to stay motivated\n\n Here's your motivation quote {random_quote}")
        connection.close()