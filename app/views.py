from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# from django.http import JsonResponse
from datetime import *
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse


# Create your views here.

def logi_n(request):
    return render(request,'index.html')    

def a_login(request):
    if request.method=='POST':
        name=request.POST['uname']
        password=request.POST['pswd']
        print("USERNAME:",name)
        print("PASSWORD:",password)
        try:
            res = login.objects.get(user_name=name,password=password)
            request.session['log']=res.pk
            if res.usertype == 'admin':
                return HttpResponse("<script>alert('Login Success');window.location='/admin'</script>")
            
            if res.usertype == 'teacher':
                teacher_data=teacher.objects.get(login=request.session['log'])
                request.session['teacher']=teacher_data.pk
                return HttpResponse("<script>alert('Login Success');window.location='/teacher'</script>")
            
            if res.usertype == 'student':
                student_data=student.objects.get(login=request.session['log'])
                request.session['student']=student_data.pk
                return HttpResponse("<script>alert('Login Success');window.location='/student'</script>")
            

            if res.usertype == 'parent':
                student_data=parent.objects.get(login=request.session['log'])
                request.session['parent']=student_data.pk
                return HttpResponse("<script>alert('Login Success');window.location='parent'</script>")
        except:
                return HttpResponse("<script>alert('Invalid Username or Password');window.location='/'</script>")
    return render(request,'admin/login.html')

def admin_home(request):
    subject_count = subject.objects.count()
    parent_count = parent.objects.count()
    teacher_count = teacher.objects.count()
    course_count = course.objects.count()
    student_count = student.objects.count()
    notification_count = notification.objects.count()

    
    
    return render(request,'admin/admin.html',{'subjects':subject_count,
                                              'parents':parent_count,
                                              'teachers':teacher_count,
                                              'courses':course_count,
                                              'students':student_count,
                                              'notifications':notification_count})

def manage_subject(request):
    if request.method == 'POST':
        subject_name=request.POST['subject']
        print(subject_name)
        result = subject(subject=subject_name)
        result.save()
        return HttpResponse("<script>alert('Subject Added');window.location='/manage_subject'</script>")
    result = subject.objects.all()
    return render(request,'admin/manage_subject.html',{'subs':result})

def subject_deletion(request,id):
    result = subject.objects.get(subject_id=id)
    result.delete()
    return HttpResponse("<script>alert('Subject Deleted');window.location='/manage_subject'</script>")

def replycomplaint(request,complaint_id):
    if request.method == 'POST':

        reply=request.POST['reply']
        print(reply)
        result = complaint.objects.get(complaint_id=complaint_id)
        result.reply=reply
        result.save()
        return HttpResponse("<script>alert('Reply Added');window.location='/view_complaints'</script>")
    
    return render(request,'teacher/replycomplaint.html')



def manage_course(request):
    if request.method == 'POST':
        course_name=request.POST['course']
        print(course_name)
        result = course(course=course_name)
        result.save()
        return HttpResponse("<script>alert('Course Added');window.location='/manage_course'</script>")
    result = course.objects.all()
    return render(request,'admin/manage_course.html',{'courses':result})



# from django.shortcuts import render
# from django.http import JsonResponse, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# import google.generativeai as genai
# import json
# import traceback

# # Configure the Gemini API with your key
# # genai.configure(api_key="AIzaSyAIcGw0rEzWnz0IOo-5TZrkfFiPuD7_uKM")
# genai.configure(api_key="AIzaSyAIcGw0rEzWnz0IOo-5TZrkfFiPuD7_uKM")



# def chat_bot(request):
#     """Render the chat bot interface."""
#     return render(request, "user/chat_bot.html")

# @csrf_exempt
# def chat_response(request):
#     """Handle chat requests and return AI responses."""
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)
#             user_message = data.get("message", "")
            
#             # Create model and generate response
#             # model = genai.GenerativeModel('gemini-1.5-pro')
#             model = genai.GenerativeModel('gemini-1.5-flash')
#             response = model.generate_content(user_message)
            
