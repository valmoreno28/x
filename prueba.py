import streamit as st


def main():
	for _,  _, _ in zip(qs2, qs3, qs4):
		placeholder = st.empty()
	num = st.session_state.num
with placeholder.form(key=str(num)):
	st.radio(qs1[num][0], key=num+1, options=qs1[num][1])
	st.radio(qs2[num][0], key=num+1, options=qs2[num][1])
	st.radio(qs3[num][0], key=num+1, options=qs3[num][1])


qs2 = [('¿Cual fue tu sexo asignado al nacer?', choices2),
('sexo biologico', choices2),
('sexo biologico', choices2)]
choices2 = [('Hombre', suma = 0), ('Mujer', suma= suma + 2)]

qs3 = [('¿Haz practicado alguna vez sexo sin metodos anticonceptivos fisicos como el condón?', choices3),
('¿Haz practicado alguna vez sexo sin metodos anticonceptivos fisicos como el condón?', choices3),
('¿Haz practicado alguna vez sexo sin metodos anticonceptivos fisicos como el condón?', choices3)]
choices3 = [({'No'}, suma1 = 0), ({'Si'}, suma1 = suma1 + 2)]

qs4 = [('¿Haz practicado sexo sin condón?', choices4),
('¿Haz practicado sexo sin condón?', choices4),
('¿Haz practicado sexo sin condón?', choices4)]
choices4 = [({'No'}, suma2 = 0), ({'Si'}, suma2 = suma1 + 2)]

	
	
