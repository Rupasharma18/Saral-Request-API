import requests
import json
import pprint
# this is saral website url
saralUrl = "http://saral.navgurukul.org/api"
def saralRequest(url):
    respons = requests.get(url)
    resops_json = respons.json()
    return resops_json
coursesUrl = saralUrl+ '/courses'
coursesUrlCall= saralRequest(coursesUrl)
 
print  "**********************************WELCOME TO SARAL**********************************"
# all course print here
def displayCourse():
    courseID = []
    index = 0
    while index < len(coursesUrlCall['availableCourses']):
        courseIndex = coursesUrlCall['availableCourses'][index]
        courseName = courseIndex['name']
        courseId = courseIndex['id']
        courseID.append(courseId)
        print index, courseName
        index= index+1
    return courseID
courseID = displayCourse()
# choose course which you want to read.
select_course = int(input("choose your courses no.  :- "))
show_select_course = courseID[select_course]
print "***************************************WELCOME TO EXERCISE*************************************"
# in this website get  all the course's exercises
ExerciseUrl = coursesUrl + '/' + str(show_select_course) +'/exercises'
ExerciseUrlCall  = saralRequest(ExerciseUrl)
# this funstion inside execises display. 
childExercise = []
slug = []
def displayExercise():
    Ex_index = 0
    while Ex_index < len(ExerciseUrlCall['data']):
        Exercise_index = ExerciseUrlCall['data'][Ex_index]
        Exercise_name = Exercise_index['name']
        print Ex_index, Exercise_name 
        child_exercise =  Exercise_index['childExercises'] 
        childExercise.append(child_exercise)   
        Exercise_slug = Exercise_index['slug']
        slug.append( Exercise_slug)
        Ex_index = Ex_index + 1
    return slug    
displayExercise()
# choose one exercise.
selectExercise =  int(input("choose your exercise no. :- "))
show_select_exercise = slug[selectExercise]
slugUrl = coursesUrl + '/' + str(show_select_course) + '/exercise/getBySlug?slug=' + show_select_exercise
slugUrlCall = saralRequest(slugUrl)
print (slugUrlCall['content'])
# this function show the exercise's inside exercise.
def displayChildExercise():
    child_slug = []
    i = 0
    while i < len(childExercise[selectExercise]):
        child_index = childExercise[selectExercise][i]
        child_name = child_index['name']
        childSlug = child_index['slug']
        child_slug.append(childSlug)
        print i+1, child_name       
        i = i +1
    return  child_slug  
child_slug =displayChildExercise() 

select_question = int(input("select one question and click on url :- "))
show_select_question =  child_slug[select_question]
print (show_select_question)

def display():
    childSlugUrl = coursesUrl + '/' + str(show_select_course) + '/exercise/getBySlug?slug=' +show_select_question 
    childSlugUrlCall = saralRequest(childSlugUrl)
    store_content = childSlugUrlCall['content']
    print (store_content)
display()
# this function for next execise.
def contentNext():    
    user_input = int(input("enter your num question"))
    slug_list = child_slug[user_input+-1] 
    url =  coursesUrl + '/' + str(show_select_course) + '/exercise/getBySlug?slug=' + slug_list
    urlCall = saralRequest(url)
    nextContent = urlCall['content']
    print (nextContent)
   
# this function previous execise.
def contentPrevious():
    userInput = int(input("enter your num question"))
    slugList = child_slug[userInput+-1] 
    url1 =  coursesUrl + '/' + str(show_select_course) + '/exercise/getBySlug?slug=' + slugList
    urlCall = saralRequest(url1)
    previousContent = urlCall['content']
    print (previousContent)
   
# here calling the next, pervious function and exit.
while True:
    choose= raw_input("Enter 'n' to go to next exercise or 'p' to go to previous exercise or to exit enter e key :- ")
    if choose == 'n':
        contentNext() 
    elif choose == 'p':
        contentPrevious() 
    elif choose == 'e':
        print("\n\n---------------------You choose exit from current COURSE.------------------------------------\n\n")
        break    
 
