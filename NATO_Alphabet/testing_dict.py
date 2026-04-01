import pandas

student_dict = {
    "student" : ["Ayla", "Seva", "Elza"],
    "score" : [56, 76, 98]
}
student_data_frames = pandas.DataFrame(student_dict)

#print(student_data_frames)
for (index, row) in student_data_frames.iterrows():
    if row.student == "Ayla":
        print(row.score)
