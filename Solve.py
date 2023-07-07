****************Problem.1a****************
import pandas as pd
from scipy.stats import skew, kurtosis
# Load the "cars" dataset
data = pd.read_csv(r"C:\Users\manoj\OneDrive\Desktop\360DigiTMG\Data Science\Assignment Question\
                   Graphical Representation\Day04_Assignment_Datasets\Day04_Assignment_Datasets\Q1_a.csv")
# Calculate skewness and kurtosis for the "speed" & "dist" column
speed_skew = skew(data['speed'])
speed_skew
speed_kurt = kurtosis(data['speed'])
speed_kurt
dist_skew = skew(data['dist'])
dist_skew
dist_kurt = kurtosis(data['dist'])
dist_kurt
# Calculate the mean, median, and mode for the "speed" column
speed_mean = data['speed'].mean()
speed_mean
speed_median = data['speed'].median()
speed_median
speed_mode = data['speed'].mode()
speed_mode
# Calculate the variance and standard deviation for the "speed" column
speed_var = data['speed'].var()
speed_var
speed_std = data['speed'].std()
speed_std
# Calculate the mean, median, and mode for the "dist" column
dist_mean = data['dist'].mean()
dist_mean
dist_median = data['dist'].median()
dist_median
dist_mode = data['dist'].mode()
dist_mode
# Calculate the variance and standard deviation for the "dist" column
dist_var = data['dist'].var()
dist_var
dist_std = data['dist'].std()
dist_std

****************Problem.1b****************
import pandas as pd
from scipy.stats import skew, kurtosis
# Load the "cars" dataset
data = pd.read_csv(r"C:\Users\manoj\OneDrive\Desktop\360DigiTMG\Data Science\Assignment Question\
                   Graphical Representation\Day04_Assignment_Datasets\Day04_Assignment_Datasets\Q2_b.csv")
# Calculate skewness and kurtosis for the "SP" & "WT" column
SP_skew = skew(data['SP'])
SP_skew
SP_kurt = kurtosis(data['SP'])
SP_kurt
WT_skew = skew(data['WT'])
WT_skew
WT_kurt = kurtosis(data['WT'])
WT_kurt
# Calculate the mean, median, and mode for the "SP" column
SP_mean = data['SP'].mean()
SP_mean
SP_median = data['SP'].median()
SP_median
SP_mode = data['SP'].mode()
SP_mode
# Calculate the variance and standard deviation for the "SP" column
SP_var = data['SP'].var()
SP_var
SP_std = data['SP'].std()
SP_std
# Calculate the mean, median, and mode for the "WT" column
WT_mean = data['WT'].mean()
WT_mean
WT_median = data['WT'].median()
WT_median
WT_mode = data['WT'].mode()
WT_mode
# Calculate the variance and standard deviation for the "WT" column
WT_var = data['WT'].var()
WT_var
WT_std = data['WT'].std()
WT_std

****************Problem.2****************

Solu: From histogram it is clear that the data is positively skewed.
	  From boxplot it is clear that there are some outliers and data is little 
      bit positive skewed.

****************Problem.3****************
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
x=pd.Series([34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56])
# Mean
x.mean()
# Median
x.median()
#Mode
x.mode() 
# Variance
x.var()
# Standard Deviation
x.std()
#Boxplot
plt.boxplot(x)

****************Problem.5****************

Solu: No skewness is present we have a perfect symmetrical distribution
    
****************Problem.6****************

Solu: Skewness and tail is towards Right
    
****************Problem.7****************

Solu: Skewness and tail is towards Left
    
****************Problem.8****************

Solu:  Positive kurtosis means the curve is more peaked and it is Leptokurtic
    
****************Problem.9****************

Solu: Negative Kurtosis means the curve will be flatter and broader
    
****************Problem.10****************

Solu: a.The above Boxplot is not normally distributed the median is towards the higher value
      b.The data is a skewed towards left. The whisker range of minimum value is greater than maximum
      c.The Inter Quantile Range = Q3 Upper quartile – Q1 Lower Quartile = 18 – 10 =8
      
****************Problem.11****************

Solu: First there are no outliers. Second both the box plot shares the same median that is approximately 
    in a range between 275 to 250 and they are normally distributed with zero to no skewness neither 
    at the minimum or maximum whisker range.

****************Problem.12****************

Solu: a. On observing the given boxplot, we can clearly observe that the upper quartile Q3 is 
    somewhere between 10 and 15 and close to 10. Hence, to give an approximate on seeing the box plot, 
    we can judge that the upper quartile Q3 is 12. Hence, upper quartile Q3 = 12

    Similarly, on observing the given boxplot, we can clearly observe that the lower quartile Q1 is 5.

    Therefore, according to the formula for the interquartile range:

    Inter-quartile range = Upper Quartile - Lower Quartile

    Inter-quartile range = Q3 - Q1

    Inter-quartile range = 12 - 5

    Inter-quartile range = 7

    The calculated IQR value of 7 is basically the measurement of the variability of X about the median 
    of X data. In simple words, the IQR of 7 tells us that the range of the middle half of X (data around 7) 
    is least influenced by the extreme values of X (like those around 0 and 20).

    b. On observing the given boxplot of Variable X, we can observe that the median of data of variable X 
    is closer to the lower quartile/left of the box and the whisker is shorter on the lower end of the box. 
    This implies that the distribution of variable X is positively skewed (skewed right).

    c. On reviewing the given boxplot, we can easily infer that the data point with value 25 is an outlier 
    because it is located outside the whiskers of the given boxplot. If this data point with value 25 is 
    found to be actually 2.5, it would not affect the given boxplot in any way because the new data point 
    with value 2.5 is again an outlier because it is again outside the boxplot. Hence, the boxplot would 
    remain unaffected and therefore, the new boxplot would be the same as the old one.

****************Problem.13****************

Solu: a. The mode of this dataset would lie between 4 to 8.
    The mode is the data value that occurs the most in a dataset. In the above figure, it is clearly seen 
    that the frequency is maximum somewhere between the values 4 to 8. Hence, the mode will definitely lie 
    between these values.

    b. The dataset is right skewed.
    Skewness refers to the distortion from a normal distribution in a dataset. It can be observed that the 
    dataset is shifted towards the right end with higher peaks than the average. Hence the dataset is right 
    skewed.

    c.Both the graphs are right skewed whose outliers and median are the same.
    The boxplot is also right skewed, hence when these are plotted for the same dataset, the graphs will be 
    right skewed. Outliers and median donnot change when depiction of a dataset is changed. Since here the same 
    dataset will be represented in boxplot and histogram, they both will be same.
