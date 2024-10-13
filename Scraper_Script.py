    
import pandas as pd 
import understatapi
import time
from datetime import datetime

class ShotDataScraper:
    def __init__(self):
        self.client = understatapi.UnderstatClient()

    def match_id_retrieval(self, league_list, season):
        match_id_list = []
        for league in league_list:
            league_matches = self.client.league(league=league).get_match_data(season=season)

            for match in league_matches:
                game_date = datetime.strptime(match['datetime'], '%Y-%m-%d %H:%M:%S')
                today = datetime.today()
                if game_date < today:
                    match_id_list.append({'id': match['id'], 'league': league})

        return match_id_list                

    def match_shots(self, match_id_list):
        match_dataframes = []
        for id in match_id_list:
            match_data = self.client.match(id['id']).get_shot_data()
            df_home = pd.DataFrame(match_data['h'])
            df_away = pd.DataFrame(match_data['a'])

            # Concatenate the home and away data for this match
            df_match = pd.concat([df_home, df_away], ignore_index=True)
            df_match['league'] = id['league']
            # Collect each match's DataFrame into the list
            match_dataframes.append(df_match)
                
        df_all_matches = pd.concat(match_dataframes, ignore_index=True)
        return df_all_matches

    def collect_shot_data(self):
        league_list = ['EPL', 'La_Liga', 'Bundesliga', 'Serie_A', 'Ligue_1']
        season = '2024'
        match_id_list = self.match_id_retrieval(league_list, season)
        df_shot_data = self.match_shots(match_id_list)

        return df_shot_data
    
    def clean_shot_data(self, df_shot_data):
        for col in ['X', 'Y', 'xG']:
            df_shot_data[col] = df_shot_data[col].astype(str).str.replace("'", "", regex=False)
            df_shot_data[col] = df_shot_data[col].astype(float)
        
        df_shot_data['X'] = df_shot_data['X']*120
        df_shot_data['Y'] = df_shot_data['Y']*80
        return df_shot_data

if __name__ == '__main__': 
    scraper = ShotDataScraper()
    df_shot_data = scraper.collect_shot_data()
    df_clean_shot_data = scraper.clean_shot_data(df_shot_data)
    df_clean_shot_data.to_csv('/Users/jordanpickles/Library/CloudStorage/OneDrive-Personal/Personal Data Projects/UnderstatData/shot_data_2024.csv', index=False)
    print(df_shot_data)