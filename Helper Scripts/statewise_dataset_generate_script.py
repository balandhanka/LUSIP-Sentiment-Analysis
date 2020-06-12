states_list = [
  'Andhra Pradesh',
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


for state in states_list:
  big_df = pd.read_csv(f"data/{state}_11_polarity.csv")
  big_df['Month'] = ['11',]*big_df.shape[0]

  for month in months_list:
    file_name = f"data/{state}_{month}_polarity.csv"

    df = pd.read_csv(file_name)
    df['Month'] = [month]*df.shape[0]

    big_df = pd.concat([big_df, df], ignore_index=True)
  
  big_df.to_csv(f"output/{state}_combined.csv", index=False)
