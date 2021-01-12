# EDFReader
Application for EDF data.

## What is EDF?🤔
EDF(European Data Format) is a data format for medical data (such as brain waves).

## What this app can do?
This application can export any data saved in EDF file to csv format.

## Requiears✅
- [pyedflib](https://pyedflib.readthedocs.io/en/latest/)
- [pandas](https://pandas.pydata.org/)
- python >= 3.6

## How to use
- Clone this repo
```
git clone https://github.com/nakarin0528/EDFReader.git
```
- Run main
```
python Main.py
```
- Load EDF file from `load` button
- Select data what you need (check left side check box)
- Select output directory
- Set start and end times (bottom)
- Push `convert` button

## Sample data
You can get sample data of EDF file from [official github repo](https://github.com/holgern/pyedflib/tree/master/pyedflib/tests/data).


## Comming soon...😉
- Data preview function (graphing)