#             # Debug: Print response structure
#             print(f"Response type: {type(response)}")
#             print(f"Response attributes: {dir(response)}")
            
#             # Try to extract text
#             response_text = "No text found"
            
#             if hasattr(response, "text"):
#                 response_text = response.text
#                 print(f"Found response.text: {response_text[:100]}...")
                
#             # Return the text response
#             return JsonResponse({
#                 "response": response_text,
#                 "debug_info": {
#                     "response_type": str(type(response)),
#                     "has_text_attr": hasattr(response, "text"),
#                 }
#             })
#         except Exception as e:
#             trace = traceback.format_exc()
#             print(f"Error: {str(e)}")
#             print(f"Traceback: {trace}")
#             return JsonResponse({
#                 "error": str(e), 
#                 "traceback": trace
#             }, status=500)
    
#     return JsonResponse({"error": "Invalid request method"}, status=400)


def course_deletion(request,id):
    result = course.objects.get(course_id=id)
    result.delete()
    return HttpResponse("<script>alert('Course Deleted');window.location='/manage_course'</script>")


def teacher_registration(request):
    res=subject.objects.all()
    teachers = teacher.objects.all()
    cours = course.objects.all()
    if request.method=='POST':
        fullname=request.POST['name']
        place=request.POST['place']
        phone=request.POST['phone']
        email=request.POST['email']
        username=request.POST['uname']
        password=request.POST['pswd']
        subject_id=request.POST['subject_id']
        course_id=request.POST['course_id']
        cours=course.objects.get(pk=course_id)
        subs=subject.objects.get(pk=subject_id)
        print(subs.pk,"+++++++++++++")
        res1=login(user_name=username,password=password,usertype='teacher')
        res1.save() 
        res2=teacher(name=fullname,place=place,phone=phone,email=email,login=res1,subject=subs,course=cours)
        res2.save()
        return HttpResponse("<script>alert('Teacher Registered');window.location='/manage_teacher'</script>")
    return render(request,'admin/teachreg.html',{'subs':res,'teachers': teachers,'course':cours})

def teacher_deletion(request,id):
    result = teacher.objects.get(teacher_id=id)
    result.delete()
    return HttpResponse("<script>alert('Teacher Dismissed');window.location='/manage_teacher'</script>")

def edit_teacher(request,id):
    result1 = teacher.objects.get(teacher_id=id)
    result2 = subject.objects.all()
    if request.method == 'POST':
        result1.name = request.POST['name']
        result1.place = request.POST['place']
        result1.phone = request.POST['phone']
        result1.email = request.POST['email']
        subject_id=request.POST['subject']
        subs=subject.objects.get(pk=subject_id)
        result1.subject=subs
        result1.save()
        return HttpResponse("<script>alert('Teacher updated');window.location='/manage_teacher'</script>")
    return render(request,'admin/edit_teacher.html',{'tchrs':result1,'subs':result2})


def notifications(request):
    res12 = notification.objects.all()
    if request.method=='POST':
      title=request.POST['title']
      des=request.POST['description']
      date=request.POST['date']
      status=request.POST['status']
      res2=notification(title=title,description=des,date=date,status=status)
      res2.save()
      return HttpResponse("<script>alert('Notification Added');window.location='/send_notification'</script>")
    return render(request,'admin/notifications.html',{'notifications':res12})

def noti_update(request,id):
      result2 = notification.objects.get(notifi_id=id)
      if request.method=='POST':
        result2.status=request.POST['status']
        result2.save()
        return HttpResponse("<script>alert('Status Updated');window.location='/send_notification'</script>")
      return render(request,'admin/noti_update.html')

def viewteachers(request):
    teachers = teacher.objects.all()
    return render(request,'admin/view_teachers.html',{'teachers':teachers})

def viewstudents(request):
    students = student.objects.all()
    return render(request,'admin/view_students.html',{'students':students})

