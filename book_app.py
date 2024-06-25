import streamlit as st
import google.generativeai as genai
st.title('story generator')
key = 'AIzaSyDAyD9PD1_fn0SJ9QN-e2-7OdhebIzbL3w'
genai.configure(api_key=key)
system_instructions = """ 
You are a book writer and you must provide a short story within 1000 words based on what a user asks from you.
"""
model = genai.GenerativeModel(model_name='gemini-1.5-flash-latest',
                              system_instruction=system_instructions)

prompt = st.text_area('specify the type of the story to be generated')

if st.button('generate story'):
    response = model.generate_content(prompt)
    st.write(response.text)
    st.download_button("Download", response.text)


