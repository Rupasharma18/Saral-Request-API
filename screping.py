import requests
import json
import pprint

saralUrl = "http://saral.navgurukul.org/api"
def saralRequest(url):
    respons = requests.get(url)
    resops_json = respons.json()
    return resops_json
coursesUrl = saralUrl+ '/courses'
coursesUrlCall= saralRequest(coursesUrl)
 
print  "**********************************WELCOME TO SARAL**********************************"
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

select_course = int(input("choose your courses no.  :- "))
show_select_course = courseID[select_course]
print "***************************************WELCOME TO EXERCISE*************************************"
ExerciseUrl = coursesUrl + '/' + str(show_select_course) +'/exercises'
ExerciseUrlCall  = saralRequest(ExerciseUrl)


slug = []
def displayExercise():
    childExercise = []
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
childExercise =displayExercise()

selectExercise =  int(input("choose your exercise no. :- "))
show_select_exercise = slug[selectExercise]
slugUrl = coursesUrl + '/' + str(show_select_course) + '/exercise/getBySlug?slug=' + show_select_exercise
slugUrlCall = saralRequest(slugUrl)
print (slugUrlCall['content'])

def displayChildExercise():
    child_slug = []
    i = 0
    while i < len(childExercise[selectExercise]):
        child_index = childExercise[selectExercise][i]
        child_name = child_index['name']
        childSlug = child_index['slug']
        child_slug.append(childSlug)
        print i, child_name       
        i = i +1
    return  child_slug  
child_slug = displayChildExercise() 

select_question = int(input("select one question and click on url :- "))
show_select_question =  child_slug[select_question]
print (show_select_question)
childSlugUrl = coursesUrl + '/' + str(show_select_course) + '/exercise/getBySlug?slug=' +show_select_question 
childSlugUrlCall = saralRequest(childSlugUrl)
store_content = childSlugUrlCall['content']
print (store_content)
