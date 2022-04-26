import streamlit as st
from PIL import Image
image = Image.open('bienvenida.png')


#Seccion 1: Presentación
my_page = st.sidebar.radio("Página de navegación", ["Historia", "Hombres", "Mujeres", "VIH/SIDA" "Referencias bibliográficas"])

if my_page == "Historia":
	st.title("Sexuapp")
	st.write("")
	st.write("")
	st.write("")

	st.header("¡Hola! Esto es Sexuapp")

	st.write("")
	st.write("")
	st.subheader("Historia")
	st.write("")
	st.write("")
	st.write("En Sexuapp estamos felices que nos visites sin importar tu sexo, orientación sexual, género o preferencia sexual, únicamente nos dirigiremos a ti en base a tu sexo asignado al nacer para poder ayudarte con información oportuna para la orientación que te podemos ofrecer en nuestra app.")
	st.write("")
	st.write("")
	st.write("Esta aplicación tiene como objetivo dar un primer acercamiento hacia la información relevante sobre las infecciones de trasmisión sexual (ITS), con una primera orientación hacia algunos de los síntomas que pueden presentarse en las enfermedades de transmisión sexual (Tricomoniasis, Gonorrea, Sífilis, Clamidia, Infección por Virus del Papiloma Humano (VPH), Infección por virus del VIH, Vaginitis bacteriana y  Candidiasis) así como posibles complicaciones y algunos consejos para mantener una vida sexual sana.")
	st.write("")
	st.write("")
	st.write("Se estima que cada año alrededor del mundo adquieren 374 millones de nuevas infecciones de trasmisión sexual (ITS) únicamente de 4 ITS; Tricomoniasis, Gonorrea, Sífilis y Clamidia, por tanto, esto quiere decir que aproximadamente 1 millón de nuevas infecciones son adquiridas por día alrededor del mundo. Además, la mayoría de estas son asintomáticas por lo cual es aún más probable que esta cifra se vea alterada.")
	st.write("")
	st.write("")
	st.write("Según cifras del IMSS (2019), el 30 % de las personas de entre 18 y 30 años de edad en el país han contraído alguna infección de trasmisión sexual al menos una vez en su vida.")
	st.write("")
	st.write("")
	st.write("En el año 2020, en el estado de Chihuahua se reportaba Vulvovaginitis y Candidiasis entre las 20 primeras causas de morbilidad en mujeres en el estado de Chihuahua en la población joven (18-29 años de edad) (INEGI, 2020) fue de aproximadamente de 68 %, del total registrado.")
	st.write("")
	st.write("")
	st.write("La edad joven de chihuahua (18-29 años de edad) según INEGI, (2020) representa aproximadamente el 25% de la población del estado (INEGI, 2021) lo cual resulta de suma importancia ya que aproximadamente el 50 % de las (ITS) nuevas se adquieren antes de los 25 años de edad (Stanford Childrens Health, 2022).")
	st.write("")
	st.write("")
	st.image("https://github.com/valmoreno28/guia/blob/main/bienvenida.png")
	st.write("")
	st.write("")
	st.write("")