def viewparents(request):
    parents = parent.objects.all()
    return render(request,'admin/view_parents.html',{'parents':parents})

def view_courssub(request):
    courses = course.objects.all()
    subjects = subject.objects.all()
    return render(request,'admin/courssub.html',{'cours':courses,'subs':subjects})



       #2
def teacher_home(request):
    total = student.objects.count()
    total1 = assignment.objects.count()
    total2 = notification.objects.count()
    teacher_details = teacher.objects.get(teacher_id=request.session['teacher'])
    return render(request,'teacher/teacher.html',{'total':total,'total1':total1,'total2':total2,'teacher_name':teacher_details.name})


def manage_student(request):
     cou_rse = course.objects.all()
     if request.method=='POST':
        fullname=request.POST['nname']
        place=request.POST['place']
        phone=request.POST['phone']
        email=request.POST['email']
        semester=request.POST['sem']
        title=request.POST['title']
        des=request.POST['description']
        date=request.POST['date']
        username=request.POST['uname']
        password=request.POST['pswd']
        course_id=request.POST['course_id']
        teacher_data = teacher.objects.get(pk=request.session['teacher'])
        course_id=course.objects.get(pk=course_id)
        # print(teacher_data.pk,"((((((((((()))))))))))")
        res1=login(user_name=username,password=password,usertype='student')
        res1.save() 
        res2=student(name=fullname,place=place,phone=phone,email=email,sem=semester,course=course_id,login=res1,teacher=teacher_data)
        res2.save()
        res3=additional(title=title,description=des,date=date,student=res2)
        res3.save()
        studnt = student.objects.count()
        return HttpResponse("<script>alert('Added');window.location='/manage_student'</script>")
    #  student_details=student.objects.get(teacher=request.session['teacher'])
     return render(request,'teacher/manage_student.html',{'course':cou_rse})


# def view_student(request):
#     student_details=student.objects.filter(teacher=request.session['teacher'])
#     return render(request,'teacher/viewstudent.html',{'students':student_details})

def view_student(request):
    student_details = student.objects.filter(teacher=request.session['teacher']).prefetch_related('additional_set')
    return render(request, 'teacher/viewstudent.html', {'students': student_details})


def delete_student(request,id):
    result = student.objects.get(student_id=id)
    result.delete()
    return HttpResponse("<script>alert('Student Deleted');window.location='/viewstudent'</script>")

def edit_student(request,id):
    result1 = student.objects.get(student_id=id)
    result2 = additional.objects.all()
    if request.method == 'POST':
        result1.name = request.POST['name']
        result1.email = request.POST['email']
        result1.place = request.POST['place']
        result1.phone = request.POST['phone']
        result2.title = request.POST['title']
        result2.description = request.POST['description']
        student_id=request.POST['student']
        subs=student.objects.get(pk=student_id)
        result1.student=subs
        result1.save()
        return HttpResponse("<script>alert('Student updated');window.location='/view_student'</script>")
    return render(request,'teacher/edit_student.html',{'std':result1,'subs':result2})


def view_notification(request):
    res12 = notification.objects.all()
    return render(request,'teacher/viewnotification.html',{"notifications":res12})

def view_passrequest(request):
    res12 = pass_request.objects.all()
    return render(request,'teacher/viewpassrequest.html',{"passrequest":res12})

def pass_accept(request,id):
    result2 = pass_request.objects.get(req_id=id)
    result2.status = "accepted"
    result2.save()
    return HttpResponse("<script>alert('Status Updated');window.location='/view_pass_request'</script>")

def pass_reject(request,id):
    result2 = pass_request.objects.get(req_id=id)
    result2.status = "rejected"
    result2.save()
    return HttpResponse("<script>alert('Status Updated');window.location='/view_pass_request'</script>")

