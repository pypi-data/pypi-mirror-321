# DiaModality - The Modality Diagram

Simple tool to plot vector modality diagram  

[![pypi_version](https://img.shields.io/pypi/v/diamodality?label=PyPI&color=green)](https://pypi.org/project/diamodality)
[![GitHub Release](https://img.shields.io/github/v/release/konung-yaropolk/DiaModality?label=GitHub&color=green&link=https%3A%2F%2Fgithub.com%2Fkonung-yaropolk%2FDiaModality)](https://github.com/konung-yaropolk/DiaModality)
[![PyPI - License](https://img.shields.io/pypi/l/diamodality)](https://pypi.org/project/diamodality)
[![Python](https://img.shields.io/badge/Python-v3.10%5E-green?logo=python)](https://pypi.org/project/diamodality)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/DiaModality?label=PyPI%20stats&color=blue)](https://pypi.org/project/diamodality)



### To install package run the command:
```bash
pip install diamodality
```


### Example use case:
See the /demo directory on Git repo or  
create and run the following two files:  
*(file names don't matter)*

---
``generate_sample_data.py``:
```python
import csv
import random
import os

num_rows = 1500
output_file = 'modality_data.csv'

# locate working directory
script_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(script_dir, output_file)

# Open a new CSV file to write the data
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Generate the data
    signal_treshold = 1.5
    for _ in range(num_rows):

        # generate data columns:
        col1 = random.uniform(0, 2.7)
        col2 = random.uniform(0, 3.3)
        col3 = random.uniform(0, 7.3)

        # generate binarization columns:
        col4 = 1 if col1 > signal_treshold else ''
        col5 = 1 if col2 > signal_treshold else ''
        col6 = 1 if col3 > signal_treshold else ''

        writer.writerow([col1, col2, col3, col4, col5, col6])

```


---
``plot_sample_data.py``:
```python
import DiaModality.ModalityPlot as plt
import scsv as csv
import os

# input files:
files = ['modality_data.csv']

# Get full path
script_dir = os.path.dirname(os.path.realpath(__file__))

for file in files:

    # Get full path of input files
    file_path = os.path.join(script_dir, file)

    # Parse data from csv file
    new_csv = csv.OpenFile(file_path)
    data, binarization = new_csv.GetRows(3, 3)

    # Make figure:
    plot = plt.ModalityPlot(
        data,
        binarization,
        modalities=['Set 1', 'Set 2', 'Set 3'],
        angles=[210, 90, 330],
        labels=False,
        scalecircle=0.5,           # Scale circle radius
        scalecircle_linestyle=':',
        scalecircle_linewidth=0.75,
        marker='',                 # vector endpoints marker
        linestyle='-',
        linewidth=0.5,
        alpha=0.5,
        same_scale=False,          # Draw all the subplots in the same scale
        full_center=True,          # Draw all vectors in the central subplot,
                                   # else draw trimodal vectors only
        whole_sum=True,            # Calculate all three modality vectors despite binarization
        figsize=(10, 10),
        dpi=100,
        title='Modality Diagram Example',
        colors=(
            'tab:green',   # Set 1 color
            'navy',        # Set 2 color
            'tab:red',     # Set 3 color
            '#1E88E5',     # Sets 1 & 2 intersection color
            '#FF9933',     # Sets 1 & 3 intersection color
            '#9900FF',     # Sets 2 & 3 intersection color
            'black',       # All sets   intersection color
        ),      
    )

    plot.save(file_path, type='png', transparent=False)
    plot.show()
```

Source page: 
https://github.com/konung-yaropolk/DiaModality


![modality_data csv](https://github.com/user-attachments/assets/eb77b4d7-281f-45b0-a5ce-4c2442fc9a75)
