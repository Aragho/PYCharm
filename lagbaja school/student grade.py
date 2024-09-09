
nums_students= int(input("Enter number of students: "))
num_subjects = int(input("Enter number of subjects: "))
for index in range(1,nums_students+1):
    print(f"Entering score for Student: {index}")
    for count in range(1,num_subjects+1):
        subject_scores = int(input(f"Enter score for Subject: {count} : "))

        while subject_scores < 0 or subject_scores > 100:
            print("Score must be between 0 and 100.")
            subject_scores = int(input(f"Re-enter score for {num_subjects}: "))










