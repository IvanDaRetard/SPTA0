import pandas as pd
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import smtplib
from email.message import EmailMessage
headers = ['Title','Price(Euro)']
df = pd.read_csv('T&p per hour.csv',names=headers)
print(df)

y = df['Price(Euro)']

plt.plot(y)

plt.savefig('day.jpg')