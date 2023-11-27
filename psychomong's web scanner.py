import requests                                 #for any kind of work we need to tell the python to do for the websites we use the requests module to send and recieve the data
from bs4 import BeautifulSoup                   #Beautiful Soup is a Python library for pulling data out of HTML and XML files. It provides Pythonic idioms for iterating, 
                                  #searching, and modifying the parse tree. Beautiful Soup automatically converts incoming documents to Unicode and outgoing documents to UTF-8. 
             #It sits on top of popular Python parsers like html.parser, lxml, and html5lib, allowing you to try out different parsing strategies or trade speed for flexibility.
import tkinter as tk #this is for the GUI Making easily
from tkinter import scrolledtext 
from urllib.parse import urljoin #This is The URL LIBRARY WHICH WILL GO AND GIVE THE RESULTS
#This is the Function who will do this for me ....
def get_hyperlinks(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a.get('href') for a in soup.find_all('a', href=True)]
        return links
    except Exception as e:
        return [f"Error: {e}"]
#NOW this function will extract and showcase the links in GUI format so YOu just tap and go it's kinda visa

def extract_hyperlinks():
    url = entry.get()
    hyperlinks = get_hyperlinks(url)
    text.delete(1.0, tk.END)  # Clear previous content
    for link in hyperlinks:
        text.insert(tk.END, f"{link}\n")

# THis is through I can have a GUI Format of our code 
root = tk.Tk()
root.title("Psychomong's Web Scanner")

# Styling
root.geometry("600x400")
root.configure(bg="#303030")

# Entry for URL input
entry_label = tk.Label(root, text="Enter Website URL:", bg="#303030", fg="white")
entry_label.pack(pady=10)
entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(pady=10)

# Button to trigger hyperlink extraction
extract_button = tk.Button(root, text="Scan Website", command=extract_hyperlinks, bg="#4CAF50", fg="white", font=("Arial", 14))
extract_button.pack(pady=20)

# ScrolledText to display hyperlinks
text = scrolledtext.ScrolledText(root, width=80, height=10, font=("Arial", 12), wrap=tk.WORD)
text.pack(pady=20)

# Start the GUI main loop
root.mainloop()
