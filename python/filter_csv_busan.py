import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta

today = datetime.today().strftime('%Y-%m-%d')
tomorrow = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')

csv = pd.read_csv('../csv/busan_data.csv', encoding='utf-8', index_col=0)

csv = csv.sort_values(by='시작일자')

mask = (csv['시작일자'] <= today) & (csv['종료일자'] >= today)
progress_event = csv.loc[mask]
progress_event = progress_event.drop_duplicates()
progress_event.reset_index(inplace=True)
progress_event.drop(['index'], axis=1, inplace=True)

progress_event.to_csv('../csv/progress_event_busan.csv', mode='w')

mask = (csv['시작일자'] >= tomorrow)
new_event = csv.loc[mask]
new_event = new_event.drop_duplicates()
new_event.reset_index(inplace=True)
new_event.drop(['index'], axis=1, inplace=True)

new_event.to_csv('../csv/new_event_busan.csv', mode='w')

mask = (csv['종료일자'] <= yesterday)
end_event = csv.loc[mask]
end_event = end_event.drop_duplicates()
end_event.reset_index(inplace=True)
end_event.drop(['index'], axis=1, inplace=True)

end_event.to_csv('../csv/end_event_busan.csv', mode='w')

#print(new_event)