if my_page == "Hombres":
	st.title("Hombres")
	st.write("")
	st.write("")
	option = st.selectbox(
	'¿Presentas alguno de estos síntomas?',
	('Llagas', 'Hinchazón', 'Verrugas', 'Irritación, enrojecimiento o ardor'))
	if 'Llagas' in option:
        	st.write('Las llagas son uno de los síntomas característicos de la sífilis, la cual, es una infección bacteriana causada por Treponema pallidum.')
        	st.subheader('Causas de transmisión')
        	st.write('Puedes contagiarte por contacto sexual vaginal, anal u oral con alguna persona infectada; pero también y de forma menos común es mediante el contacto con una lesión activa como las que se podrían presentar en la boca y al darse un beso se transmitiría.') 
        	st.write('También existe la probabilidad de transmisión de madre a hijo durante el embarazo o parto mediante el contacto de las llagas con la piel o membranas mucosas.') 
        	st.warning('Debes saber que no es probable que se contagie mendiante el uso de inodoros, ropa, piscinas, jacuzzis; por mencionar algunos ejemplos.') 
        	st.write('Los síntomas más comunes es la aparición de llagas indoloras en boca, recto o genitales.') 
        	st.write('')
        	st.write('')
        	st.subheader('¿Cuál es el tratamiento adecuado para mí?') 
        	st.write('Es simple. Existen ocasiones en que los contagios pueden curarse con una sola dosis del antibiótico recomendado por tu médico, por lo que en caso de presentar algun sÍntoma, es necesario que acude inmediatamente con tu médico, para evitar complicaciones a largo plazo las cuales pueden dañar gravemente a tus órganos como el corazón o cerebro incluso algunos otros.') 
        	st.write('')
        	st.write('')
        	st.info('POR FAVOR, ¡CHÉCATE!')
	if 'Hinchazón' in option:
        	st.write('La hinchazón en pene o testículos puede considerarse como uno de los síntomas caraterísticos de la Blenorragia o Gonorrea, esta infección de trasmisión sexual que afecta tanto hombres y mujeres causada por la bacteria Neisseria gonorrhoeae y puedes adquirirla por sexo vaginal, anal u oral; así como también puede trasnmitirse por la mamá al bebé durante del parto.') 
        	st.write('Aunque esta infección puede expresarse en varias partes del cuerpo como el recto, ojos, garganta y articulaciones; generalmente se expresa más en los genitales, donde se puede presentar secresión en la punta del pene similar al pus, dolor al orinar o hinchazón en los testículos.') 
        	st.write('')
        	st.write('')
        	st.warning('Entre sus complicaciones puedes presentar infertilidad y afectación en las articulaciones, así como también aumenta la posibilidad de contraer VIH/SIDA.') 
        	st.write('')
        	st.write('')
        	st.subheader('¿Cuál es el tratamiento adecuado para mí?') 
        	st.write('Deberás acudir con tu médico ante síntomas o sospechas de gonorrea y este te asignará un tratamiento adecuado tanto para ti como tu pareja.') 
        	st.write('')
        	st.write('')
        	st.info('POR FAVOR, ¡CHÉCATE!')
	if 'Verrugas' in option:
        	st.write('Cuando presentas verrugas en los genitales existe una causa probable de que estés contagiado con el Virus del Papiloma Humano (VPH).')
        	st.write('Se dice que todas las personas sexualmente activas adquirirán el virus en algún momento de sus vidas.')
        	st.write('Existen causas probables de transmisión como la práctica de sexo vaginal, sexo anal u oral; aunque también se trasnmite por medio de cortaduras, abrasiones y desgarros; además las personas son portadoras del VIH o con alguna alteración en el sistema inmune.') 
        	st.write('La verrugas ocasionadas por este virus se presentan principalmente en los tejidos húmedos de las zonas genitales como el escroto, punta o cuerpo del pene o ano, aunque también se podrían presentar en la boca o garganta de la persona infectada dependiendo del modo de contagio; además que en muchas ocasiones las verrugas son tan pequeñas que no logran ser visibles.') 
        	st.write('Presentan un color carne y apariencia similar a una coliflor.')
        	st.write('También puedes presentar hinchazón, comezón o malestar en el área e incluso sangrado al momento de mantener relaciones sexuales.') 
        	st.write('')
        	st.write('')       
        	st.warning('Las complicaciones a largo plazo es que aumentan la posibilidad de presentar cáncer en pene, boca, ano y garganta,')
        	st.write('')
        	st.write('')
        	st.subheader('¿Cuál es el tratamiento adecuado para mí?') 
        	st.write('Tu médico te recomendará las instrucciones a seguir una vez diagnosticado') 
        	st.info('POR FAVOR, ¡CHÉCATE!')
	if 'Irritación, enrojecimiento o ardor' in option:
        	st.write('Este síntoma se puede debe a varias causas entre las cuales existe la presencia de alguna infección o la portación de microrganismos como el causante de la Trichomoniasis por el parásito Tricomonas vaginallis o la infección por balanianitis causada por contacto con el hongo Candida albicans; ambas presentan enrojecimiento, picazón y sensación de ardor en el pene al orinar o mantener relaciones sexuales.') 
        	st.write('En ambos casos es ocasionado por el contacto sexual vaginal con parejas portadoras de los microoganismos señalados que presentan Candidiasis y Trichomoniasis.') 
        	st.write('')
        	st.write('') 
        	st.subheader('¿Cuál es el tratamiento?') 
        	st.write('En ambos casos necesitarás visitar a tu médico que aplicará el tratamiento correspondiente dependiendo del patógeno.') 
        	st.info('POR FAVOR, CHÉCATE!')

