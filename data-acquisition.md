### Transfer Learning for Custom Datasets in the Small-Data Regime for Basement

# Milestone 2: Data Acquisition

For the basement I shortlisted following 10 product catogries that HD sells and are visible in their video :

 1. Pillar Wood/Steel 
 2. Television 
 3. Photo Frame
 4. Lamp and Lighting 
 5. Fireplace 
 6. Flooring 
 7. Sofa 
 8. Table 
 9. Installation Service 
 10. Window 

I used Google Custom Search API to get images for disered labels. Here is the code for a particular lable :
```python
# !pip install google-api-python-client

import  requests
from  PIL  import  Image
import  os

api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
from apiclient.discovery import build
resource = build("customsearch", 'v1', developerKey=api_key).cse()
items = []

search_string = "basement wire"
cx = "xxxxxxxxxxx"  #Custom Search Engine ID

for  rng  in  range(1,100,10):
	print(rng, end=' ')
	result = resource.list(q=search_string, cx='c027b0cbdfed84f0b', searchType = 'image',start=rng).execute()
	for  item  in  result['items']:
		items.append([item['title'], item['link']])

# Saving Images into folder
dir_name = './wire_data/'
if  dir_name  not  in  os.listdir():
	os.makedirs('dir_name')
	
i=0
for  item  in  items:
	img_url = item[1]
	response = requests.get(img_url)
	if  response.status_code:
		fp = open('./wire/+'+str(i)+'.png', 'wb')
		fp.write(response.content)
		fp.close()
	print(i,item[1])
	i+=1
```

