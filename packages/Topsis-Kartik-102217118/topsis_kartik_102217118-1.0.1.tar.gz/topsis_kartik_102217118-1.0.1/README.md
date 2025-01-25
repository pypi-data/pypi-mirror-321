# Topsis-Kartik-102217118

# Topsis
# Technique for Order Preference by Similarity to Ideal Solution (TOPSIS)
In a general sense, it is the aspiration of human being to make "calculated" decision in a position of
multiple selection. In scientific terms, it is the intention to develop analytical and numerical methods that take into
account multiple alternatives with multiple criteria.
TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) is one of the numerical
methods of the multi-criteria decision making


## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the package
```
pip install Topsis-Kartik-102217118
```




## Usage
topsis module will take the data.csv file , weights , impacts , result.csv file:
1. data.csv file  - It is a dataset in CSV format which has atleast 3 columns(including the first column with names). It should only have numerical values. Any non-numerical value should be encoded before passing it to function.
2. weights - It is a string of comma(,) separated numbers which tell the weight of each criteria.
3. impacts - It is a string of comma(,) separated + and - sign showing the impact of criteria on decision making.
4. result.csv file - The output will be saved as a new CSV file, containing the original data, scores, and the final ranking for all alternatives.
The command line interface can be used as follows:
```
python 102217118.py data.csv "1,2,1" "+,+,-" result.csv
```
## Example

data.csv (Input):

|contestent|sur|tal|lah|pitch|sharpness|
|------|---|----|-------|-------|-----|
|a|4|18|6.5|35|15|
|b|6|14|4|38|19|
|c|6|12|5|42|20|
|d|8|26|7|50|25|
|e|3|14|6|40|14|


```
pip install Topsis-Kartik-102217118
python 102217118.py data.csv "1,1,1,1,1" "+,+,-,+,-" result.csv
```

Output: the result.csv file

|contestent|sur|tal|lah|pitch|sharpness|output|
|--|------|----|--------|--------|-------|-------|
|a|4|18|6.5|35|15|3|
|b|6|14|4|38|19|4|
|c|6|12|5|42|20|2|
|d|8|26|7|50|25|1|
|e|3|14|6|40|14|5|
