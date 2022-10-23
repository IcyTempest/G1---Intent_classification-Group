import pandas as pd
csv_input = pd.read_csv('ListClub.csv')
csv_input['Intent'] = 'ListClub'
csv_input.to_csv('ListClub.csv', index=False)