# Project Overview

Project instructions:  
[42 Subject PDF](https://cdn.intra.42.fr/pdf/pdf/94019/en.subject.pdf?utm_source=chatgpt.com)

---

# Part 1 — Analysis of the Data Set

## Program
`Distribution.py`

## Description
The program takes a directory path as argument and recursively fetches images from its subdirectories.

It must then:
- extract and analyze the dataset from the images,
- generate pie charts and bar charts for each plant type,
- retrieve the directory names in order to properly label the chart columns.

## Expected Features
- Directory traversal
- Image dataset analysis
- Plant type classification
- Pie chart generation
- Bar chart generation
- Automatic labeling based on folder names

## Example
```bash
python Distribution.py ./dataset
