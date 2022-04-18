import streamlit as st

#Seccion 1: Presentación


st.title("Sexuapp")
st.write("")
st.write("")
st.write("")

	
st.header("¡Hola! Bienvenido (a) Sexuapp")

st.write("")
st.write("")
st.subheader("Historia")
st.write("")
st.write("")
st.subheader("Esta aplicación fue desarrollada por dos estudiantes de posgrado de la Universidad Autónoma de Chihuahua con el fin de ayudar en la orientación de algunas enfermedades de transmisión sexual a través de una serie de preguntas")
st.write("")
st.write("")
st.write("Es corta, segura y anónima. Tu información será cuidadosamente analizada y podrás aprender acerca de las posibles causas de tus síntomas")
st.write("")
st.write("")
st.write("")
st.write("")


#Sección 2: Términos y condiciones

st.subheader("Términos y condiciones")
st.write("")
st.write("")
st.write("Antes de comenzar a usar la aplicación, es necesario que leas los términos y condiciones")



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
	st.write(q1, q2)	

#Tercera sección 
if 'num' not in st.session_state:
	st.session_state.num = 0
choices1 = ['Cisgénero', 'Género no binario', 'Intersexual', 'Gay', 'Lesbiana', 'Transgénero', 'Femenino', 'Masculino', 'Transexual']
choices2 = ['Hombre', 'Mujer']
choices3 = ['No', 'Si']
choices4 = ['No', 'Si']
choices5 = ['Llagas', 'Hinchazón', 'Verrugas', 'Inflamación, Enrojecimiento o irritación (Dentro o fuera de los genitales)']
choices6 = ['Orinar', 'Durante el acto sexual', 'Después de eyacular']
choices7 = ['Pene', 'Testículos', 'No presento este síntoma']
choices8 = ['Si cuento con ardor', 'No cuento con ardor']
choices9 = ['Si', 'No']
choices10 = ['Indoloras', 'Dolorosas', 'No presento este síntoma']
choices11 = ['Desaparecieron solas,' 'Desaparecieron con algun tratamiento', 'No presente llagas']
choices12 = ['Si', 'No', 'No presente llagas']
choices13 = ['Secreción (Pene)', 'Secreción Vagina']
choices14 = ['Sexo Pene-Vagina', 'Sexo Vagina-Vagina', 'Sexo Anal', 'Sexo Oral']
choices15 = ['3 semanas', '2 semanas', '1 mes']


