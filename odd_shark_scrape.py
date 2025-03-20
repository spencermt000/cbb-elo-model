import pandas as pd
import requests
from bs4 import BeautifulSoup
import html5lib

# Read the raw data
raw = pd.read_csv("oddsshark_scrape.csv")
seasons = [2025]

# Loop through each season
for season in seasons:
    all_data = []
    
    # Loop through each team in the DataFrame
    for index, row in raw.iterrows():
        team = row['team']
        team_id = row['id']
        
        # Build the URL
        url = f"https://www.oddsshark.com/stats/gamelog/basketball/ncaab/{team_id}"
        if season != 2025:
            url += f"?season={season}"
        
        print(f"Scraping {team} for season {season}\n")
        
        try:
            # Make the request
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Find the table
            table = soup.find("table")
            df = pd.read_html(str(table))[0]
            
            # Add team and season info
            df['team'] = team
            df['team_id'] = team_id
            df['season'] = season
            
            # Append to list
            all_data.append(df)
        
        except Exception as e:
            print(f"Failed to scrape {team} for {season}: {e}")

    # Combine all data for the season
    if all_data:
        season_df = pd.concat(all_data, ignore_index=True)
        season_df.to_csv(f"odds_{season}.csv", index=False)
        print(f"Saved odds_{season}.csv")
    else:
        print(f"No data scraped for {season}")