#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install tiktoken openai')


# In[3]:


import difflib
import tiktoken
import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# List of words to use for auto-correction
word_list = ['apple', 'banana', 'orange', 'grape', 'mango']

# Function to tokenize text
def tokenize_text(text):
    return tiktoken.Tokenizer().tokenize(text)

# Function to perform auto-correction
def auto_correct(word):
    closest_match = difflib.get_close_matches(word, word_list, n=1)
    if closest_match:
        return closest_match[0]
    else:
        return "No suggestion found."

# Function to generate auto-correction using GPT-3.5
def generate_correction(text):
    prompt = f"Auto-correct the following text: \"{text}\""

    # Tokenize the prompt
    tokens = tokenize_text(prompt)

    # Generate completion
    completion = openai.Completion.create(
        engine='text-davinci-003',
        prompt=tokens,
        max_tokens=20,
        n=1,
        stop=None,
        temperature=0.7
    )

    # Extract the generated text
    generated_text = completion.choices[0].text.strip()

    # Process the generated text
    processed_text = generated_text.split('\"')[1].strip()

    return processed_text

# Test the auto-correct tool
input_word = input("Enter a word: ")
correction = auto_correct(input_word)

if correction == "No suggestion found.":
    gpt_correction = generate_correction(input_word)
    print("Auto-correct suggestion (GPT-3.5):", gpt_correction)
else:
    print("Auto-correct suggestion:", correction)


# In[ ]:




