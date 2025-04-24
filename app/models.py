from django.db import models

# Create your models here.

class login(models.Model):
    log_id=models.AutoField(primary_key=True)   
    user_name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    usertype=models.CharField(max_length=20)

class subject(models.Model):
    subject_id=models.AutoField(primary_key=True)
    subject=models.CharField(max_length=20)

class course(models.Model):
    course_id=models.AutoField(primary_key=True)
    course=models.CharField(max_length=100)

class teacher(models.Model):
    teacher_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    subject=models.ForeignKey(subject,on_delete=models.CASCADE)
    course=models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    
class notification(models.Model):
    notifi_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    date=models.CharField(max_length=50)
    status=models.CharField(max_length=50)

class complaint(models.Model):
    complaint_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE,null=True)
    complaint=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)
    date=models.CharField(max_length=20)

class student(models.Model):
    student_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    teacher=models.ForeignKey(teacher,on_delete=models.CASCADE)
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    sem=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    email=models.CharField(max_length=50)

class additional(models.Model):
    ai_id=models.AutoField(primary_key=True)
    student=models.ForeignKey(student,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    date=models.CharField(max_length=20)

class note(models.Model):
    note_id=models.AutoField(primary_key=True)
    subject=models.ForeignKey(subject,on_delete=models.CASCADE)
    file=models.CharField(max_length=100)
    date=models.CharField(max_length=100)    

class assessment_set(models.Model):
    set_id=models.AutoField(primary_key=True)
    teacher=models.ForeignKey(teacher,on_delete=models.CASCADE)
    set_name=models.CharField(max_length=100)
    question_count=models.CharField(max_length=100)   

class assessment(models.Model):
    assessment_id=models.AutoField(primary_key=True)
    set=models.ForeignKey(assessment_set,on_delete=models.CASCADE)
    student=models.ForeignKey(student,on_delete=models.CASCADE)
    score=models.CharField(max_length=50)
    date=models.CharField(max_length=50)

class pass_request(models.Model):
    req_id=models.AutoField(primary_key=True)
    student=models.ForeignKey(student,on_delete=models.CASCADE)
    pass_type=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    start_time=models.CharField(max_length=50)
    end_time=models.CharField(max_length=50)
    status=models.CharField(max_length=20)

class parent(models.Model):
    parent_id=models.AutoField(primary_key=True)
    student=models.ForeignKey(student,on_delete=models.CASCADE)
    teacher=models.ForeignKey(teacher,on_delete=models.CASCADE)
    login=models.ForeignKey(login,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=500)

class assignment(models.Model):
    assign_id=models.AutoField(primary_key=True)
    teacher=models.ForeignKey(teacher,on_delete=models.CASCADE,null=True)
    subject=models.ForeignKey(subject,on_delete=models.CASCADE,null=True)
    file=models.CharField(max_length=100)
    date=models.CharField(max_length=100) 
    deadline=models.CharField(max_length=50)


# class upload(models.Model):
#     upload_id=models.AutoField(primary_key=True)
#     assignement=models.ForeignKey(assignment,on_delete=models.CASCADE,null=True)
#     student=models.ForeignKey(student,on_delete=models.CASCADE,null=True)
#     file=models.CharField(max_length=100)
#     date=models.CharField(max_length=100) 
 

class assign_submiss(models.Model):
    submiss_id=models.AutoField(primary_key=True)
    assign=models.ForeignKey(assignment,on_delete=models.CASCADE,null=True)
    student=models.ForeignKey(student,on_delete=models.CASCADE)
    file=models.CharField(max_length=100)
    submiss_date=models.CharField(max_length=100) 

class attendance(models.Model):
    attendance_id=models.AutoField(primary_key=True)
    course=models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    student=models.ForeignKey(student,on_delete=models.CASCADE,null=True)
    teacher=models.ForeignKey(teacher,on_delete=models.CASCADE,null=True)
    attendance=models.CharField(max_length=100)
    date=models.CharField(max_length=100) 


