import requests
import json
import pprint
# this is saral webiste link 
saralUrl = "http://saral.navgurukul.org/api"
def requestUrl(url):
    res = requests.get(url)
    respo = res.json()
    return respo
courseUrl = saralUrl + '/courses'
courseUrlCall = requestUrl(courseUrl)  


def displayCourse():
    index = 0
    while index < len(courseUrlCall['availableCourses']):
        courseIndex =courseUrlCall ['availableCourses'][index]
        courseName = courseIndex['name']
        courseId = courseIndex['id']
        courseID.append(courseId)
        print index, courseName
        index= index+1
courseID = []

def useInput():
    select_course = int(input("enter your couser nmo"))
    show_select_course = courseID[select_course]
    exerciseUrl =  courseUrl+ '/' + str(show_select_course) +'/exercises'
    exerciseUrlCall  = requestUrl(exerciseUrl)

def displayExercise():
    Ex_index = 0
    while Ex_index < len(exerciseUrlCall['data']):
        Exercise_index = exerciseUrlCall ['data'][Ex_index]
        Exercise_name = Exercise_index['name']
        print Ex_index, Exercise_name 
        child_exercise =  Exercise_index['childExercises'] 
        childExercise.append(child_exercise)   
        Exercise_slug = Exercise_index['slug']
        slug.append( Exercise_slug)
        Ex_index = Ex_index + 1
    return slug    
childExercise = []
slug = []


def start():
    while True:
        courseID =  displayCourse()
        c = useInput()
        childExercise= displayExercise()

        break
if __name__ == "__main__":
    start()   