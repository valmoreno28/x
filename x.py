import streamlit as st
import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import censusdata


fill_in_the_blanks = {'questions': ['question1','question2'], 'answers': ['answer1','answer2']}
ans = []
mark = 0
with st.form(key = id_generator()):
	for i,quest in enumerate(fill_in_the_blanks["questions"]):
		st.write(i+1,quest)
		x = st.text_input("Enter your answer here",key=id_generator())
		ans.append(x)
	submitted = st.form_submit_button(label='Submit')
	if submitted:
		# if answers are correct then
			mark = mark+1
	st.success("Test Score - "+str(mark))
