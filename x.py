import streamlit as st

#Seccion 1: Presentación


st.title("Sexuapp")
st.write("")
st.write("")
st.write("")

	
st.write(("¡Hola! Bienvenido (a) Sexuapp"), cliked.st.session_state["button"] = button2)

st.write("")
st.write("")
st.subheader("Esta aplicación ayuda en la orientación de algunas enfermedades de transmisión sexual a través de una serie de preguntas")
st.write("")
st.write("")
st.write("Es corta, segura y anónima. Tu información será cuidadosamente analizada y podrás aprender acerca de las posibles causas de tus síntomas")
st.write("")
st.write("")


#Sección 2: Términos y condiciones

st.subheader("Términos de condiciones")
st.write("")
st.write("")
st.write("Antes de comenzar a usar la aplicación, es necesario que leas los términos de condiciones")



st.write("•La encuesta no es un diagnóstico médico. Su función es informar y orientar a la comunidad sobre algunas enfermedades de transmisión sexual.")
st.write("•No lo uses en emergencias. En caso de emergencias médicas, es mejor acudir directamente a una revisión médica.")
st.write("•Tus datos están seguros. La información que tu brindes será anónima y no será compartida con nadie más.")
st.write("")
st.write("")

st.caption("Al dar click en el botón de siguiente aceptas términos y condiciones.")


button2= st.button("Atrás")
	
if st.session_state.get("button") != True:
   st.session_state["button"] = button2
if st.session_state["button"] == True:

    st.write("")
    st.session_state["button"] = False
    st.write("Lamentamos que no quisieras participar en nuestra app. Muchas gracias por visitarnos.")
 st.stop()

with st.form("my_form"):
 	submitted = st.form_submit_button("Siguiente")  
   	if submitted:
   	

#Tercera sección 

    	st.write("¿Cuál es tu género?")
    	genero = st.selectbox("Selecciona una opción", ["Hombre", "Mujer", "Prefiero no decirlo"])
        
        
if genero:
	st.write("¿Cuál es tu sexo biológico?")
sexo = st.selectbox("Selecciona una opción", ["Hombre", "Mujer"])
	#genero != True
 	#st.session_state("selectbox") != True:
 	#st.session_state("selectbox") = genero
