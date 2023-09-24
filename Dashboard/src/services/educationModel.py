import openai

# Set your OpenAI API key
api_key = "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"

if not api_key:
    raise ValueError("OpenAI API key not found in environment variables.")

def educationModel(prompt):
    print("Loading...")
    # Initialize the OpenAI API client
    openai.api_key = api_key

    try:
        # Instrucciones
        messages = [
        {"role": "system", "content": "Sabes todo sobre inversiones,finanzas y economia. Vas contestar cualquier tipo de preguntas que sean exclusivamente sobre inversiones, finanzas o economia"},
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