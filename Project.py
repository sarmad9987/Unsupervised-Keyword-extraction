import json
import configparser
import os.path
import sys 
import pandas as pd
import os
import yake



config = configparser.ConfigParser()

#Reading the configuration file
config.read(r'C:/NLP project/projectconfigs/Project.config')

#print sections in configuration file    
print("The sections for configuration file:\n",config.sections())

# Get different sections of config file
print (config.get('Parameters','deduplication_thresold'))

#Print the location of data file from the configuration file
Data = config.get('file location', 'data')
print ("The location of the data file is:\n",Data)

#Check if the given location of data file exists if not exit
if os.path.isfile(Data):
    print ("The location of the Data File exists\n")
    #Reading the Csv file
    df = pd.read_csv(Data)
    

else:
    print ("The location of the Data File doesn't exist")
    sys.exit() 

df= df.rename(columns={"POSTCODE": "Postcode", "PERSONAL_STATEMENT": "PersonalStatements","APPLICATION_CREATED":"month/year","STATEMENT_UPDATED":"time_updated"})

#set time column to DateTime Format
df['month/year']= pd.to_datetime (df['month/year'],errors='coerce')

#set time_updated column to DateTime Format
df['time_updated'] =  pd.to_datetime(df['time_updated'],errors='coerce')


#Setting the columns according to config file
statements= df['PersonalStatements']
post_code=df['Postcode']
month_year = df['month/year'].dt.strftime('%m/%Y')
time= df['time_updated'].dt.time

#parameters for custom yake extractor
language = "en"
max_ngram_size = 3
deduplication_thresold = 0.9
deduplication_algo = 'seqm'
windowSize = 1
numOfKeywords = 100


#Function for keyword extraction from combined statements and create Json file to store results 
def keywords_yake(ucas_statements):
    
    #take keywords for each post & turn them into a text string "sentence"
    sentences=" "
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold, dedupFunc=deduplication_algo,top=numOfKeywords, windowsSize=windowSize, features=None)
    
    keywords = custom_kw_extractor.extract_keywords(ucas_statements)
    
    for word,number in keywords:
        sentences+= word + " "  
    keywords = dict(keywords)    
    jsonString1 =json.dumps ([sentences]) 
    jsonString2 =json.dumps(keywords,indent=2)    
    jsonfile1 = open("combined_statements_keywords.json", "w")
    jsonfile2 = open("combined_keywords_score.json", "w")
    JsonFile=jsonfile1.write(jsonString1)
    JsonFile=jsonfile2.write(jsonString2)
    jsonfile1.close()
    jsonfile2.close()
    return JsonFile


#Function for extracting keywords from every row of the statements column
def keywords_yake1 (sample_post):
    # take keywords for each post & turn them into a text string "sentence"
    simple_kwextractor = yake.KeywordExtractor()
    
    # create empty list to save our "sentences" to
    sentences = []

    for post in sample_post:
        post_keywords = simple_kwextractor.extract_keywords(post)

        sentence_output = ""
        for word, number in post_keywords:
            sentence_output += word + " "

        sentences.append(sentence_output)
        
    extracted_keywords = pd.DataFrame (sentences, columns = ['Extracted Keywords']) 
      
    return extracted_keywords




#Convert dataframes into separate Json files
def df_to_json (keywords_postcode_year,keywords_postcode,keywords_year,keywords_time):
    keywords_postcode_year= keywords_postcode_year.to_dict('dict')
    keywords_postcode= keywords_postcode.to_dict('dict')
    keywords_year= keywords_year.to_dict('dict')
    keywords_time= keywords_time.to_dict('dict')
    Jsonstring1= json.dumps(keywords_postcode_year,indent=4) 
    Jsonstring2= json.dumps(keywords_postcode,indent=4) 
    Jsonstring3= json.dumps(keywords_year,indent=4)
    Jsonstring4= json.dumps(keywords_time,indent=4, default=str)
    jsonFile1 = open('keywords by postcode and year.json', "w")
    jsonFile2 = open('keywords by postcode.json', "w")
    jsonFile3 = open('keywords by month and year.json', "w")
    jsonFile4 = open('keywords by time.json', "w")
    jsonfile= jsonFile1.write(Jsonstring1)
    jsonfile= jsonFile2.write(Jsonstring2)
    jsonfile= jsonFile3.write(Jsonstring3)
    jsonfile= jsonFile4.write(Jsonstring4)
    jsonFile1.close()
    jsonFile2.close()
    jsonFile3.close() 
    jsonFile4.close() 
    return jsonfile



#Function to convert one column to a string
def combine1col(text):
    text= ''.join(text)
    text = text.replace("\n","")
    return text

#Convert statements column into a string 
combined_statements = combine1col(statements)
#print (combined_statements)

#keywords_yake function on combined statements to extract keywords  
keywords_combined_statements= keywords_yake(combined_statements)
#print (keywords_combined_statements)

#keywords_yake1 function on statements column to extract keywords
Extracted_keywords= keywords_yake1(statements)
#print (Extracted_keywords)
 
# Concatenate post_code,month_year and Extracted_keywords columns and converting to dataframe
keywords_postcode= pd.concat([post_code, Extracted_keywords], join="outer",axis=1) 
keywords_month_year= pd.concat([month_year, Extracted_keywords], join="outer",axis=1)
keywords_postcode_month_year= pd.concat([post_code,month_year,Extracted_keywords], join="outer",axis=1)
keywords_time= pd.concat([time,Extracted_keywords], join="outer",axis=1)


# Converting the concatenated dataframes into Json files
df_to_json (keywords_postcode_month_year,keywords_postcode,keywords_month_year,keywords_time)
