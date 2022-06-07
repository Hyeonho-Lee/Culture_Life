import json
import pandas as pd

progress_csv = '../csv/progress_event_busan.csv'
new_csv = '../csv/new_event_busan.csv'
end_csv = '../csv/end_event_busan.csv'

progress_path = '../static/result/progress_event_busan.json'
new_path = '../static/result/new_event_busan.json'
end_path = '../static/result/end_event_busan.json'


def csv_to_json(csv, path):
    
    csv = pd.read_csv(csv, encoding='utf-8', index_col=0)
    csv.to_json(path)
    
    with open(path, 'r') as file:
        text = json.load(file, strict=False)
    
    with open(path, 'w') as file:
        json.dump(text, file, indent = 4, ensure_ascii=False)

csv_to_json(progress_csv, progress_path)
csv_to_json(new_csv, new_path)
csv_to_json(end_csv, end_path)