def teacher_view_students_to_add_score(request,set_id):
    print(set_id,"///////////////////")
    teacher_course_details = teacher.objects.get(teacher_id=request.session['teacher'])

    student_details=student.objects.filter(course_id=teacher_course_details.course_id)
    return render(request,'teacher/teacher_view_students_to_add_score.html',{'students':student_details,'set_id':set_id})



# views.py
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from datetime import date
# Assuming you have relevant models imported
# from .models import Score, Student, Set

@require_http_methods(["GET", "POST"])
def teacher_add_score(request, student_id, set_id):
    """
    View to handle adding scores for a student
    """
    if request.method == "POST":
        # For AJAX requests
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            try:
                data = json.loads(request.body)
                mark = data.get('mark')


                
                # Process the data (save to database)
                # Example (replace with your actual model and field names):
                # score, created = Score.objects.update_or_create(
                #     student_id=student_id,
                #     set_id=set_id,
                #     defaults={'mark': mark}
                # )
                
                # Just for testing/debug

                print(mark,'((((((((((((((()))))))))))))))')
                print(f"Adding score: mark={mark}, student_id={student_id}, set_id={set_id}")

                result_adding = assessment(score=mark,student_id=student_id,set_id=set_id,date=date.today())
                result_adding.save()
                
                return JsonResponse({'success': True, 'message': 'Score added successfully'})
            except Exception as e:
                return JsonResponse({'success': False, 'message': str(e)})
        
        # For traditional form submissions
        else:
            mark = request.POST.get('mark')
            
            # Process the data (save to database)
            # Example (replace with your actual model and field names):
            # score, created = Score.objects.update_or_create(
            #     student_id=student_id,
            #     set_id=set_id,
            #     defaults={'mark': mark}
            # )
            
            print(f"Adding score: mark={mark}, student_id={student_id}, set_id={set_id}")
            
            # Redirect back to the students list
            return redirect('teacher_students')
    
    # If it's a GET request, render a form (fallback option)
    # return render(request, 'add_score.html', {'student_id': student_id, 'set_id': set_id})
    return ""




def manage_parent(request,id):
    
    try:
        res12 = parent.objects.get(student=id)
        print("HHHHHHHHHHHHHHHH")
    except:
        print("uuuuuuuuuuuu")
        res12 = ''

    if request.method=='POST':
        fullname=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        address=request.POST['address']
        username=request.POST['uname']
        password=request.POST['pswd']



        subs=student.objects.get(pk=id)

        teachr = teacher.objects.get(pk=request.session['teacher'])
                                                 
        res11=login(user_name=username,password=password,usertype='parent') 
        res11.save()                                 

        res12=parent(name=fullname,phone=phone,email=email,address=address,teacher=teachr,student=subs,login=res11)
        res12.save()

        return HttpResponse("<script>alert('Parent Registered');window.location='/viewstudent'</script>")

    return render(request,'teacher/parent.html',{"manage_parent":res12})                   


def lecture_note(request):
    subs=subject.objects.all()

    if request.method=='POST':
        sub_id=request.POST['subject']
        
        subs_id=subject.objects.get(pk=sub_id)

        photo=request.FILES['file']
        fs=FileSystemStorage()
        pdf=fs.save(photo.name,photo)


        res2=note(file=photo,date=datetime.today().date(),subject=subs_id)
        res2.save()



        return HttpResponse("<script>alert('Note Uploaded');window.location='/lecture_note'</script>")
    
    return render(request,'teacher/note.html',{'subs':subs})    

def assign_ment(request):
    # result1 = student.objects.get(student_id=id)

    subs=subject.objects.all()

    if  request.method=='POST':
        #  sub_id=request.POST['subject']
        
        # subs_id=subject.objects.get(pk=sub_id)
        teachr = teacher.objects.get(pk=request.session['teacher'])


        photo=request.FILES['file']
        deadline=request.POST['deadline']
        fs=FileSystemStorage()
        pdf=fs.save(photo.name,photo)


        res2=assignment(file=photo,date=datetime.today().date(),teacher=teachr,subject=teachr.subject,deadline=deadline)
        res2.save()



        return HttpResponse("<script>alert('Assignment Uploaded');window.location='/assign_ment'</script>")
    
    return render(request,'teacher/assignment.html',{'subs':subs})

