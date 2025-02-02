# dek2csv 

Import your MTGO library in Archidekt!
Why? Because MTGO client is poorly optimized and crashes/freezes all the time.

## Prerequisits
You need to install python3 and the requests package.
On Windows, python3 can be installed easily installed via the [MS Store](https://apps.microsoft.com/detail/9PNRBTZXMB4Z?hl=neutral&gl=DE&ocid=pdpshare).
To install the requests package, open a terminal ("cmd"-program), and type
```console
python3 -m pip install requests
```

## How to use
Export from MTGO:
- Go to your MTGO library.
- Select one card, then press CTRL+A to select all cards
- Right click and "Export selected"

Use the script to convert the exported file:
- Open terminal ("cmd"-program) and navigate to the file ("cd" command)
- Run the following command (you can choose your own name for export_file)
```console
python3 ./dek2csv.py 'Your Magic Online CollectionXXX.dek' export_file.csv 
```

## How it works
This is a python3 script that uses Scryfall's API to fetch the corresponding scryfall_id from the catid which MTGO uses.
