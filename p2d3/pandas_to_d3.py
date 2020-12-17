# libraries
import json
import pandas as pd
import os

class PandastoD3():
    def __init__(self):
        self.name = 'name'
        self.children = 'children'
        self.value = 'value'
        self.flare = {self.name: "flare", self.children: []}

        self.filename = 'flare.json'
        self.folder = 'data'
        self.path = os.environ['PWD'] + os.sep + os.sep.join([self.folder, self.filename])


    def p2d3(self, df):
        """
        :params A DataFrame df with four columns.
        The df contains three categorical-ish columns, in order of hierarchy.
        The fourth df column contains a number (float or integer).

        :return A json flare file suitable for plotting starburst chart in D3

        :reference
        - https://stackoverflow.com/questions/59946453/creating-a-flare-json-to-be-used-in-d3-from-pandas-dataframe/65333978#65333978
        - https://github.com/andrewheekin/csv2flare.json/blob/master/csv2flare.json.py
        
        """

        # iterate through dataframe values
        for row in df.values:
            level0 = row[0]
            level1 = row[1]
            level2 = row[2]
            value = row[3]

            d = {self.name: level0,
                  self.children: [{self.name: level1,
                                self.children: [{self.name: level2,
                                              self.value: value}]}]}
            # initialize key lists
            key0 = []
            key1 = []

            # iterate through first level node names
            for i in self.flare[self.children]:
                key0.append(i[self.name])

                # iterate through next level node names
                key1 = []
                for _, v in i.items():
                    if isinstance(v, list):
                        for x in v:
                            key1.append(x[self.name])

            # add the full path of data if the root is not in key0
            if level0 not in key0:
                d = {self.name: level0,
                      self.children: [{self.name: level1,
                                    self.children: [{self.name: level2,
                                                  self.value: value}]}]}
                self.flare[self.children].append(d)

            else:

                # if the root exists, then append to its children
                if level1 not in key1:

                    d = {self.name: level1,
                          self.children: [{self.name: level2,
                                           self.value: value}]}

                    self.flare[self.children][key0.index(level0)][self.children].append(d)

                else:

                    # if the root exists, then append to its children
                    d = {self.name: level2,
                          self.value: value}

                    self.flare[self.children][key0.index(level0)][self.children][key1.index(level1)][self.children].append(d)

        # save to some file

        with open(self.path, 'w') as outfile:
            json.dump(self.flare, outfile)
        print('Writing Flare to JSON')
        print(json.dumps(self.flare, indent=2))
