import pandas as pd
df = pd.read_json ('article_body.json')
df.to_csv ('khoa_hoc.csv', index = None)