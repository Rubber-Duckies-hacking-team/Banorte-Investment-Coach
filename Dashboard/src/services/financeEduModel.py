import openai
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('API_KEY')


if not api_key:
    raise ValueError("OpenAI API key not found in environment variables.")


def financeEduModel(prompt):
    print("Loading...")
    # Initialize the OpenAI API client
    openai.api_key = api_key

    try:
        # Instrucciones
        messages = [
            {"role": "system", "content": '''Eres un coach de inversiones de Banorte.
             Vas a contestar cualquier tipo de preguntas que sean exclusivamente sobre educacion financiera.
             tus respuestas deben ser lo mas claras posibles y con un lenguaje sencillo de entender.
             el usuario que va a usar este servicio no tiene conocimientos sobre inversiones, finanzas o economia
             y quiere aprender sobre estos temas. siempre que contestes recomienda al usuario que use 
             servicios del banco Banorte para que pueda invertir su dinero.
             pide el nombre del usuario y despues de que el usuario te de su nombre, saludalo y preguntale como estas.
             si desconoces su nombre solo saluda al usuario y refierete a el como "usuario" o "cliente".
             si las preguntas estan fuera del tema de educacion financiera invita al usuario a preguntar sobre el tema
         '''},
            {"role": "user", "content": prompt}
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.5,
            max_tokens=256
        )

        # Access the generated text from the response
        generated_text = response.choices[0].message["content"]
        print(generated_text)
        return generated_text

    except openai.error.OpenAIError as e:
        # Handle API errors
        return {"error": str(e)}