def assign_submission(request):
    res12 = assign_submiss.objects.all()
    return render(request,'teacher/viewsubmitassign.html',{"assignments":res12})

def view_complaint(request):
    comp=complaint.objects.all()

    #    return HttpResponse("<script>alert('Reply Sent');window.location='/teacher'</script>")

    return render(request,'teacher/viewcomplaints.html',{"complaints":comp})


def assess_ment(request):
    
    if request.method == 'POST':
        name = request.POST['test_name']
        questions = request.POST['question_count']
        result = assessment_set(set_name=name,question_count=questions,teacher_id=request.session['teacher'])
        result.save()
        return HttpResponse("<script>alert('Assessment Created');window.location='/assess_ment'</script>")
    return render(request,'teacher/assessment.html')


def teacher_add_results(request):
    teacher_datas = assessment_set.objects.filter(teacher_id=request.session['teacher'])

    return render(request,'teacher/teacher_add_results.html',{'datas':teacher_datas})

       
# def teacher_mark_attendance(request):
#     teacher_datas = teacher.objects.get(pk=request.session['teacher'])
#     student_details = student.objects.filter(course_id=teacher_datas.course_id)
#     print(student_details,'////////////////////////')
#     return render(request,'teacher/teacher_mark_attendance.html',{'student_details':student_details})


# def mark_attendance(request,student_id,course_id):
    
#     attendance_results = attendance(student_id=student_id,course_id=course_id,teacher_id=request.session['teacher'],date=datetime.now().date(),attendance='present')
#     attendance_results.save()
#     return HttpResponse("<script>alert('Attendance Marked');window.location='/teacher_mark_attendance'</script>")


from datetime import datetime
from django.http import HttpResponse
from .models import attendance, student, course, teacher  # adjust import as needed

def mark_attendance(request, student_id, course_id):
    today = datetime.now().date()

    # Check if attendance already marked for this student today
    existing_attendance = attendance.objects.filter(
        student_id=student_id,
        course_id=course_id,
        teacher_id=request.session['teacher'],
        date=today
    ).first()

    if existing_attendance:
        msg = f"Attendance already marked as {existing_attendance.attendance.capitalize()}"
        return HttpResponse(f"<script>alert('{msg}');window.location='/teacher_mark_attendance'</script>")
    else:
        attendance_results = attendance(
            student_id=student_id,
            course_id=course_id,
            teacher_id=request.session['teacher'],
            date=today,
            attendance='present'
        )
        attendance_results.save()
        return HttpResponse("<script>alert('Attendance Marked');window.location='/teacher_mark_attendance'</script>")



from datetime import datetime

def teacher_mark_attendance(request):
    teacher_datas = teacher.objects.get(pk=request.session['teacher'])
    student_details = student.objects.filter(course_id=teacher_datas.course_id)

    today = datetime.now().strftime('%Y-%m-%d')

    for stu in student_details:
        record = attendance.objects.filter(student=stu, date=today).first()
        stu.attendance_status = record.attendance if record else None

    return render(request, 'teacher/teacher_mark_attendance.html', {
        'student_details': student_details
    })



# def mark_absent(request,student_id,course_id):
    
#     attendance_results = attendance(student_id=student_id,course_id=course_id,teacher_id=request.session['teacher'],date=datetime.now().date(),attendance='absent')
#     attendance_results.save()
#     return HttpResponse("<script>alert('Attendance Marked');window.location='/teacher_mark_attendance'</script>")


