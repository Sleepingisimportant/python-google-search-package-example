from googlesearch import search
import pandas as pd
from datetime import datetime


query = "pokemon pokeball" # The item you are searching for
countResult = 60 # Count of google search result snippet that includes the query name
today_str = datetime.today().strftime('%Y%m%d') #for the naming of the output file

results = []

# Perform a Google search using the specified query and retrieve the predefined number of results
for url in search(query, num_results=countResult): 
    results.append({query+" / "+today_str: url})  #Append each result to the list as a dictionary with the query and date as the key, and the URL as the value
    print(url)
    
# Convert the list of search results into a pandas DataFrame and save DF to csv file
df = pd.DataFrame(results)
output_file = 'search_'+query+"_"+today_str+'.csv'
df.to_csv(output_file, index=False)


