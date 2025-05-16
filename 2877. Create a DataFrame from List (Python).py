import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    student_id = []
    age = []

    for i in student_data:
        student_id.append(i[0])
        age.append(i[1])

    df = pd.DataFrame({"student_id":student_id, "age":age})

    return df   
