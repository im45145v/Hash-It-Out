import requests
import geocoder

API_KEY="ab8609a877cd4f91b6269e7f768127a6"
# replace with your API token
base_url = "https://api.assemblyai.com/v2"

def get_coords(address):
    g = geocoder.bing(address, key='Aowcdh3tB--xi-HGt95MZr7jCFWqDenSzKp0yDtC2AgfH_HstHkEBY2XkFgw9XW9')
    return [g.json['lat'], g.json['lng']]

def get_address(transcription_id):
    answer = question(transcription_id, q_format("Extract the full address or location mentioned in the transcript ", "One line"))
    address = answer["response"][0]["answer"]
    return address

def q_format(prompt, format):
    questions = [
    
    {
        "question": f"{prompt}",
        "answer_format": f'''{format}
        '''
    }
]
    return questions

def post_lemur(api_token, transcript_ids, questions=None, type='qa', data={}):
    if type=='qa':
        url = "https://api.assemblyai.com/lemur/v3/generate/question-answer"
    else:
        url = "https://api.assemblyai.com/lemur/v3/generate/summary"

    headers = {
        "authorization": api_token
    }
    if not questions and not data:
        data = {
        "transcript_ids": transcript_ids,
        "model": "basic"
    }   
    else:

        data = {
            "transcript_ids": transcript_ids,
            "questions": questions,
            "model": "basic"
        }

    response = requests.post(url, json=data, headers=headers)
    return response
def question(transcript_id,question):
    lemur_output = post_lemur(API_KEY, [transcript_id], question)
    lemur_response = lemur_output.json()

    if "error" in lemur_response:
        print(f"Error: { lemur_response['error'] }")
    else:
        return(lemur_response)

