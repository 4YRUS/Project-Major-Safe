from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Images,PDFs
import json 
import base64
from .imagereader import read_image
from django.core.files.base import ContentFile
import time
from .TextGeneration import read_pdf,get_mcqs

# Home Page
def home(request):
	return render(request,'home.html')

# About Us Page 
def aboutUs(request):
	return render(request,'aboutUs.html')

# aiCanvas
def aiCanvas(request):
	return render(request,'aiCanvas.html')

# Calls the external function.
def read_canvas(path):
    text = read_image(path)
    print(text)
    return text

# returns response for aiCanvas
def return_canvas_response(request):
    message = "Hey Ssup??!! Draw or Write any thing, let me solve."
    if request.method=='POST':
        try:
            message = "HELLO IT HAS COME HERE"

            print(f"\n\n\n {message} \n\n\n")

            imagedata = json.loads(request.body).get('image')

            a,imagestring = imagedata.split(';base64,')

            image = ContentFile(base64.b64decode(imagestring),name='firstimage.png')

            obj1 = Images.objects.create(image = image)

            image_url = obj1.image.url

            print('\n\n\n',image_url,"\n\n\n")

            try:

                message = read_canvas("C:\\Users\\bss22\\OneDrive\\Desktop\\Don't Open\\DJANGO\\MAJOR PROJECT\\major_project" + image_url)
                # message = read_canvas("C:\\Users\\bss22\\OneDrive\\Desktop\\Don't Open\\DJANGO\\work\\" + image_url)
                # message = "THIS IS A TEMPORARY RESPONSE"
                # print(f"\n\n\n {message} \n\n\n")
                # time.sleep(10)
                obj1.delete()

                return JsonResponse({"message": message})
            except:
                obj1.delete()
                return JsonResponse({"message":"Sorry, There was an error. "})
        except:
            return JsonResponse({"Error" : "Not Valid Form"})


    return JsonResponse({"message":message})


#Path Finder
def pathFinder(request):
	return render(request,"pathFinder.html")

# Home page for MCQ
def mcqTestHome(request):
    return render(request, 'mcqTestHome.html')

def getPdfs(request):
    pdfs = PDFs.objects.all().values()
    pdfs = list(pdfs)[::-1]
    return JsonResponse({"data":pdfs})

# Extracts pdfs for a new test.
def extractMcqs(request):

    if request.method == "POST":

        try:
            doc = PDFs(pdf=request.FILES['pdf'])
            doc.save()

            print("\n\n\n",doc.pdf.url,"\n\n\n")

            pdf_url = doc.pdf.url 

            data = get_mcqs("C:\\Users\\bss22\\OneDrive\\Desktop\\Don't Open\\DJANGO\\MAJOR PROJECT\\major_project" + pdf_url)
            # data = {'topic': 'Data Structures and Data Manipulation in C#', 'description': 'This module covers fundamental data structures like arrays and various C# collections (Lists, Dictionaries, HashSets, SortedSets, Queues, LinkedLists), along with string manipulation techniques, numeric formatting, and date/time operations in C#.', 'mcqs': [{'question': 'Which of the following statements about C# arrays is true?', 'options': ['A) All arrays in C# are statically allocated.', 'B) The size of a C# array can be changed after it is created.', 'C) C# arrays are objects of the base type System.Array.', 'D) Array indices in C# begin from 1.'], 'answer': 'C) C# arrays are objects of the base type System.Array.'}, {'question': "What is the primary purpose of 'Collections' in C#?", 'options': ['A) To define custom data types.', 'B) To store and manipulate groups of related objects.', 'C) To handle exceptions in a program.', 'D) To manage file I/O operations.'], 'answer': 'B) To store and manipulate groups of related objects.'}, {'question': 'Which of the following is a key characteristic of the C# `Dictionary` collection?', 'options': ['A) It allows duplicate keys and values.', 'B) Keys can be null, but values cannot.', 'C) Keys must be unique, and duplicate keys will throw an exception.', 'D) It is primarily used for ordered sequential access.'], 'answer': 'C) Keys must be unique, and duplicate keys will throw an exception.'}, {'question': 'What is a primary advantage of using a `HashSet` over a `List` in C# when storing elements?', 'options': ['A) `HashSet` preserves the order of elements.', 'B) `HashSet` allows for faster element access by index.', 'C) `HashSet` automatically prevents duplicate elements.', 'D) `HashSet` supports heterogeneous data types.'], 'answer': 'C) `HashSet` automatically prevents duplicate elements.'}, {'question': 'What unique property does `SortedSet` offer compared to `HashSet` in C#?', 'options': ['A) `SortedSet` allows duplicate elements.', 'B) `SortedSet` stores elements in a random order.', 'C) `SortedSet` stores elements in sorted (ascending) order.', 'D) `SortedSet` supports different types of elements within the same set.'], 'answer': 'C) `SortedSet` stores elements in sorted (ascending) order.'}, {'question': 'In C#, what happens when you perform an operation that appears to modify a `string` object?', 'options': ['A) The original string object is updated in memory.', 'B) A new string object is created with the modified content.', 'C) The operation is ignored if the string is immutable.', 'D) It results in a compilation error because strings cannot be modified.'], 'answer': 'B) A new string object is created with the modified content.'}, {'question': 'Which type of string literal in C# allows including special characters like backslashes (`\\`) without needing escape sequences?', 'options': ['A) Double-quoted string literals', 'B) Interpolated string literals', 'C) Verbatim string literals', 'D) Character literals'], 'answer': 'C) Verbatim string literals'}, {'question': "What is the purpose of the 'P' (Percent) standard numeric format specifier in C#?", 'options': ['A) To display a number with a specific precision after the decimal point.', 'B) To convert a number to a string representing a percentage by multiplying it by 100.', 'C) To format a number as currency.', 'D) To represent a number in scientific (exponential) notation.'], 'answer': 'B) To convert a number to a string representing a percentage by multiplying it by 100.'}, {'question': "In custom numeric format strings, what does the '0' (Zero placeholder) custom specifier do?", 'options': ['A) It hides the corresponding digit if it is zero.', 'B) It always displays a zero in the result string if a digit is not present.', 'C) It represents a thousands separator.', 'D) It marks the beginning of a negative number.'], 'answer': 'B) It always displays a zero in the result string if a digit is not present.'}, {'question': 'How would you obtain the current date and time in Coordinated Universal Time (UTC) using C#?', 'options': ['A) `DateTime.Now;`', 'B) `DateTime.Current;`', 'C) `DateTime.UtcNow;`', 'D) `DateTime.Parse("UTC");`'], 'answer': 'C) `DateTime.UtcNow;`'}]}

            request.session['mcq-questions'] = data 

        except:
            return JsonResponse({"message":"Error has occurred", "flag" : False, "id" : None})

    return JsonResponse({"message":"Successfully Completed", "flag" : True, "id" : doc.id})

