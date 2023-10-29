from rest_framework.response import Response
from .models import Question
from .getAnsFromQuestions import getAnsFromQuestions
from django.http import JsonResponse
from django.core.files.uploadedfile import InMemoryUploadedFile
import PyPDF2
import io
import speech_recognition as sr




def convert_audio_to_text(audio_data):
    recognizer = sr.Recognizer()

    try:
        # Recognize the audio and convert it to text
        text = recognizer.recognize_google(audio_data)  # You can choose a different recognizer (e.g., 'sphinx') if needed
        return text
    except sr.UnknownValueError:
        return "Speech Recognition could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results from Google Web Speech API; {e}"



def getQuestionAnswer(request):
    try:
        pdf_file = request.FILES.get('pdf_file', None)
        question = request.POST.get('question', None)
        audio = request.FILES.get('audio', None)  # Use get to handle missing 'audio' case

        if question is not None:
            pdf_filename = pdf_file.name if pdf_file is not None else "empty"
            audio_filename = audio.name if audio is not None else "empty"

            if pdf_file is not None:
                pdf_content = pdf_file.read()  # Read the PDF content from the uploaded file
                pdf_reader =PyPDF2.PdfReader(io.BytesIO(pdf_content))  # Use io.BytesIO
                text = ''

                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text()
                response = getAnsFromQuestions(text, question)
                ans = Question.objects.create(
                    pdf_file=pdf_filename, 
                    audio=audio_filename,
                    questions=question,
                    answers=response
                )
                ans.save()
                return JsonResponse({'response': response}, safe=False, status=200)
            elif audio is not None and isinstance(audio, InMemoryUploadedFile):  # Handle the 'audio' case properly
                audio_content = audio.read()
                question = convert_audio_to_text(audio_content)

                if question is not None:
                    response = getAnsFromQuestions(pdf_file, question)  # Pass pdf_file, as before
                    ans = Question.objects.create(
                        pdf_file=pdf_filename, 
                        audio=audio_filename,
                        questions=question,
                        answers=response
                    )
                    ans.save()
                    return JsonResponse({'response': response}, safe=False, status=200)
                else:
                    return JsonResponse({'message': 'Error converting audio to text'}, status=400)
            else:
                return JsonResponse({'message': 'Missing field or invalid audio file'}, status=400)
        elif pdf_file:
            return JsonResponse({'message': 'Missing question field'}, status=400)
        elif question:
            return JsonResponse({'message': 'Missing pdf_file field'}, status=400)
        else:
            return JsonResponse({'message': 'Missing data fields'}, status=400)
    except Exception as error:
        return JsonResponse({'message': str(error)}, status=400)







def get_question(request, pk):
    try:
        # Retrieve the question with the specified ID
        question = Question.objects.get(pk=pk)
        
        
        if question.pdf_file:  # Check if pdf_file is not None
                pdf_url = question.pdf_file.url
        else:
            pdf_url = None
            
        if question.audio:  # Check if pdf_file is not None
                audio = question.audio.url
        else:
            audio = None
            
        if question is not None:
        # Convert the question data to a dictionary
            question_detail = {
                'pdf_file': pdf_url,
                'questions': question.questions,
                'answers': question.answers,
                'audio':audio
            }

            return JsonResponse(question_detail,safe=False,status=200)
        else:
            return JsonResponse({'message':'This chat doesnot exit'},status=404)
    except Exception as error:
        return JsonResponse({'message': str(error)}, status=404)



def getAllQuestion(request):
    try:
        # Retrieve all questions
        all_questions = Question.objects.all()

        # Create a list to store question details
        all_question_details = []
        for question in all_questions:
            if question.pdf_file:  # Check if pdf_file is not None
                pdf_url = question.pdf_file.url
            else:
                pdf_url = None
            if question.audio:  # Check if pdf_file is not None
                audio = question.audio.url
            else:
                audio = None

            all_question_details.append({
                'id': question.id,
                'pdf_file': pdf_url,
                'audio':audio,
                'questions': question.questions,
                'answers': question.answers,
            })
        return JsonResponse(all_question_details, safe=False , status=200)  # Use status=200 for a successful response
    except Exception as error:
        return JsonResponse({'message': str(error)}, status=404)


# def getQuestionAnswer(request):
#     try:
#         pdf_file = request.FILES.get('pdf_file', None)
#         question = request.POST.get('question', None)
#         audio = request.FILES.get('audio', None)  # Use get to handle missing 'audio' case

#         if question is not None:
#             if pdf_file is not None:
#                 pdf_content = pdf_file.read()  # Read the PDF content from the uploaded file
#                 pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_content))  # Use io.BytesIO
#                 text = ''

#                 for page_num in range(len(pdf_reader.pages)):
#                     page = pdf_reader.pages[page_num]
#                     text += page.extract_text()
#                 response = getAnsFromQuestions(text, question)
#                 ans = Question.objects.create(
#                     pdf_file=pdf_file.name, 
#                     audio=audio.name if audio.name is not None else "empty",    # Save the file name, not the file content
#                     questions=question,
#                     answers=response
#                 )
#                 ans.save()
#                 return JsonResponse({'response': response}, safe=False, status=200)
#             elif audio is not None and isinstance(audio, InMemoryUploadedFile):  # Handle the 'audio' case properly
#                 audio_content = audio.read()
#                 question = convert_audio_to_text(audio_content)

#                 if question is not None:
#                     response = getAnsFromQuestions(pdf_file, question)  # Pass pdf_file, as before
#                     ans = Question.objects.create(
#                         pdf_file=pdf_file.name, 
#                         audio=audio.name if audio.name is not None else "empty",# Save the file name, not the file content
#                         questions=question,
#                         answers=response
#                     )
#                     ans.save()
#                     return JsonResponse({'response': response}, safe=False, status=200)
#                 else:
#                     return JsonResponse({'message': 'Error converting audio to text'}, status=400)
#             else:
#                 return JsonResponse({'message': 'Missing field or invalid audio file'}, status=400)
#         elif pdf_file:
#             return JsonResponse({'message': 'Missing question field'}, status=400)
#         elif question:
#             return JsonResponse({'message': 'Missing pdf_file field'}, status=400)
#         else:
#             return JsonResponse({'message': 'Missing data fields'}, status=400)
#     except Exception as error:
#         return JsonResponse({'message': str(error)}, status=400)












# def convert_audio_to_text(audio):
#     try:
#         # Define the whisper command and arguments
#         command = ["whisper", audio, "--model", "medium.en"]

#         # Execute the whisper command
#         result = subprocess.run(command, capture_output=True, text=True, check=True)

#         # Get the standard output (result of the whisper command)
#         output = result.stdout

#         # Process the output as needed (e.g., return it or save it to a file)
#         return output
#     except subprocess.CalledProcessError as e:
#         # Handle any errors or exceptions that occur when running the command
#         error_message = e.stderr.decode()
#         return f"Error: {error_message}"