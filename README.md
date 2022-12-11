# Analysis-of-gender-perception

In this project, we are trying to analyse how the perception of women has changed before and after they were given voting rights. Little bit about our data set, we extracted the data from Hansard Website - https://api.parliament.uk/historic-hansard/index.html
We used Beautiful soup to extract the data from hansard website. The data extraction files can be found in this repository. The extracted data can be found in the shared drive - https://drive.google.com/drive/folders/1DwsRwN3ecGvKzFDkh5uhV2RK_vxTz9lo?usp=sharing. The data is present in the 1800's data folder and mergedcsv files contain 1800's , 1900's, 2000's merged csvs. I cannot upload the data set folder to this repository as it is a very big file
To extract the data, 
1. First you need to extract the URL's. For that you need to run scraping_URL's code. 
2. In that code enter your desired start year and end year and it will extract all the URL's available in those years.
3. Download the URLS.csv file which was generated as an output of scraping_URL's file and upload the file to the folder where scraping_articles code file is available
4. In the scraping_articles code file, enter the same start and end year dates for which you extracted the URL's and run the script
5. You will get each year data as a CSV file which will consists of 5 columns.
The dataset consists of 5 columns - ID, Title, URL, Date, Text. We were able to extract 3.85 GB of data (80 years data). We are yet to extract the data (our IP was blocked, we will use VPN and extract the remaining data)
The file analysis_gp.py contains the code to get the male and female pronoun count, word2vec using Gensim. The file also contains the code to plot the male and female pronoun count for the existing data. 
Steps to get the male and female pronoun counts for all the years - 
1. Copy the data location and paste it in the path = "" line of the code
2. Run the cells
3. Prerun all the definitions available in the colab file
4. When running the 'for dir in dirs:' cell you can see the progress bar
5. Once it is done the male and female counts along with the year is stored in a dictionary where year is the key and male pronoun count and female pronoun count are the values
6. Once you get the male and female pronoun count you can proceed with your analysis (Check the screenshot for sample output of how the male and female pronoun counts are displayed)

<img width="602" alt="Screen Shot 2022-12-10 at 10 14 21 PM" src="https://user-images.githubusercontent.com/89367457/206884593-1f0eeb13-1571-4673-9ebf-f350f690347c.png">

Plot for male, female pronoun count vs year (The plot has some missing values. We decided to leave it empty as we donot have that year's data)

![download](https://user-images.githubusercontent.com/89367457/206884559-b12bb6cd-cf40-4561-b091-5fdcfe64edba.png)

The necessary packages to be installed are already present in the analysis_gp.py file. You can run the file by giving the data set location and you will the preliminary results.

To Generate the word cloud - download the sentiment_analysis.ipynb file. Open the file and read the CSV of the file for which you want to create a word cloud. Run all the cells, there are some preprocessing done on the data like checking for missing values and replacing the missing values with "No Text Available" (The file is fully documented so you will understand what and why you are doing that step)
Word Cloud created for the years 1925 to 1928 - 

![wordcloud](https://user-images.githubusercontent.com/89367457/206921710-11bbbef0-936c-489b-8877-2292cee3c53e.png)

