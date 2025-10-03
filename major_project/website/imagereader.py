
from google import genai

client = genai.Client(api_key="AIzaSyAx8_0F9dpyGa1RXNnpBEaKdI9-1Y6dDD8")


def extract_text_from_image(path, prompt):

    my_file = client.files.upload(file=path)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[my_file, prompt],
    )
    return response.text


def upload_screenshot_view(path):

    text = extract_text_from_image(path, "Respond Interactively, Explain and Solve or recognise the problem and give me the final answer using normal math symbols(√, π, ∫, etc.) in plain text, without LaTeX code, bold letters or \\boxed{} formatting .")
    print(text)
    return text


def read_image(path):
	return upload_screenshot_view(path)


if __name__=="__main__":
	read_image("C:\\Users\\bss22\\OneDrive\\Desktop\\Don't Open\\BIPIN\\PHOTOS\\Screenshot 2024-02-25 234513.png")
    #"C:\Users\bss22\OneDrive\Desktop\Don't Open\BIPIN\PHOTOS\DBMS_PRESENT.pdf"
    # JUST PUT THE PATH OF ANY FILE TO UPLOAD IT ,DAMN!!!!

