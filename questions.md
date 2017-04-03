### Machine Learning Toolbox Questions ###

** 1. What is the general trend in the curve? **

When we use more of the data for training, the accuracy on the test set increases.  It also appears that - even when 100% of the data is used for training - the accuracy never reaches above 25%.

** 2. Are there parts of the curve that appear to be noisier than others? Why? **

The areas of higher noise are most apparent in a high number of trials.  When the trials are above 1000, the most noise appears from 0 to 20 percent, when a lower percentage of training data is used.

![alt text](https://github.com/srbarden/ToolBox-MachineLearning/100trials.png "100 trials")

![alt text](https://github.com/srbarden/ToolBox-MachineLearning/1000trials.png "1000 trials")

** 3. How many trials do you need to get a smooth curve? **

After about 1000 trials, the curve begins to even out and has less noise.  Over 2000 trials will get you an almost completely "smooth" curve.

![alt text](https://github.com/srbarden/ToolBox-MachineLearning/2000trials.png "2000 trials")

** 4. Try different values for C (by changing Logistic Regression(C=10^-10)). What happens? If you want to know why this happens, see this Wikipedia page as well as the documentation for LogisticRegression in scikit-learn. **

I kept the number of trials at 2000.  Using a smaller value of C (10^-20) results in a strange curve. It has a constant accuracy of 10% until you get past 60% usage of training data.  Then, the curve increases rapidly.

![alt text](https://github.com/srbarden/ToolBox-MachineLearning/smallC.png "C=10^-20, 2000 trials")

Using a larger value of C (10^-1) results in a very pretty curve that has the shape of a logarithmic function. The accuracy reaches almost 90%.

![alt text](https://github.com/srbarden/ToolBox-MachineLearning/largeC.png "C=10^-1, 2000 trials")
