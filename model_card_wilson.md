# Model Card
 Udacity course to Learn how to deploy a pipeline with FastAPI
## Model Details
Model Name: Census Income Classifier
Model Type: Random Forrest
Metric model from sklearn learn
DVC by github/workflow
Deployment: RESTful API using FastAPI
## Intended Use
>Can be used to determine relation between subject and income
>Can be used to identify commonalities between high earners and lower earners. 
> Educational purposes. To learn how to deploy ML pipeline via Fast Api
## Training Data
> UCI Census INCOME, large data set with over 48,000 records and covering a many attributes (includging:age,workclass,fnlgt,education,education-num,marital-status,occupation,relationship,race,sex,capital-gain,capital-loss,hours-per-week,native-country,salary)
## Evaluation Data
> 20% of data used 6400 rows, predict whether income exceeds $50K/yr based on census data. Preprocessing pipeline was with OneHotEncoeder. OneHotEncoeder is used to convert categorical features into a one-hot numeric array. This helps with machine learning algorithms. The Fit/Transform feature of OneHotEncoeder. This method learns all unique categories from training data, which ensures that the same encoding scheme can be applied consistently. . (scikit-learn.org)
## Metrics
> Model Trained on fbeta, Precision, and Recall,       
> fbeta: .6862, Precision: .7468, Recall: .6346, 
Why These Tests:
fbeta is a performance metric for evaluating binary classification model based on predictions
Precision asks: Of all predicted positives, how many were actually positive?
Recall asks: Of all actual positives, how many did the model find? (https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fbeta_score.html)
## Ethical Considerations
>This data set was not treated for bias and should not be treated as bias free without further investigation. 
## Caveats and Recommendations
Data is older so this data is good for creating models and sharpening concepts. Care should be taken if newer data is not accumulated. 
For learning purposes only. This is a large dataset with potential for significant insight into the population studied. 

