
columns = ['Pclass', 'Sex', 'Sibsp', 'Parch', 'Embarked',
       'Cabin', 'AgeGroup', 'Title', 'Fareband']



def process(df):
    ## gender mapping
    sex_mapping = {"male": 0, "female": 1}
    df['Sex'] = df['Sex'].map(sex_mapping)

    ## embarked mapping
    embarked_mapping = {"S": 1, "C": 2, "Q": 3}
    df['Embarked'] = df['Embarked'].map(embarked_mapping)

    ## Cabin to bool
    df["CabinBool"] = (df["Cabin"].notnull().astype('int'))
    df = df.drop(['Cabin'], axis=1)

    ## title mapping
    title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3,
                "Master": 4, "Royal": 5, "Other": 6}
    df['Title'] = df['Title'].map(title_mapping)


    ##  Agegroup mapping
    # map each Age value to a numerical value
    age_mapping =  {'Unknown':1,'Child(5-12)':2, 'Teenager(12-18)':3,'Student(18-24)':4,'Young Adult(24-35)':5, 'Adult(35-60)':6,'Senior(>60)':7}
    df['AgeGroup'] = df['AgeGroup'].map(age_mapping)

    # fareband mapping
    df = df.astype({"Pclass":"int","Sibsp":"int", "Parch":"int", "Fareband":"int"})

    return df