def mark_absent(request, student_id, course_id):
    today = datetime.now().date()

    existing_attendance = attendance.objects.filter(
        student_id=student_id,
        course_id=course_id,
        teacher_id=request.session['teacher'],
        date=today
    ).first()

    if existing_attendance:
        msg = f"Attendance already marked as {existing_attendance.attendance.capitalize()}"
        return HttpResponse(f"<script>alert('{msg}');window.location='/teacher_mark_attendance'</script>")
    else:
        attendance_results = attendance(
            student_id=student_id,
            course_id=course_id,
            teacher_id=request.session['teacher'],
            date=today,
            attendance='absent'
        )
        attendance_results.save()
        return HttpResponse("<script>alert('Marked as Absent');window.location='/teacher_mark_attendance'</script>")

    
#3

def student_home(request):
    total = teacher.objects.all()
    total1 = assignment.objects.all()
    stud_id=student.objects.get(pk=request.session['student'])
    return render(request,'student/student.html',{'total':total,'total1':total1,'studname':stud_id})
                   
def view_teachers(request):
    res12 = teacher.objects.all()
    return render(request,'student/viewteachers.html',{"teachers":res12})

def view_lecture(request):
    res12 = note.objects.all()
    return render(request,'student/viewlecture.html',{"lecture":res12})

def viewnotification(request):
    res12 = notification.objects.all()
    return render(request,'student/viewnotification.html',{"notifications":res12})


def assignmment(request):
    subs = subject.objects.all()
    assignments = assignment.objects.all()  # Fetch all assignments

    if request.method == 'POST':
        teachr = teacher.objects.get(pk=request.session['teacher'])
        photo = request.FILES['file']
        deadline = request.POST['deadline']
        fs = FileSystemStorage()
        pdf = fs.save(photo.name, photo)

        res2 = assignment(
            file=photo,
            date=datetime.today().date(),
            teacher=teachr,
            subject=teachr.subject,
            deadline=deadline
        )
        res2.save()

        return HttpResponse("<script>alert('Assignment Uploaded');window.location='/assignmment'</script>")
    
    return render(request, 'student/viewassignment.html', {'subs': subs, 'assignments': assignments})


def assign_sub(request,id):
    subs = subject.objects.all()

    if request.method == 'POST':
        # sub_id = request.POST['subject']
        # subs_id = subject.objects.get(pk=sub_id)
        # teachr = teacher.objects.get(pk=request.session['teacher'])

        assign_id = assignment.objects.get(pk=id)

        stud_id=student.objects.get(pk=request.session['student'])

        photo = request.FILES['file']
        # subdate = request.POST['submiss_date']
        fs = FileSystemStorage()
        pdf = fs.save(photo.name, photo)

        res2 = assign_submiss(
            file=photo,
            submiss_date=datetime.today().date(),
            assign=assign_id,
            # submiss_date=subdate,
            student=stud_id
        )
        res2.save()

        return HttpResponse("<script>alert('Assignment Uploaded');window.location='/assignment'</script>")
    
    return render(request, 'student/assignsub.html', {'subs': subs})

def passreq(request):
    if request.method == 'POST':
        date = request.POST['date']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        passtype = request.POST['passtype']

        stud_id=student.objects.get(pk=request.session['student'])


        res12 = pass_request(
            date=date,
            start_time=start_time,
            end_time=end_time,
            pass_type=passtype,
            student=stud_id,
            status='pending'
        )
        res12.save()

        return HttpResponse("<script>alert('Pass Request Gone');window.location='/pass_request'</script>")
    
    return render(request, 'student/passrequest.html')


def view_passreq(request):
    res12 = pass_request.objects.all()
    return render(request,'student/viewpassreq.html',{"passreq":res12})


# def student_view_attendance(request):
#     res12 = attendance.objects.filter(student_id=request.session['student'])
#     return render(request,'student/student_view_attendance.html',{"attendance":res12})

from django.shortcuts import render
from django.http import HttpResponse
from .models import attendance, teacher, subject

