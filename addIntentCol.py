import pandas as pd
csv_input = pd.read_csv('datasets/AskAboutRegisterDate.csv')
csv_input['Intent'] = 'AskAboutRegisterDate'
csv_input.to_csv('datasets/AskAboutRegisterDate.csv', index=False)