if my_page == "Mujeres":
	st.title("Mujeres")
	st.write("")
	st.write("")
	option = st.selectbox('¿Presentas alguno de estos síntomas?',('Llagas', 'Aumento del flujo vaginal', 'Verrugas', 'Irritación, enrojecimiento o ardor', 'Secreción vaginal', 'Olor fétido'))
	if 'Llagas' in option:
		st.write('Las llagas son uno de los síntomas característicos de la sífilis.') 
		st.write('La Sílifis es una infección bacteriana causada por Treponema pallidum. La principal causa de transmisión es por contacto sexual con alguna persona infectada, ya sea vaginal, anal u oral, pero también y de forma menos comun es mediante el contacto con una lesión activa en la boca, ya que al darse un beso se podría transmitir.') 
		st.write('También existe la probabilidad de transmisión de madre a hijo durante el embarazo o parto. Esto puede ocurrir por medio del contacto de las llagas con la piel o membranas mucosas.')
		st.warning('Es importante que sepas que no es probable que te contagies mediante el uso de inodoros, compartir ropa, pisciinas, jacuzzis; por mencionar algunos ejemplos.') 
		st. write('')
		st. write('')
		st.write('Además de la aparición de llagas en los genitales, también se pueden presesentar llagas indoloras en boca y recto.') 
		st.subheader('¿Cuál es el tratamiento?') 
		st.write('Es simple. Existen ocasiones en que los contagios pueden curarse con una sola dosis del antibiótico recomendado por tu médico.') 
		st. write('')
		st. write('')
		st.warning('En caso de que presentes algun sintoma acude inmenditamente con tu medico a realizar el diagnostico correspondiente, para evitar complicaciones a largo plazo las cuales pueden dañar gravemente a órganos como el corazón o cerebro, incluso algunos otros.')
		st. write('')
		st. write('') 
		st.info('POR FAVOR, ¡CHÉCATE!')
	if 'Aumento del flujo vaginal' in option:
		st.write('El aumento del flujo vaginal puede considerarse como uno de los síntomas caraterísticos de la Blenorragia o también conocida como Gonorrea.') 
		st.write('Esta infección de trasmisión sexual afecta tanto hombres y mujeres y es causada por la bacteria Neisseria gonorrhoeae. Puede ser adquirida tanto por relaciones sexuales vaginales, anales u orales.') 
		st.write('Aunque también puede ser transmitida durante el parto por la madre al bebé.') 
		st.write('Aunque esta infección puede expresarse en varias partes del cuerpo como el recto, ojos, garganta y articulaciones; esta infección se expresa generalmente en los genitales, donde además puedes presentar dolor al orinar, sangrado vaginal después de mantener relaciones sexuales vaginales, dolor abdominal o pélvico.') 
		st. write('')
		st. write('')
		st.warning('Entre sus complicaciones existe la posibilidad de infertilidad, presentar afectaciones en las articulaciones, y aumenta la posibilidad de contraer VIH/SIDA.')
		st. write('')
		st. write('') 
		st.subheader('¿Cuál es el tratamiento?') 
		st.write('Deberás acudir con tu médico ante síntomas o sospechas de gonorrea y este te asignará el tratamiento adecuado tanto para ti como tu pareja.') 
		st. write('')
		st. write('')
		st.info('¡POR FAVOR, CHECATE!')
	if 'Verrugas' in option:
		st.write('Cuando se presentan verrugas en los genitales existe una causa probable de que se deba al Virus del Papiloma Humano (VPH).') 
		st.write('Se dice que todas las personas sexualmente activas adquirirán el virus en algún momento de sus vidas. Existen causas probables de transmisión como la práctica de relaciones sexuales vaginales, anales u orales.') 
		st.write('Aunque también se puede transmitir por medio de cortaduras, abrasiones y desgarros.')
		st. write('')
		st. write('') 
		st. warning('Es importante que sepas que las personas que son portadoras del VIH o con alguna alteración en el sistema inmune son aun mas propensas.') 
		st. write('')
		st. write('')
		st.write('La verrugas ocasionadas por este virus se presentan principalmente en los tejidos húmedos de las zonas genitales o ano aunque también se pueden presentar en la boca o garganta de la persona infectada dependiendo del modo de contagio, presentan un color carne y apariencia similar a una coliflor.') 
		st.write('También se puede presentar hinchazón, comezón o malestar en el área; así como sangrado al momento de mantener relaciones sexuales, ademas en muchas ocasiones las verrugas son tan pequeñas que no logran ser visibles.') 
		st. write('')
		st. write('')
		st.warning('Las complicaciones a largo plazo es que aumenta la posibilidad de presentar cancer de cuello uterino, boca, ano y garganta.') 
		st. write('')
		st. write('')
		st.subheader('¿Cuál es el tratamiento?') 
		st.write('Tu médico te recomendará las instrucciones a seguir una vez que hayas sigo correctamente diagnosticada.')
		st. write('')
		st. write('')
		st.info('POR FAVOR, ¡CHÉCATE!')
	if 'Irritación, enrojecimiento o ardor' in option:
		st.write('Este síntoma puede deberse a varias causas como Trichomoniasis ocasionada por el parásito patógeno Tricomonas vaginallis o candidiasis causada por contacto con hongos vaginales como Candida albicans.') 
		st.write('Ambas enfermedades ocasionan síntomas como enrojecimiento, picazón y sensación de ardor en los genitales al orinar o mantener relaciones sexuales. En ambos casos este es ocasionado por el contacto sexual vaginal con parejas portadoras de estos microorganismos.') 
		st.subheader('¿Cuál es el tratamiento?') 
		st.write('En ambos casos necesitarás visitar a tu médico el cual aplicará las pruebas de diagnóstico adecuadas y en caso de confirmar, se necesitará aplicar el tratamiento correspondiente dependiendo de la infección.') 
		st.info('POR FAVOR, ¡CHÉCATE!')
	if 'Secreción vaginal' in option:
		st.write('Existen fluidos vaginales que no son comunes tener y que pueden estar relacionados con alguna enfermedad de transmisión sexual.  Estos pueden ser fluidos de colores como gris, amarillo o verde y es caracteristico de la tricomoniasis o vaginitis bacteriana') 
		st.write('También puede ser una secreción espesa, blanca e inolora parecida al queso cotagge que es parte de los síntomas relacionados con la candidiasis.') 
		st.write('Estas infecciones son ocasionadas por distintos microrganismos patógenos y en la mayoría de los casos estas son ocasionados por el contacto sexual vaginal con parejas portadoras de los agentes causantes de las mismas.') 
		st. write('')
		st. write('')
		st.subheader('¿Cuál es el tratamiento?') 
		st.write('En estos casos necesitarás visitar a tu médico el cual aplicará las pruebas de diagnóstico correctas y en caso de confirmar se aplicará el tratamiento correspondiente dependiendo de la enfermedad.') 
		st.info('POR FAVOR, ¡CHÉCATE!')
	if 'Olor fétido' in option:
		st.write('El olor fétido a "pescado", es uno de los síntomas mas comunes de las vaginitis bacteriana.')
		st.write('Estas infecciones son ocasionadas principalmente por un desequilibrio en la población bacteriana de la vagina.') 
		st.write('Además de este síntoma, también es posible que presentes comezón, ardor o secreción de color gris, blanca o verde en tu zona íntima.') 
		st. write('')
		st. write('')
		st.warning('Si no es tratada correctamente la vaginitis bacteriana puede ocasionar complicaciones durante el embarazo, enfermedad inflamatoria pélvica o aumentar la posibilidad de contraer otras enfermedades de transmisión sexual.') 
		st. write('')
		st. write('')
		st.subheader('¿Cuál es el tratamiento?') 
		st. write('Deberás acudir al médico a que te aplique las herramientas de diagnóstico adecuadas y él te indicará al tratamiento correcto para ti.')
		st. write('')
		st. write('')
		st.info('POR FAVOR, ¡CHÉCATE!')


