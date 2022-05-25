from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np

model = load_model('model_12')

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions_label = predictions_df['Label'][0]
    predictions_score   = predictions_df['Score'][0]
    return predictions_label,predictions_score

def run():

    from PIL import Image
    st.set_page_config(layout="wide") 
    
   

    st.markdown("""
<style>
.big-font {
    font-size:14px !important;
}
</style>
""", unsafe_allow_html=True)

    st.markdown('<p class="big-font"><b>ПРЕДУПРЕЖДЕНИЕ! Данный калькулятор не предоставляет Медицинских Рекомендаций.</b> </p>', unsafe_allow_html=True)
    st.markdown('<p class="big-font">ХОТЯ НЕКОТОРЫЕ МАТЕРИАЛЫ МОГУТ ПРЕДОСТАВЛЯТЬСЯ ОТДЕЛЬНЫМИ МЕДИЦИНСКИМИ РАБОТНИКАМИ, ВЫ ПРИЗНАЕТЕ, ЧТО ПРЕДОСТАВЛЕНИЕ ТАКОГО КОНТЕНТА НЕ СОЗДАЕТ ОТНОШЕНИЙ МЕЖДУ МЕДИЦИНСКИМ РАБОТНИКОМ И ПАЦИЕНТОМ И НЕ ПРЕДСТАВЛЯЕТ СОБОЙ МНЕНИЕ, МЕДИЦИНСКУЮ КОНСУЛЬТАЦИЮ, ПРОФЕССИОНАЛЬНЫЙ ДИАГНОЗ, УСЛУГУ ИЛИ ЛЕЧЕНИЕ КАКОГО-ЛИБО ЗАБОЛЕВАНИЯ', unsafe_allow_html=True)
    
    st.markdown('<p class="big-font">Доступ к общей информации предоставляется только в образовательных целях через этот сайт и ссылки на другие сайты. Контент не рекомендуется и не одобрен каким-либо врачом или поставщиком медицинских услуг. Предоставленная информация и контент не заменяют медицинскую или профессиональную помощь, и вы не должны использовать информацию вместо посещения, звонка, консультации или консультации вашего врача или другого поставщика медицинских услуг. Вы несете ответственность или несете ответственность за любые рекомендации, курс лечения, диагностику или любую другую информацию, услуги или продукт, полученные через этот сайт</p>', unsafe_allow_html=True)
        
    image = Image.open('main_logo.jpg')
    
    
    image_hospital = Image.open('Glavnij-klinicheskij_web.jpg')
    
    
    col1, col2, col3 = st.columns([3,8,1])

    with col1:
        st.write("     ")

    with col2:
        st.image(image,use_column_width=False)

    with col3:
        st.write("")
   

    add_selectbox = st.sidebar.selectbox(
    "Какой Прогноз Вы хотите?",
    ("Online", "Пакет (файл)"))

    st.sidebar.info('Калькулятор прогнозирование летального исхода у пациентов с COVID-19')
    st.sidebar.success('http://www.almazovcentre.ru/')
    
    st.sidebar.image(image_hospital)
    st.sidebar.success('©  Igor Korsakov, PhD')
    
    st.title("Калькулятор прогнозирование летального исхода у пациентов с COVID-19")
    
    
#['Возраст', 'Процент поражения легочной ткани', 'Хронические заболевания сердечно-сосудистой системы', 'PLT- Тромбоциты', 'С-реактивный 
# белок (СРБ)', 'Пульсоксиметрия число', 'ЧДД число', 'ЧСС', 'Креатинин', 'Мочевина', 'Общий белок']
    if add_selectbox == 'Online':

        age = st.number_input('Возраст ', min_value=1, max_value=100, value=76)
        lung = st.number_input('Процент поражения легочной ткани (0-100%)', min_value=0, max_value=100, value=20)
        cvd = st.checkbox('ССЗ')
        if cvd:
            cvd_ = '1'
        else:
            cvd_ = '0'
            
            
        #sex = st.selectbox('Sex', ['male', 'female'])
        
        dimer = st.number_input('Тромбоциты    [150-400] (10 в ст. 9/л)', min_value=0, max_value=1000, value=255)
        
        crb = st.number_input('С-реактивный белок (СРБ) [0 - 5] (мг/л)', min_value=0, max_value=150, value=116)
        
        oxigen = st.number_input('Пульсоксиметрия число ( 0 - 100)', min_value=0, max_value=100, value=93)
        
       # fibrinogen = st.number_input('Фибриноген ( 1,8 - 3,5 г/л)', min_value=0, max_value=100, value=6)
        
        raspiratory_rate = st.number_input('ЧДД  ( 0 - 100)', min_value=0, max_value=100, value=25)
        
        heart_rate = st.number_input('ЧСС ( 0 - 250)', min_value=0, max_value=250, value=78)
        
        сreatinine = st.number_input('Креатинин ( 0 - 250) (мкмоль/л)', min_value=0, max_value=250, value=50)
        
        urea = st.number_input('Мочевина (2,5—8,32) (ммоль/л)', min_value=0, max_value=100, value=2)
        
        protein = st.number_input('Общий белок ( 1 - 50) (г/л)', min_value=1, max_value=50, value=7)
        
        #children = st.selectbox('Children', [0,1,2,3,4,5,6,7,8,9,10])
        
        #if st.checkbox('Smoker'):
#            smoker = 'yes'
#        else:
#            smoker = 'no'
#        region = st.selectbox('Region', ['southwest', 'northwest', 'northeast', 'southeast'])

        output=""

        
        
        input_dict = {'Возраст' : age, 
                      'Процент поражения легочной ткани' : lung, 
                      'ССЗ' : cvd_ ,
                      'Тромбоциты' : dimer, 
                      'СРБ' : crb, 
                      'Пульсоксиметрия' : oxigen,
                      #'Фибриноген' : fibrinogen,
                      'ЧДД' : raspiratory_rate,
                      'ЧСС' :  heart_rate,
                      'Креатинин' : сreatinine,
                      'Мочевина' : urea,
                      'Общий белок' : protein                   
                                         
                         }
        
        
        
        input_df = pd.DataFrame([input_dict])

        if st.button("Прогноз"):
            output_label,output_val = predict(model=model, input_df=input_df)
            
            if (output_label ==1):
                output = str(output_val)+' %'
                out = output_val
            else:
                output = str((1 - output_val).round(2))+' %'
                out = 1 - output_val
                
                
            if (out > 0.5):
                code = '  (высокий риск)'
            elif (out < 0.2):
                code = '  (низкий риск)'
            else:
                code = '  средний риск'
            output = output+code
            
            
        st.success('Вероятность летального исхода  {}'.format(output))

    if add_selectbox == 'Пакет (файл)':

        file_upload = st.file_uploader("Загрузите csv файл для прогноза", type=["csv"])

        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)

if __name__ == '__main__':
    run()
