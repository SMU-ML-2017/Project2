import math

# Data Structures
import numpy as np
import pandas as pd

# Statistics and Processing
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline

# Natural Language Processing
import nltk
from nltk.corpus import stopwords

# Visualization
import seaborn as sns
from wordcloud import WordCloud
from PIL import Image

import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

#Make matplotlib pretty
matplotlib.rcParams.update({'figure.figsize': (15, 9)})
matplotlib.rcParams.update({'font.size': 16})
matplotlib.rcParams.update({'axes.labelsize': 20})
matplotlib.rcParams.update({'xtick.labelsize': 12})
matplotlib.rcParams.update({'ytick.labelsize': 12})
matplotlib.rcParams.update({'font.family': 'Helvetica, Arial, sans-serif'})

# Place this in the notebook:
# %config InlineBackend.figure_format = 'retina'

