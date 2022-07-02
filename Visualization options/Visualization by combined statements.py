import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# % matplotlib inline


# Load Json file of the combined statements extracted keywords 
keywords_all_statements = json.load (open('combined_statements_keywords.json'))

# Convert Json format into a string for wordcloud
text=(" ").join(keywords_all_statements)

#Wordcloud visualization of combined statements
wordcloud = WordCloud(max_words=100,mode="RGBA",background_color="white").generate(text)

#Display the generated image:
plt.figure( figsize=(10,6), facecolor='w')    
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig("C:/NLP project/projectconfigs/images/statements.png", format="png")
plt.show()

