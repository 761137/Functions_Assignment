def process_scores(students):
   result={}
   for name,marks in students.items():
     avg=sum(marks)/len(marks)
     result[name]=round(avg,2)
   return result
                     


def classify_grades(averages):
    grade={}
    for name,avg in averages.items():
        if avg>=90:
           grades= 'A';
        elif avg>=75 and avg <=89:
           grades= 'B';
        elif avg>=60 and avg<=74:
           grades='C'
        elif avg<60:
           grades='F'
        grade[name]=(avg,grades)
    return grade;

def generate_report(classified, passing_avg=70):
    print("===== Student Grade Report =====")
    tot_count=0
    pass_count=0
    fail_count=0
    
    for name,(avg,grade) in classified.items():
        if avg>=passing_avg:
            status="PASS"
            pass_count+=1
        else:
            status="FAIL"
            fail_count+=1
        print(f"{name}     | Avg: {avg}   | Grade: {grade} | Status={status}")
        # print(f"{name}|Avg:{avg}|Grade:{grade}Avg:{avg}|Grade:{grade}|Status={status}")
        tot_count+=1
    print("================================")
    print("Total Students:",tot_count)
    print("Passed:",pass_count)
    print("Failed:",fail_count)
    
Student_list={"Alice":[75,82,90,85],"Bob":[85,77,72,75],"Clara":[42,55,59]}
Results=process_scores(Student_list)
Final_Grade=classify_grades(Results)
generate_report(Final_Grade)
