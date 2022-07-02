# Keywords extraction ucas

This repository is for the source code to extract keywords from ucas personal statments (unstructured data). Unsupervised keywords extraction approach is implemented to extract keywords from ucas personal statements of applicants. 

In this project we have used:

•	Yet Another Keyword Extractor (Yake) for unsupervided keyword extraction.

•	Word Cloud for visual representation of extracted keywords. 


## Installation
### Requirements

•	Python 3.5 (or higher).

•	Yake keyword extractor. Check: https://github.com/LIAAD/yake

•	WordCloud: a word cloud generator library. Check:  [Windows 10 Python 3.5](https://github.com/amueller/word_cloud/issues/134),  [Visual code studio (Python)](https://github.com/amueller/word_cloud/issues/609)

   Packages needed to install as prerequisites:

•	Pip: package management system (it comes with Python)

•	Jupyter Notebook: an online editor for data visualization. (Optional)

•	Pandas: a library to prepare data for plotting.

•	Integrated development environment: Any (IDE) of your choice e.g. Visual studio code or Spyder.

•	Matplotlib: a plotting library.

•	Pillow.



## Setup


1. Install Yake :-

To install Yake using pip: 
```bash
pip install git+https://github.com/LIAAD/yake 
```

To upgrade using pip:

```bash
pip install git+https://github.com/LIAAD/yake –-upgrade
```

2. Install Word Cloud :-

If you are using pip:

```bash
pip install wordcloud
```
If you are using conda, you can install from the conda-forge channel:

```bash
conda install -c conda-forge wordcloud
```

3. Install Pillow:

```bash
pip install Pillow
```

## DEMO:

![Postcode and time](https://user-images.githubusercontent.com/90148389/163736119-9b9bb5ef-8027-4211-a951-4b0ea5d624ae.gif)

![Postcode](https://user-images.githubusercontent.com/90148389/163736120-d7748778-c8c9-4662-a4ec-56f663fe2814.gif)

## Word Cloud
The wordclouds are generated using the different visualization options.  


#### Wordcloud of combined statements:
![statements](https://user-images.githubusercontent.com/90148389/163731822-b880fad3-b0f4-4413-a739-d0903f3daeb9.png)


#### Wordcloud by time:
![keywords by time](https://user-images.githubusercontent.com/90148389/163731823-49104d4d-fefb-4f22-aa86-efe67cc2585b.png)


#### Wordcloud by Postcode:
![keywords by postcode](https://user-images.githubusercontent.com/90148389/163731827-7c081414-790a-4027-b2be-49692157ef6a.png)


#### Wordcloud by Postcode and Time:
![keywords by postcode and time](https://user-images.githubusercontent.com/90148389/163731830-fd73f2c6-b024-47e5-b484-6ba3fbd58e50.png)


## Contributors

•	Brett Drury

•	Sarmad Shaharyar Ahmad