# Extracts Existing Pdfs
def extractExistingPdf(request,pk):
    try:
        print(pk)
        doc = PDFs.objects.get(id = pk)
        print(doc)

        print("\n\n\n",doc.pdf.url,"\n\n\n")

        pdf_url = doc.pdf.url 

        data = get_mcqs("C:\\Users\\bss22\\OneDrive\\Desktop\\Don't Open\\DJANGO\\MAJOR PROJECT\\major_project" + pdf_url)
        # data = {'topic': 'Data Structures and Data Manipulation in C#', 'description': 'This module covers fundamental data structures like arrays and various C# collections (Lists, Dictionaries, HashSets, SortedSets, Queues, LinkedLists), along with string manipulation techniques, numeric formatting, and date/time operations in C#.', 'mcqs': [{'question': 'Which of the following statements about C# arrays is true?', 'options': ['A) All arrays in C# are statically allocated.', 'B) The size of a C# array can be changed after it is created.', 'C) C# arrays are objects of the base type System.Array.', 'D) Array indices in C# begin from 1.'], 'answer': 'C) C# arrays are objects of the base type System.Array.'}, {'question': "What is the primary purpose of 'Collections' in C#?", 'options': ['A) To define custom data types.', 'B) To store and manipulate groups of related objects.', 'C) To handle exceptions in a program.', 'D) To manage file I/O operations.'], 'answer': 'B) To store and manipulate groups of related objects.'}, {'question': 'Which of the following is a key characteristic of the C# `Dictionary` collection?', 'options': ['A) It allows duplicate keys and values.', 'B) Keys can be null, but values cannot.', 'C) Keys must be unique, and duplicate keys will throw an exception.', 'D) It is primarily used for ordered sequential access.'], 'answer': 'C) Keys must be unique, and duplicate keys will throw an exception.'}, {'question': 'What is a primary advantage of using a `HashSet` over a `List` in C# when storing elements?', 'options': ['A) `HashSet` preserves the order of elements.', 'B) `HashSet` allows for faster element access by index.', 'C) `HashSet` automatically prevents duplicate elements.', 'D) `HashSet` supports heterogeneous data types.'], 'answer': 'C) `HashSet` automatically prevents duplicate elements.'}, {'question': 'What unique property does `SortedSet` offer compared to `HashSet` in C#?', 'options': ['A) `SortedSet` allows duplicate elements.', 'B) `SortedSet` stores elements in a random order.', 'C) `SortedSet` stores elements in sorted (ascending) order.', 'D) `SortedSet` supports different types of elements within the same set.'], 'answer': 'C) `SortedSet` stores elements in sorted (ascending) order.'}, {'question': 'In C#, what happens when you perform an operation that appears to modify a `string` object?', 'options': ['A) The original string object is updated in memory.', 'B) A new string object is created with the modified content.', 'C) The operation is ignored if the string is immutable.', 'D) It results in a compilation error because strings cannot be modified.'], 'answer': 'B) A new string object is created with the modified content.'}, {'question': 'Which type of string literal in C# allows including special characters like backslashes (`\\`) without needing escape sequences?', 'options': ['A) Double-quoted string literals', 'B) Interpolated string literals', 'C) Verbatim string literals', 'D) Character literals'], 'answer': 'C) Verbatim string literals'}, {'question': "What is the purpose of the 'P' (Percent) standard numeric format specifier in C#?", 'options': ['A) To display a number with a specific precision after the decimal point.', 'B) To convert a number to a string representing a percentage by multiplying it by 100.', 'C) To format a number as currency.', 'D) To represent a number in scientific (exponential) notation.'], 'answer': 'B) To convert a number to a string representing a percentage by multiplying it by 100.'}, {'question': "In custom numeric format strings, what does the '0' (Zero placeholder) custom specifier do?", 'options': ['A) It hides the corresponding digit if it is zero.', 'B) It always displays a zero in the result string if a digit is not present.', 'C) It represents a thousands separator.', 'D) It marks the beginning of a negative number.'], 'answer': 'B) It always displays a zero in the result string if a digit is not present.'}, {'question': 'How would you obtain the current date and time in Coordinated Universal Time (UTC) using C#?', 'options': ['A) `DateTime.Now;`', 'B) `DateTime.Current;`', 'C) `DateTime.UtcNow;`', 'D) `DateTime.Parse("UTC");`'], 'answer': 'C) `DateTime.UtcNow;`'}]}

        request.session['mcq-questions'] = data 

    except:
        return JsonResponse({"message":"Error has occurred", "flag" : False, "id" : None})

    return JsonResponse({"message":"Successfully Completed", "flag" : True, "id" : doc.id})    


