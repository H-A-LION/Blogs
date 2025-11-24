#Create DataFrame from list
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data,columns=['student_id','age'])

#Get the Size of a DataFrame
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    [r,c]=players.shape
    return [r,c]



#Display the First Three Rows
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    #head
    #return employees.head(3)
    #With slicing.
    #return employees[0:3]
    #With .iloc
    return employees.iloc[:3, :]


#Select Data
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    #return students.loc[students["student_id"] == 101, ["name", "age"]]
    return students[students.student_id == 101][["name", "age"]]


#Create New Column
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus']=employees['salary']*2
    return employees


#Drop Duplicate Rows
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset='email',keep='first',inplace=True)
    return customers

#Drop Missing Data
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students.dropna(subset=['name'],inplace=True)
    return students


