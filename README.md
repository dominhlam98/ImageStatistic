# ImageStatistic

Export CSV and Image according to brightness value

## Installation

Select your Python version ( Python 3.6.8)
--------------------------

Create enviroment
```bash
python -m virtualenv myenv
```

Activate enviroment
```bash
myenv\Scripts\activate.bat 
```

Install lib
```bash
pip install -r requirements.txt
```

## Usage

Download 3 Folder Image in GoogleDrive
Add 3 Folder to Folder's name "image" in this repo

Separate Image
```
python separate_image.py
```

Run this to extract all image in Separate Image
```
python export_total.py
```

or run this to export specify dir
```
python export.py
```

