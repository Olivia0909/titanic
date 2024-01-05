import streamlit as st
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.linear_model import LogisticRegression


def predict_survival(pclass, age, fare, alone, sex, embarked):
  
    print("pclass", pclass)
    if pclass == "First class":
        pclass = 1
    elif pclass == "Second class":
        pclass = 2
    else:
        pclass = 3
    print("pclass: ", pclass)

    if age <= 16:
        age = 0
    elif age > 16 and age <= 32:
        age = 1
    elif age > 32 and age <= 48:
        age = 2
    elif age > 48 and age <= 64:
        age = 3
    else:
        age = 4

    if fare <= 8:
        fare = 0
    elif fare > 8 and fare <= 14:
        fare = 1
    elif fare > 14 and fare <= 31:
        fare = 2
    else:
        fare = 3
    
    if alone == True:
        alone = 0
    else:
        alone = 1
    
    if sex == "Male":
        sex = 0
    elif sex == "Female":
        sex = 1
    
    if embarked == "Southhampton":
        embarked = 0
    elif embarked == "Queenstown":
        embarked = 1
    elif embarked == "Cherbourg":
        embarked = 2
    
    df1 = pd.read_csv("data.csv")
    df1 = df1.drop(df1.columns[0], axis=1)
    
    X = df1.drop("Survived", axis=1)
    y = df1['Survived']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 101)
    lr = LogisticRegression()
    lr.fit(X_train, y_train)
    result = lr.predict([[pclass, embarked, age, sex, fare, alone]])
    
    if result[0] == 0:
        st.text("Sorry, you are unlucky and you did not survive")
    elif result[0] == 1:
        st.text("Congrats, you survived")

def main():
    st.title("Prediction of Titanic Survival")
    st.text("Please fill in following information about survivor")

    pclass = st.selectbox(
        'Selected your class',
        ('First class', 'Second class', 'Third class'))

    age = st.slider('How old are you?', 0, 80, 40)

    fare = st.number_input("Enter your fare cost", min_value=0, max_value=512, value=50, step=1)

    alone = st.toggle('Are you alone')

    if alone:
        st.write('You are alone!')
    else:
        st.write('You are not alone!')

    sex = st.selectbox(
        'Selected your gender',
        ('Female', 'Male'))


    embarked = st.radio(
        "Where did you embark from",
    ("Southhampton", "Queenstown", "Cherbourg"))
    st.button("Submit", type="primary", on_click=predict_survival(pclass, age, fare, alone, sex, embarked))
    


main()

