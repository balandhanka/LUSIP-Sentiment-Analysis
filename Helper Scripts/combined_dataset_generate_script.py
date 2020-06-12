states_list = [
  'Arunachal Pradesh',
  'Assam',
  'Bihar',
  'Chhattisgarh',
  'Goa',
  'Gujarat',
  'Haryana',
  'Himachal Pradesh',
  'Jammu & Kashmir',
  'Jharkhand',
  'Karnataka',
  'Kerala',
  'Madhya Pradesh',
  'Maharashtra',
  'Manipur',
  'Meghalaya',
  'Mizoram',
  'Nagaland',
  'Odisha',
  'Punjab',
  'Rajasthan',
  'Sikkim',
  'Tamil Nadu',
  'Telangana',
  'Tripura',
  'Uttarakhand',
  'Uttar Pradesh',
  'West Bengal',
]


months_list = ['12', '01', '02', '03', '04', '05']


import pandas as pd


big_df = pd.read_csv(f"data/Andhra Pradesh_combined.csv")
big_df['State'] = ['Andhra Pradesh',]*big_df.shape[0]

for state in states_list:
  file_name = f"data/{state}_combined.csv"

  df = pd.read_csv(file_name)
  df['State'] = [state]*df.shape[0]

  big_df = pd.concat([big_df, df], ignore_index=True)



big_df.to_csv(f"output/all_states_combined.csv", index=False)
