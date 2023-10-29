import os
from PyPDF2 import PdfReader
import re
from litellm import completion
import numpy as np
import tensorflow_hub as hub
from sklearn.neighbors import NearestNeighbors



recommender = None


def preprocess(text):
    text = text.replace('\n', ' ')
    text = re.sub('\s+', ' ', text)
    return text


def text_to_chunks(texts, word_length=150, start_page=1):
    text_toks = [t.split(' ') for t in texts]
    chunks = []

    for idx, words in enumerate(text_toks):
        for i in range(0, len(words), word_length):
            chunk = words[i: i + word_length]
            if (
                (i + word_length) > len(words)
                and (len(chunk) < word_length)
                and (len(text_toks) != (idx + 1))
            ):
                text_toks[idx + 1] = chunk + text_toks[idx + 1]
                continue
            chunk = ' '.join(chunk).strip()
            chunk = f'[Page no. {idx+start_page}]' + ' ' + '"' + chunk + '"'
            chunks.append(chunk)
    return chunks


class SemanticSearch:
    def __init__(self):
        self.use = hub.load('https://tfhub.dev/google/universal-sentence-encoder/4')
        self.fitted = False

    def fit(self, data, batch=1000, n_neighbors=5):
        self.data = data
        self.embeddings = self.get_text_embedding(data, batch=batch)
        n_neighbors = min(n_neighbors, len(self.embeddings))
        self.nn = NearestNeighbors(n_neighbors=n_neighbors)
        self.nn.fit(self.embeddings)
        self.fitted = True

    def __call__(self, text, return_data=True):
        inp_emb = self.use([text])
        neighbors = self.nn.kneighbors(inp_emb, return_distance=False)[0]

        if return_data:
            return [self.data[i] for i in neighbors]
        else:
            return neighbors

    def get_text_embedding(self, texts, batch=1000):
        embeddings = []
        for i in range(0, len(texts), batch):
            text_batch = texts[i: (i + batch)]
            emb_batch = self.use(text_batch)
            embeddings.append(emb_batch)
        embeddings = np.vstack(embeddings)
        return embeddings


def load_recommender(texts):
    global recommender
    if recommender is None:
        recommender = SemanticSearch()

    chunks = text_to_chunks(texts)
    recommender.fit(chunks)
    return 'text Loaded.'


def generate_text(openAI_key, prompt, engine="text-davinci-003"):
    try:
        messages = [{"content": prompt, "role": "user"}]
        completions = completion(
            model=engine,
            messages=messages,
            max_tokens=512,
            n=1,
            stop=None,
            temperature=0.7,
            api_key=openAI_key
        )
        message = completions['choices'][0]['message']['content']
    except Exception as e:
        message = f'API Error: {str(e)}'
    return message


def generate_answer(question, openAI_key):
    topn_chunks = recommender(question)
    prompt = ""
    prompt += 'search results:\n\n'
    for c in topn_chunks:
        prompt += c + '\n\n'

    prompt += (
        "Instructions: Compose a comprehensive reply to the query using the search results given. "
        "Cite each reference using [ Page Number] notation (every result has this number at the beginning). "
        "Citation should be done at the end of each sentence. If the search results mention multiple subjects "
        "with the same name, create separate answers for each. Only include information found in the results and "
        "don't add any additional information. Make sure the answer is correct and don't output false content. "
        "If the text does not relate to the query, simply state 'Text Not Found in PDF'. Ignore outlier "
        "search results which have nothing to do with the question. Only answer what is asked. The "
        "answer should be short and concise. Answer step-by-step. \n\nQuery: {question}\nAnswer: "
    )

    prompt += f"Query: {question}\nAnswer:"
    answer = generate_text(openAI_key, prompt, "text-davinci-003")
    return answer


def load_openai_key() -> str:
    key = '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'
    if key is None:
        raise ValueError(
            "[ERROR]: Please pass your OPENAI_API_KEY. Get your key here: https://platform.openai.com/account/api-keys"
        )
    return key


def getAnsFromQuestions(pdf_text, user_question):
    text = preprocess(pdf_text)
    load_recommender(text)
    openAI_key = load_openai_key()
    return generate_answer(user_question, openAI_key)







