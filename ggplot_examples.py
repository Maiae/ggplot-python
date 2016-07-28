# We'll use the popular package called Pandas
# Install it with pip
import pip
    pip.main(['install', 'pandas'])

# Import it as 'pd'
import pandas as pd

# Create a dataframe
df=pd.DataFrame({"Animal":["dog","dolphin","chicken","ant","spider"],
                    "Legs":[4,0,2,6,8]})
df.head()


#####################################################################################
# ggplot examples

pip.main(['install', 'ggplot'])
#from ggplot import ggplot, aes, geom_bar, geom_line, stat_smooth
from ggplot import *

# bar chart
ggplot(df, aes(x="Animal", weight="Legs")) + geom_bar(fill='blue')


# line chart with smoothing
ggplot(aes(x='date', y='beef'), data=meat) + geom_line() + stat_smooth(colour='blue', span=0.2)


# scatter points
ggplot(diamonds, aes(x='carat', y='price', color='cut')) +\
    geom_point() +\
    scale_color_brewer(type='diverging', palette=4) +\
    xlab("Carats") + ylab("Price") + ggtitle("Diamonds")


# density and facets
ggplot(diamonds, aes(x='price', fill='cut')) +\
    geom_density(alpha=0.25) +\
    facet_wrap("clarity")


# histogram
import pandas as pd
import numpy as np

df3 = pd.DataFrame({
    "x": np.random.normal(0, 10, 1000),
    "y": np.random.normal(0, 10, 1000),
    "z": np.random.normal(0, 10, 1000)
})
df3 = pd.melt(df3)

ggplot(movies, aes(x='rating')) + \
    geom_histogram()

ggplot(aes(x='value', fill='variable', color='variable'), data=df3) + \
    geom_histogram(alpha=0.6)

