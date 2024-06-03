# Minimum-Volume-Tetrahedron-Finder

## Description
This script reads points data from files, validates tetrahedrons, and finds the smallest tetrahedron. It uses multiprocessing for efficient computation.

## Preparation

### Input Data
Ensure you have two files named `points_small.txt` and `points_large.txt` in the same directory as your Python file. These files should contain the points data in the format specified in the `read_points` function.

### Dependencies
Make sure you have Python installed on your system. Additionally, ensure you have the `multiprocessing` module installed. If you're using a virtual environment, activate it and then install the module via pip:

```bash
pip install multiprocessing
```
## Running the Script

1. Open a terminal or command prompt.
2. Navigate to the directory where your Python script (`tetrahedron.py`) is located.
3. Run the script with the following command:

```bash
python tetrahedron.py
```