# Mcq Test Page
def mcqTest(request):

    if request.method == "POST":
        
        # data = {'topic': 'Data Structures and Data Manipulation in C#', 'description': 'This module covers fundamental data structures like arrays, lists, dictionaries, sets, queues, and linked lists in C#. It also delves into string manipulation, various types of string and character literals, and comprehensive data formatting for numeric, date, and time values, including standard and custom format specifiers. Finally, it details methods for converting strings to other data types.', 'mcqs': [{'question': 'Which of the following statements about C# arrays is FALSE?', 'options': ['A) All arrays in C# are dynamically allocated.', 'B) A C# array variable can be declared with `[]` after the data type.', 'C) Once created, the size of a C# array can be changed dynamically.', 'D) C# arrays are objects of base type `System.Array`.'], 'answer': 'C) Once created, the size of a C# array can be changed dynamically.'}, {'question': 'Which of the following is NOT a type of collection explicitly listed as provided by the .NET Framework in the context of storing and manipulating groups of related objects in C# within the given content?', 'options': ['A) Lists', 'B) Dictionaries', 'C) Linked Lists', 'D) Trees'], 'answer': 'D) Trees'}, {'question': 'What is a key characteristic of `HashSet` in C#?', 'options': ['A) Elements are stored in ascending sorted order.', 'B) It allows duplicate elements.', 'C) It stores unique elements and uses a hash table for storage.', 'D) The order of elements is always preserved as they are added.'], 'answer': 'C) It stores unique elements and uses a hash table for storage.'}, {'question': 'In C#, what happens when you perform an operation that appears to modify an existing `string` object?', 'options': ['A) The original string object is modified in place.', 'B) A new string object is created with the modifications.', 'C) An error is thrown because strings are immutable.', 'D) The operation is deferred until the string is explicitly saved.'], 'answer': 'B) A new string object is created with the modifications.'}, {'question': 'Which type of string literal in C# allows including special characters like backslashes without the need for escape sequences?', 'options': ['A) Double-quoted literals', 'B) Interpolated strings', 'C) Verbatim string literals', 'D) Character literals'], 'answer': 'C) Verbatim string literals'}, {'question': 'Which standard numeric format specifier in C# multiplies a number by 100 and displays it with a percent symbol?', 'options': ['A) "N"', 'B) "F"', 'C) "D"', 'D) "P"'], 'answer': 'D) "P"'}, {'question': 'In custom numeric formatting, what is the behavior of the "#" custom specifier if a digit is NOT present in its corresponding position in the value being formatted?', 'options': ['A) A zero is displayed in that position.', 'B) Nothing is stored in that position in the result string.', 'C) An exception is thrown.', 'D) The next available digit is shifted into that position.'], 'answer': 'B) Nothing is stored in that position in the result string.'}, {'question': 'What C# structure represents a time interval, such as the difference between two `DateTime` objects or a specific duration?', 'options': ['A) `DateInterval`', 'B) `Duration`', 'C) `TimeSpan`', 'D) `DateTimeOffset`'], 'answer': 'C) `TimeSpan`'}, {'question': 'Which standard date and time format specifier in C# would you use to get an output like "Monday, April 29, 2024 1:30:00 PM"?', 'options': ["A) 'f'", "B) 'F'", "C) 'g'", "D) 'G'"], 'answer': "B) 'F'"}, {'question': 'To convert a string representation of an integer, for example, "123", into an `int` type in C#, which method is typically used?', 'options': ['A) `int.Convert()`', 'B) `int.ToInteger()`', 'C) `int.Parse()`', 'D) `Convert.ToInt()`'], 'answer': 'C) `int.Parse()`'}]}
        data = request.session['mcq-questions']

        return JsonResponse(data)

    return render(request,'mcqTest.html')