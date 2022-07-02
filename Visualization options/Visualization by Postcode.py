import json
from collections import defaultdict
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# % matplotlib inline

data = json.load (open('keywords by postcode.json'))

#creating two dictionaries 
dict1 = data['Postcode']
dict2= data['Extracted Keywords']

dict1= dict1.values()
dict2 = dict2.values()

#Creating a new dictionary and storing keys and values
d = defaultdict(list)
for key, value in zip(dict1, dict2):
    d[key].append(value)

newdict = dict(d)

while True:
    user_input = input("Enter Postcode : ")
    if user_input in newdict:
           text= newdict.get(user_input)
           text=' '.join(text)
           print ("keywords for the entered Postcode:\n",text)
           wordcloud = WordCloud(max_words=100,mode="RGBA",background_color="white").generate(text)
           plt.figure( figsize=(10,6), facecolor='w')    
           plt.imshow(wordcloud, interpolation='bilinear')
           plt.title('Postcode: {}'.format(user_input))
           plt.axis("off")
           plt.tight_layout(pad=0)
           plt.savefig("C:/NLP project/projectconfigs/images/keywords by postcode.png", format="png")
           plt.show()
           if input('Press y to continue or Press anything to finish:\n') != 'y':
            break
    else:
          print ("The entered Postcode {} doesn't exist, Enter Postcode in in valid format: ".format(user_input))
