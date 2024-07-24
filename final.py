#Noah Persily
from cs50 import get_string
from cs50 import get_int
import csv
#https://realpython.com/sort-python-dictionary/#using-the-sorted-function
#global variables
final_movies = {}
form_movies = []


def init() :
    #open csv
    with open("final.csv") as file:
        reader = csv.DictReader(file)
        # for every row
        for row in reader:
            temp = []
            #iterate threw collumns
            for i in range(1,11) :
                i = str(i)
                #if there is a value
                if(not (row[i] is None)) :
                    row[i] = row[i].lower()
                    #add it to temp
                    temp.append(row[i])
            #add list to another list        
            form_movies.append(temp)
    
def main() :
    length = get_int("how many movies(up to 10): ")
    movies = get_movie(length)
    init()
    compare(movies)
    sort_print()
    edit_csv(movies, length)
    

def common_elements(arr1, arr2) :
    
    for i in arr1 :
        if i in arr2:
            return True

def get_movie(length) :
    movies = []
    for i in range(length):
        temp = (get_string("Movie: "))
        movies.append(temp.lower())
    return movies      
 
def compare(user_movies) :
  
    #iterate through row of training movies
    for list_of_movies in form_movies :
        if(common_elements(user_movies, list_of_movies)) :
            #for every movie in that list
            for movie in list_of_movies :
                if(not(movie in user_movies)) :
                    if(not(movie in final_movies)) :
                        final_movies[movie] = 0
                    final_movies[movie] += 1
                            
def sort_print() :
    for movie in sorted(final_movies, key=lambda movie: final_movies[movie], reverse=True):
        print(f"{movie}")

   
def value_getter(item) :
    return item[1]
def edit_csv(movies, length) :
    # list of column names 
    if length == 1 :
        return
    field_names = []
    add_movies = {}
    for i in range(length) :
        field_names.append(str(i))
        add_movies[field_names[i]] = movies[i]         
    with open('final.csv', 'a') as csv_file:
        dict_object = csv.DictWriter(csv_file, fieldnames=field_names) 
        dict_object.writerow(add_movies)
        
if __name__ == "__main__":
    main()