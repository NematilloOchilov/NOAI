
import openai
openai.api_key = 'API_KEY'  # API_KEY ni https://platform.openai.com/ saytidan olasiz


def input_text(text):
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            # {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": text},
            # {"role": "assistant", "content": "Toshkent"},
            # {"role": "user", "content": "2-savol"},
            # {"role": "assistant", "content": "2-javob"},
            # {"role": "user", "content": "3-savol"}
        ]
    ).choices[0].message.content


print(input_text("O'zbekiston poytaxti?"))