qs1 = [('¿Cuál es tu género?', choices1),
('¿Cual es tu género?', choices1),
('¿Cual es tu género?', choices1)]
qs2 = [('¿Cuál fue tu sexo asignado al nacer?'), choices2),
('sexo biologico', choices2),
('sexo biologico', choices2)]
qs3 = [('¿Haz practicado alguna vez sexo sin metodos anticonceptivos fisicos como el condón?', choices3),
('¿Haz practicado alguna vez sexo sin metodos anticonceptivos fisicos como el condón?', choices3),
('¿Haz practicado alguna vez sexo sin metodos anticonceptivos fisicos como el condón?', choices3)]
qs4 = [('¿Haz practicado sexo sin condón?', choices4),
('¿Haz practicado sexo sin condón?', choices4),
('¿Haz practicado sexo sin condón?', choices4)]
qs5 = [('¿Haz presentado alguno de estos síntomas?', choices5),
('¿Haz presentado alguno de estos síntomas?', choices5),
('¿Haz presentado alguno de estos síntomas?', choices5)]
qs6 = [('¿Haz presentado ardor en el pene?', choices5),
('¿Haz presentado ardor en el pene?', choices5),
('¿Haz presentado ardor en el pene?', choices5)]
qs7 = [('¿Dónde fue la hinchazón?', choices5),
('¿Dónde fue la hinchazón?', choices5),
('¿Dónde fue la hinchazón?', choices5)]
qs8 = [('Haz presentado ardor en los genitales?', choices6),
('¿Haz presentado ardor en los genitales?', choices6),
('¿Haz presentado ardor en los genitales?', choices6)]
qs9 = [('¿Presentas llagas?', choices6),
('¿Presentas llagas?', choices6),
('¿Presentas llagas?', choices6)]
qs10 = [('En caso de presentar llagas, estas son...?', choices6),
('En caso de presentar llagas, estas son...?', choices6),
('En caso de presentar llagas, estas son...?', choices6)]
qs11 = [('En caso de Haber presentado Llagas, estas...?', choices6),
('En caso de Haber presentado llagas, estas...?', choices6),
('En caso de Haber presentado llagas, estas...?', choices6)]
qs12 = [('En caso de haber presentado Llagas, y estas hubiesen desaparecido solas, en un periodo de un año (aproximadamente) después de desaparecer (solas) presentaste síntomas como: Fiebre, Dolor de Garganta o Ganglios linfáticos inflados intermientemente durante este periodo (Despues de la desaparición)?', choices6),
('En caso de haber presentado llagas, y estas hubiesen desaparecido solas, en un periodo de un año (aproximadamente) después de desaparecer (solas) presentaste síntomas como: Fiebre, Dolor de Garganta o Ganglios linfáticos inflados intermientemente durante este periodo (Despues de la desaparición)?', choices6),
('En caso de haber presentado llagas, y estas hubiesen desaparecido solas, en un periodo de un año (aproximadamente) después de desaparecer (solas) presentaste síntomas como: Fiebre, Dolor de Garganta o Ganglios linfáticos inflados intermientemente durante este periodo (Despues de la desaparición)?', choices6)]
qs13 = [('¿Haz presentado algún tipo de secreción inusual en los genitales?', choices7),
('¿Haz presentado algún tipo de secreción inusual en los genitales?', choices7),
('¿Haz presentado algún tipo de secreción inusual en los genitales?', choices7)]
qs14 = [('¿Cómo fue la práctica sexual de la que sospechas pudiste haberte contagiado?', choices7),
('¿Cómo fue la práctica sexual de la que sospechas pudiste haberte contagiado?', choices7),
('¿Cómo fue la práctica sexual de la que sospechas pudiste haberte contagiado?', choices7)]
qs15 = [('¿Cuál consideras fue el lapso entre la relacion sexual sospechosa y la presencia de estos síntomas?', choices7),
('¿Cuál consideras fue el lapso entre la relacion sexual sospechosa y la presencia de estos síntomas?', choices7),
('¿Cuál consideras fue el lapso entre la relacion sexual sospechosa y la presencia de estos síntomas?', choices7)]


def main():
	for _, _, _, _, _, _, _, _, _, _, _, _, _, _, _ in zip(qs1, qs2, qs3, qs4, qs5, qs6, qs7, qs8, qs9, qs10, qs11, qs12, qs13, qs14, qs15):
		placeholder = st.empty()
	num = st.session_state.num
with placeholder.form(key=str(num)):
	st.radio(qs1[num][0], key=num+1, options=qs1[num][1])
	st.radio(qs2[num][0], key=num+1, options=qs2[num][1])
	st.radio(qs3[num][0], key=num+1, options=qs3[num][1])
	st.radio(qs4[num][0], key=num+1, options=qs4[num][1])
	st.radio(qs5[num][0], key=num+1, options=qs5[num][1])
	st.radio(qs6[num][0], key=num+1, options=qs6[num][1])
	st.radio(qs7[num][0], key=num+1, options=qs7[num][1])
	st.radio(qs8[num][0], key=num+1, options=qs8[num][1])
	st.radio(qs9[num][0], key=num+1, options=qs9[num][1])
	st.radio(qs10[num][0], key=num+1, options=qs10[num][1])
	st.radio(qs11[num][0], key=num+1, options=qs11[num][1])
	st.radio(qs12[num][0], key=num+1, options=qs12[num][1])
	st.radio(qs13[num][0], key=num+1, options=qs13[num][1])
	st.radio(qs14[num][0], key=num+1, options=qs14[num][1])
	st.radio(qs15[num][0], key=num+1, options=qs15[num][1])

