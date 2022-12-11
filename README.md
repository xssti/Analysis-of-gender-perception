# Analysis-of-gender-perception

In this project, we are trying to analyse how the perception of women has changed before and after they were given voting rights. Little bit about our data set, we extracted the data from Hansard Website - https://api.parliament.uk/historic-hansard/index.html
We used Beautiful soup to extract the data from hansard website. The data extraction files can be found in this repository. The extracted data can be found in the shared drive - https://drive.google.com/drive/folders/1DwsRwN3ecGvKzFDkh5uhV2RK_vxTz9lo?usp=sharing. The data is present in the 1800's data folder and mergedcsv files contain 1800's , 1900's, 2000's merged csvs.
The dataset consists of 5 columns - ID, Title, URL, Date, Text. We were able to extract 3.85 GB of data (80 years data). We are yet to extract the data (our IP was blocked, we will use VPN and extract the remaining data)
The file analysis_gp.py contains the code to get the male and female pronoun count, word2vec using Gensim. The file also contains the code to plot the male and female pronoun count for the existing data. 
Steps to get the male and female pronoun counts for all the years - 
1. Copy the data location and paste it in the path = "" line of the code
2. Run the cells
3. Prerun all the definitions available in the colab file
4. When running the 'for dir in dirs:' cell you can see the progress bar
5. Once it is done the male and female counts along with the year is stored in a dictionary where year is the key and male pronoun count and female pronoun count are the values
6. Once you get the male and female pronoun count you can proceed with your analysis

The necessary packages to be installed are already present in the analysis_gp.py file. You can run the file by giving the data set location and you will the preliminary results.
