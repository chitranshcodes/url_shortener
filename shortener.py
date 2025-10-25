import pyshorteners
import pyperclip
s= pyshorteners.Shortener()

long_url=input("enter url:")
short_url=s.tinyurl.short(long_url)
pyperclip.copy(short_url)
print("copied to clipboard")