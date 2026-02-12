import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy
import pandas
from datetime import time,datetime


st.title('My first app')
st.write('There is a science.')

# st.write(pandas.DataFrame({
#     'first_colomn':[1,2,3,4],
#     'second_colomn':[5,6,7,8]
# }))

# python3自带魔术方法，所以可以省略write方法，直接进行调用
df = pandas.DataFrame({
    'first_column':[1,2,3,4],
    'second_column':[5,6,7,8]
})



# 使用st.map()你可以在地图上显示数据点。
def demo_map():
    map_data = pandas.DataFrame(
        numpy.random.randn(100,2) / [50,50] + [31.23,-121.47],
        columns=['lat','lon']
    )
    #st.map(map_data)

def demo_line_chart():
    #复选框
    if st.checkbox('Show dataframe'):
        chart_data = pandas.DataFrame(
            numpy.random.randn(20,3),
            columns=['a','b','c']
        )
        st.line_chart(chart_data)

def demo_selectbox():
    # 列表选择框
    option = st.selectbox(
        'Which number do you like best?',
        df['first_column']
    )
    #st.write('You selected: ', option)

def demo_sidebar():
    # 将组件放在侧栏
    side_option = st.sidebar.selectbox(
        'Which number do you like best?',
        df['first_column']
    )

def demo_progress():
    # 进度条
    st.write('Starting a long computation...')
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i+1)
        time.sleep(0.1)

    st.write('Done!')

def demo_slider():
    st.header('slider')
    st.subheader('Slider')
    age = st.slider('How old are u?',0,130,25)
    st.write('I am ',age,'years old.')

    st.subheader('Range slider')
    values = st.slider(
        'Select a range of values',
        0.0,100.0,(25.0,75.0))
    st.write('Values:',values)


    st.subheader('Range time slider')
    appointment = st.slider(
        "Schedule your appointment:",
        value=(time(11, 30), time(12, 45)))
    st.write("You're scheduled for:", appointment)

    st.subheader('Datetime slider')
    start_time = st.slider(
        "When do you start?",
        value=datetime(2020, 1, 1, 9, 30),
        format="MM/DD/YY - hh:mm")
    st.write("Start time:", start_time)
demo_slider()

