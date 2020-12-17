# p2d3
A Working Example to Transform Pandas DataFrame to JSON D3 Flare

## Usage

```python
# libraries
import json
import pandas as pd

# example data with three levels and a single value field
data = {'group1': ['Animal', 'Animal', 'Animal', 'Plant'],
        'group2': ['Mammal', 'Mammal', 'Fish', 'Tree'],
        'group3': ['Fox', 'Lion', 'Cod', 'Oak'],
        'value': [35000, 25000, 15000, 1500]}

df = pd.DataFrame.from_dict(data)

print(df)

""" The sample dataframe
group1  group2 group3  value
0  Animal  Mammal    Fox  35000
1  Animal  Mammal   Lion  25000
2  Animal    Fish    Cod  15000
3   Plant    Tree    Oak   1500
"""

from p2d3.pandas_to_d3 import PandastoD3

convert = PandastoD3()
convert.p2d3(df)

# returns a json file to /data/flare.json
```

## References
- Stackoverflow: https://stackoverflow.com/questions/59946453/creating-a-flare-json-to-be-used-in-d3-from-pandas-dataframe/65333978#65333978
- GitHub: https://github.com/andrewheekin/csv2flare.json/blob/master/csv2flare.json.py
- Source Data: https://opendata.dc.gov/datasets/311-city-service-requests-in-2020/data