def student_view_attendance(request):
    # Default query: Get all attendance records for the student
    res12 = attendance.objects.filter(student_id=request.session['student'])

    # Filter by date if provided
    date_filter = request.GET.get('date', '')
    if date_filter:
        res12 = res12.filter(date=date_filter)
    
    # Filter by teacher if provided
    teacher_filter = request.GET.get('teacher', '')
    if teacher_filter:
        res12 = res12.filter(teacher_id=teacher_filter)
    
    # Filter by subject if provided
    subject_filter = request.GET.get('subject', '')
    if subject_filter:
        res12 = res12.filter(teacher__subject_id=subject_filter)
    
    # Get all teachers and subjects for the filter dropdowns
    teachers = teacher.objects.all()
    subjects = subject.objects.all()

    return render(request, 'student/student_view_attendance.html', {
        "attendance": res12,
        "teachers": teachers,
        "subjects": subjects,
    })


def give_complaint(request):
    complts = complaint.objects.filter(login_id=request.session['log'])
    if request.method == 'POST':
        complaints = request.POST['complaint']
        # reply = request.POST['reply']
        # date = request.POST['date']
        
        res = complaint(
            complaint=complaints,
            reply='pending',
            date=date.today(),
            login_id=request.session['log']
        )
        res.save()
        # stud_id=student.objects.get(pk=request.session['student'])
        

        return HttpResponse("<script>alert('Complaint Sent');window.location='/student'</script>")
    return render(request,'student/complaint.html',{"complaints":complts})




from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai
import json
import traceback

# Configure the Gemini API with your key
# genai.configure(api_key="AIzaSyAIcGw0rEzWnz0IOo-5TZrkfFiPuD7_uKM")
genai.configure(api_key="AIzaSyAIcGw0rEzWnz0IOo-5TZrkfFiPuD7_uKM")



def chat_bot(request):
    """Render the chat bot interface."""
    return render(request, "student/chat_bot.html")

@csrf_exempt
def chat_response(request):
    """Handle chat requests and return AI responses."""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")
            
            # Create model and generate response
            # model = genai.GenerativeModel('gemini-1.5-pro')
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(user_message)
            
            # Debug: Print response structure
            print(f"Response type: {type(response)}")
            print(f"Response attributes: {dir(response)}")
            
            # Try to extract text
            response_text = "No text found"
            
            if hasattr(response, "text"):
                response_text = response.text
                print(f"Found response.text: {response_text[:100]}...")
                
            # Return the text response
            return JsonResponse({
                "response": response_text,
                "debug_info": {
                    "response_type": str(type(response)),
                    "has_text_attr": hasattr(response, "text"),
                }
            })
        except Exception as e:
            trace = traceback.format_exc()
            print(f"Error: {str(e)}")
            print(f"Traceback: {trace}")
            return JsonResponse({
                "error": str(e), 
                "traceback": trace
            }, status=500)
    
    return JsonResponse({"error": "Invalid request method"}, status=400)

# app

def parent_login(request):
   data=[]
   u=request.GET.get('u')
   p=request.GET.get('p')

   print(u,p,"")
   
   
   try:
    print("Checking login for:", u, p)
    z = login.objects.filter(user_name=u, password=p)
    print("Query result:", list(z))  # Print results for debugging
    
    if z:
        data = list(z.values("log_id", "user_name", "password", "usertype"))
        status = "success"
    else:
        status = "failed"
   except Exception as e:
    status = "error"
    print("Exception occurred:", str(e))  # Print the actual error


    
   print(status,data)
  

   return JsonResponse({'status':status,'view':data})