if my_page == "VIH/SIDA":
	st.title("VIH/SIDA")
	st.write("")
	st.write("")
    

if my_page == "Referencias bibliográficas":
    st.title("Referencias bibliográficas")
    st.write("")
    st.write("")
    st.write("🔹En línea, consultado el 05 de abril del 2022:")
    st.write("https://www.stanfordchildrens.org/es/topic/default?id=enfermedadesdetransmisinsexual-90-P04757#:~:text=Las%20enfermedades%20de%20transmisi%C3%B3n%20sexual%20(ETS)%20son%20enfermedades%20infecciosas%20transmitidas,entre%2015%20y%2024%20a%C3%B1os")
    st.write("")
    st.write("🔹En línea, consultado el 07 de abril del 2022:")
    st.write("https://www.who.int/news-room/fact-sheets/detail/sexually-transmitted-infections-(stis)")
    st.write("")
    st.write("🔹En línea, consultado el 10 de abril del 2022:")
    st.write("https://www.mayoclinic.org/es-es/diseases-conditions/trichomoniasis/symptoms-causes/syc-20378609#:~:text=Descripci%C3%B3n%20general,lo%20general%20no%20tienen%20s%C3%ADntomas")
    st.write("")
    st.write("🔹En línea, consultado el 10 de abril del 2022:")
    st.write("https://www.mayoclinic.org/es-es/diseases-conditions/chlamydia/symptoms-causes/syc-20355349")
    st.write("")
    st.write("🔹En línea, consultado el 10 de abril del 2022:")
    st.write("https://www.mayoclinic.org/es-es/diseases-conditions/syphilis/symptoms-causes/syc-20351756")
    st.write("")
    st.write("🔹En línea, consultado el 10 de abril del 2022:")
    st.write("https://www.mayoclinic.org/es-es/diseases-conditions/gonorrhea/symptoms-causes/syc-20351774")
    st.write("")
    st.write("🔹En línea, consultado el 10 de abril del 2022:")
    st.write("https://www.mayoclinic.org/es-es/diseases-conditions/hpv-infection/symptoms-causes/syc-20351596")
    st.write("")
    st.write("🔹En línea, consultado el 10 de abril del 2022:")
    st.write("https://www.mayoclinic.org/es-es/diseases-conditions/genital-warts/symptoms-causes/syc-20355234")
    st.write("")
    st.write("🔹En línea, consultado el 15 de abril del 2022:    ")
    st.write("https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2021/EstSociodemo/ResultCenso2020_Chih.pdf")
    st.write("")
    st.write("🔹En línea, consultado el 15 de abril del 2022: ")
    st.write("https://epidemiologia.salud.gob.mx/anuario/20200/principales/estatal_grupo/chih.pdf")
    st.write("")
    st.write("🔹En línea, consultado el 15 de abril del 2022: ")
    st.write("https://epidemiologia.salud.gob.mx/anuario/html/morbilidad_estatal.html")
    st.write("")
    st.write("🔹En línea, consultado el 15 de abril del 2022: ")
    st.write("https://www.mayoclinic.org/es-es/diseases-conditions/bacterial-vaginosis/symptoms-causes/syc-20352279")
    st.write("")
    st.write("En línea, consultado el 15 de abril del 2022: ")
    st.write("https://www.mayoclinic.org/es-es/diseases-conditions/yeast-infection/symptoms-causes/syc-20378999")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
