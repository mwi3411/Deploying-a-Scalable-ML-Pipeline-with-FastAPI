# Model Card
> Udacity course to Learn how to deploy a pipeline with FastAPI
> For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
> ML Pipe line with Census Data set
> Used base code anf filled in details to form a functioning ML Pipeline and then deploy via FastAPI
>To take in data, split, train and output modles and depoloy using an api
>used random forest classifer as algorithm used
> fields in data age,workclass,fnlgt,education,education-num,marital-status,occupation,relationship,race,sex,capital-gain,capital-loss,hours-per-week,native-country,salary
## Intended Use
> Educational purposes. To learn how to deploy ML pipline via Fast Api
## Training Data
> UCI Census INCOME, 
## Evaluation Data
> 20% of data used, Predict whether income exceeds $50K/yr based on census data. Also known as Adult dataset.
## Metrics
> Model Trained on F1, Precision, and Recall.
> Precision: .7468, Precall: .6346, F1: .6862
## Ethical Considerations
>This data set was not treated for bias and should not be treated as bias free without further investigation. 
## Caveats and Recommendations
For learing purposes only. This is a large dataset with potential for signifcant insight into the population studied. 