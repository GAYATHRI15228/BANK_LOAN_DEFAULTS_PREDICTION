import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder


def prediction(id,Loan_amount,Purpose_of_loan,Annual_income,FICO_score,Mortgages,Employment_status,Debt_to_income_ratio,Terms,House_ownership):
    df=pd.read_csv("loan_data.csv")
    df['Loan_status'] = df['Loan_status'].replace(to_replace='ND', value=0.0)
    df['Loan_status'] = df['Loan_status'].replace(to_replace='D', value=1.0)

    notdefault_df =df[df['Loan_status']==0.0][0:200]
    default =df[df['Loan_status']==1.0][0:200]
    axes = notdefault_df.plot(kind = 'scatter',x='Loan_amount',y= 'Annual_income', color='blue',label='Not default')
    default.plot(kind = 'scatter',x='Loan_amount',y= 'Annual_income', color='red',label='Default', ax=axes)

    df= df[pd.to_numeric(df['id'],errors='coerce').notnull()]

    df['id'].astype('float')

    feature_df = ['id','Loan_amount','Purpose_of_loan','Annual_income','FICO_score','Mortgages','Employment_status','Debt_to_income_ratio','Terms','House_ownership','Loan_status']

    #Independent var
    x = np.asarray(feature_df)
#dependent var
    y = np.asarray(df['Loan_status'])


    x = df.drop("Loan_status",axis=1)
    y = df["Loan_status"]
    x= x.values
    y= y.values
    train_x = x[:80]
    train_y = y[:80]
    test_x = x[80:]
    test_y = y[80:]

    label_encoder = LabelEncoder()
    X[:, 2] = label_encoder.fit_transform(X[:, 2])  # Purpose_of_loan
    X[:, 5] = label_encoder.fit_transform(X[:, 5])  # Mortgages
    X[:, 6] = label_encoder.fit_transform(X[:, 6])  # Employment_status
    X[:, 9] = label_encoder.fit_transform(X[:, 9])  # House_ownership

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=4)

    from sklearn.ensemble import RandomForestClassifier
    random_forest_classifier = RandomForestClassifier()
    random_forest_classifier.fit(x_train,y_train)

    random_forest_classifier.score(x_test,y_test)

    
    with open("loan_default.py", "r") as file:
        file_contents = file.read()

# Save the contents as a pkl file
    with open("model.pkl", "wb") as file:
        pickle.dump(file_contents, file)

    hp =[[id,Loan_amount,Purpose_of_loan,Annual_income,FICO_score,Mortgages,Employment_status,Debt_to_income_ratio,Terms,House_ownership]]

    predicts = model.predict(hp)
    if predicts == [0.]:
        predicts="The Loan Applicant is Not a defaulter"
    elif predicts == [1.]:
        predicts = "The Loan Applicant is a defaulter"
    return predicts