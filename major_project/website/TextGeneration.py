from google import genai
import json


client = genai.Client(api_key="AIzaSyAx8_0F9dpyGa1RXNnpBEaKdI9-1Y6dDD8")


def extract_text_from_image(path, prompt):

    my_file = client.files.upload(file=path)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[my_file, prompt],
    )
    return response.text


def upload_screenshot_view(path):

    prompt = """From this PDF content, extract key topics with very detailed descriptions for students,Respond ONLY with string JSON in this format: {"topic":"<main>","important_topics":[{"title":"...","description":"..."}]}"""
    text = 'hello'
    raw = extract_text_from_image(path, prompt)
    raw = raw[8:len(raw)-4]
    raw = json.loads(raw)
    print(raw)
    return [raw['topic'],raw['important_topics']]

def get_10_mcqs(path):

    prompt = """From this PDF content,for students generate 10 important MCQs from read_pdf with 4 options each while specifying the correct answer, Respond ONLY with string JSON in this format: {"topic":"<main>","description":"...","mcqs":[{"question":"...","options":["A)","B)","C)","D)"],"answer":"A)..."}]}"""
    text = 'hello'
    raw = extract_text_from_image(path, prompt)
    raw = raw[8:len(raw)-4]
    raw = json.loads(raw)
    print(raw)
    return raw

def read_pdf(path):
	return upload_screenshot_view(path)

def get_mcqs(path):
    return get_10_mcqs(path)

if __name__=="__main__":

	# Topic, SubTopic = read_pdf("C:\\Users\\bss22\\OneDrive\\Desktop\\Don't Open\\BIPIN\\COLLEGE\\CC_mod1.pdf")

    Topic, mcqs = get_mcqs("C:\\Users\\bss22\\OneDrive\\Desktop\\Don't Open\\BIPIN\\COLLEGE\\C# Module 2.pdf")

    #"C:\Users\bss22\OneDrive\Desktop\Don't Open\BIPIN\PHOTOS\DBMS_PRESENT.pdf"
    # JUST PUT THE PATH OF ANY FILE TO UPLOAD IT ,DAMN!!!!
