import streamlit as st
import pickle
import pandas as pd
import base64

def set_bg_hack(main_bg):
     main_bg_ext = "png"

     st.markdown(
          f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
          unsafe_allow_html=True
     )


set_bg_hack('image2.png')





similarity = pickle.load(open('similarity.pkl', 'rb'))


def recommend(movie):
     movie_index = movies[movies['title'] == movie].index[0]
     distance = similarity[movie_index]
     movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

     recommend_movies = []
     for i in movie_list:
          movie_id = movies.iloc[i[0]].movie_id
          recommend_movies.append(movies.iloc[i[0]].title)
     return recommend_movies

movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)



st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
'WHAT ARE YOU LOOKING FOR...?',
movies['title'].values)

if st.button('Recommend'):
     recommendations = recommend(selected_movie_name)
     for i in recommendations:
          st.write(i)
