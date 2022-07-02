import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# % matplotlib inline

#Open json file
data = json.load (open('keywords by time.json'))

#creating two dictionaries 
dict1 = data['time_updated']
dict2= data['Extracted Keywords']

#Creating a new dictionary and storing keys and values
newdict = dict(zip(dict1.values(), dict2.values()))
 


while True:
    user_input = input("Enter time in HH:MM:SS format : ")
    if user_input in newdict:
           text= newdict.get(user_input)
           print ("keywords for the entered time:\n",text)
           wordcloud = WordCloud(max_words=100,mode="RGBA",background_color="white").generate(text)
           plt.figure( figsize=(10,6), facecolor='w')    
           plt.imshow(wordcloud, interpolation='bilinear')
           plt.title('Time: {}'.format(user_input))
           plt.axis("off")
           plt.tight_layout(pad=0)
           plt.savefig("C:/NLP project/projectconfigs/images/keywords by time.png", format="png")
           plt.show()
           if input('Press y to continue or Press anything to finish:\n') != 'y':
            break
    else:
          print ("The entered time: {} doesn't exist, Enter valid time in HH:MM:SS format:".format(user_input))
