import pandas as pd
import os
import requests

df = pd.read_csv("query.csv")

print "Beginning"

top_depict = df['depicts'].value_counts().rename_axis('unique_depicts').reset_index(name='counts').head(10)

image_count_per_depict = int(top_depict['counts'].tail(1)) #set to minimum count of the depicts
home_dir_name = os.path.dirname(__file__)

for depict in top_depict['unique_depicts']:
    i = 1
    cat_df = df.loc[df['depicts'] == depict].head(image_count_per_depict)
    for index, row in cat_df.iterrows():
        url = row["image"]
        extension = url.rsplit('.', 1)[1]
        dir_name = os.path.join(home_dir_name, depict.rsplit('/',1)[1])
        file_name = os.path.join(dir_name, row["item"].rsplit('/',1)[1]) + "." + extension

        if not os.path.exists(dir_name):
            try:
                os.makedirs(dir_name)
            except OSError:
                print 'Error: Creating directory. ' +  dir_name

        if not os.path.isfile(file_name):
            try:
                r = requests.get(url, allow_redirects=True)
                open(file_name, 'wb').write(r.content)
            except OSError:
                print 'Error: Failed downloading ' +  url
        
        i = i + 1
        if i%50 == 0:
            print 'Progress : ' + depict + ' ===  ' + str(i) + '/' + str(image_count_per_depict)

print "Completed! YEY!!!!"
