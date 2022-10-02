import json
import os
import pandas as pd

def get_players_df(file_name, file_location):
    path = os.path.join(file_location, file_name)
    file = open(path)
    data = json.load(file)
    players_list = ''
    for k, v in data.items():
        if k == 'player':
            players_list = v
    df = pd.DataFrame(players_list)
    return df

def validate_no_of_foreign_players(no_of_foreign_players):
    players_df = get_players_df("TeamRCB.json", "test_data")
    filtered_df = players_df[players_df["country"] != "India"]
    no_of_players = filtered_df.shape[0]
    if no_of_players == no_of_foreign_players:
        print(f"PASS - Team contains only {no_of_foreign_players} foreign players.")
        return True
    else:
        print(f"FAIL - Team contains {no_of_players} foreign players, which is not equal to {no_of_foreign_players}.")
        return False

def validate_no_of_wicket_keepers(min_no_of_wkt_keeprs_req):
    players_df = get_players_df("TeamRCB.json", "test_data")
    filtered_df = players_df[players_df["role"] == "Wicket-keeper"]
    no_of_players = filtered_df.shape[0]
    if no_of_players >= min_no_of_wkt_keeprs_req:
        print(f"PASS - Team contains {no_of_players} wicket keeper(s), which is >= {min_no_of_wkt_keeprs_req}.")
        return True
    else:
        print(f"FAIL - Team contains {no_of_players} wicket keeper(s), which < {min_no_of_wkt_keeprs_req}.")
        return False

validate_no_of_foreign_players(4)
validate_no_of_wicket_keepers(1)
