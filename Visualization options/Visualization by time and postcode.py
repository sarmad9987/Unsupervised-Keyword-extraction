import json
from collections import defaultdict
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import ast

# % matplotlib inline
data = json.load (open('keywords by postcode.json'))
data1= json.load (open('keywords by time.json'))

#creating three dictionaries 
dict1 = data['Postcode']
dict2= data1['time_updated']
dict3=data['Extracted Keywords']

dict1= dict1.values()
dict2 = dict2.values()
dict3= dict3.values()

#Creating a new dictionary and storing keys and values
d = defaultdict(list)
for x, y, z in zip(dict1, dict2,dict3):
    d[x,y].append(z)

newdict = dict(d)

while True:
 user_input = ast.literal_eval(input("Enter postcode and time in ('postcode', 'time') format, e.g ('AP12', '13:46:09') : "))
 print (user_input)
 if user_input in newdict:
    print(f"Yes, user_input: '{user_input}' exists in dictionary\n")
    text= d.get(user_input)
    text=' '.join(text)
    print ("keywords for the entered postcode and time :\n",text)
    wordcloud = WordCloud(max_words=100,mode="RGBA",background_color="white").generate(text)
    plt.figure( figsize=(10,6), facecolor='w')    
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title('Postcode and Time: {}'.format(user_input))
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig("C:/NLP project/projectconfigs/images/keywords by postcode and time.png", format="png")
    plt.show()
    if input('Press y to continue or Press anything to finish:\n') != 'y':
     break       
else:
    print ("The entered postcode and time {} doesn't exist, Enter valid postcode and time format:".format(user_input))