def parent_student(request):
    data = []
    lid_parent = request.GET.get('pli')

    print(lid_parent, "")

    try:
        # Find parent based on login
        res = parent.objects.get(login=lid_parent)

        # Fetch student records, joining with course and teacher
        z = student.objects.filter(parent=res.parent_id).select_related('course', 'teacher')

        # Debugging log (optional)
        print("Query result:", list(z))

        if z:
            # Build response data with course name and teacher name
            data = []
            for s in z:
                data.append({
                    "student_id": s.student_id,
                    "name": s.name,
                    "place": s.place,
                    "phone": s.phone,
                    "email": s.email,
                    "course": s.course.course,  # Access course name via relation
                    "teacher": s.teacher.name,  # Access teacher name via relation
                    "sem": s.sem
                })

            status = "success"
        else:
            status = "failed"

    except Exception as e:
        status = "error"
        print("Exception occurred:", str(e))

    print(status, data, "***************************")
    return JsonResponse({'status': status, 'view': data})





def parent_view_notifications(request):
    data = []  # Initialize an empty list for notifications

    try:
        # Fetch all notification objects
        notifications = notification.objects.all()

        # Debugging: Print query results
        # print("Query result:", list(notifications.values("title", "description", "date", "status")))

        # Check if notifications exist
        if notifications.exists():
            data = list(notifications.values("title", "description", "date", "status"))
            status = "success"
        else:
            status = "failed"
    
    except Exception as e:
        status = "error"
        print("Exception occurred:", str(e))  # Print the actual error for debugging

    print(status, data, "gfgggvhghbh")  # Debugging output
    return JsonResponse({'status': status, 'view': data})


# def parent_view_student_assessment(request):
#     parent_login_id = request.GET.get('parent_login_id')

#     parent_data = parent.objects.get(login=parent_login_id)
#     student_data = student.objects.get(student_id=parent_data.student_id)


#     assessment_details = assessment.objects.filter(student_id=student_data.student_id)

#     return ""


from django.http import JsonResponse
from .models import assessment, parent, student  # make sure these are correctly imported

def parent_view_student_assessment(request):
    data = []

    try:
        parent_login_id = request.GET.get('parent_login_id')

        # Fetch the parent and corresponding student
        parent_data = parent.objects.get(login=parent_login_id)
        student_data = student.objects.get(student_id=parent_data.student_id)

        # Get assessment records for the student
        assessment_records = assessment.objects.filter(student=student_data)

        if assessment_records.exists():
            for record in assessment_records:
                assessment_set_obj = record.set
                teacher = assessment_set_obj.teacher
                subject = teacher.subject

                data.append({
                    "assessment_name": assessment_set_obj.set_name,
                    "question_count": assessment_set_obj.question_count,
                    "teacher_name": teacher.name,
                    "subject": subject.subject,
                    "score": record.score,
                    "date": record.date,
                })
            status = "success"
        else:
            status = "no_records"

    except Exception as e:
        print("Exception occurred:", str(e))
        status = "error"

    res = {'status': status, 'assessment_details': data}
    print(res, "333333333333333333333333333333")

    return JsonResponse({'status': status, 'assessment_details': data})

      

from django.http import JsonResponse
from .models import attendance, parent, student  # adjust the import as needed

def parent_view_student_attendance(request):
    data = []  # List to hold attendance details

    try:
        parent_login_id = request.GET.get('parent_login_id')

        # Get the student linked to the parent
        parent_data = parent.objects.get(login=parent_login_id)
        student_data = student.objects.get(student_id=parent_data.student_id)

        # Filter attendance records for the student
        attendance_details = attendance.objects.filter(student=student_data)

        # Check if attendance records exist
        if attendance_details.exists():
            # Construct response data
            for record in attendance_details:
                data.append({
                    "attendance": record.attendance,
                    "date": record.date,
                    "course": record.course.course if record.course else None,
                    "teacher_name": record.teacher.name if record.teacher else None,
                    "subject": record.teacher.subject.subject if record.teacher and record.teacher.subject else None,
                })
            status = "success"
        else:
            status = "no_records"

    except Exception as e:
        print("Exception occurred:", str(e))  # Debugging output
        status = "error"

    res = {'status': status, 'attendance_details': data}
    print(res, "gfgggvhghbh")  

    return JsonResponse({'status': status, 'attendance_details': data})
