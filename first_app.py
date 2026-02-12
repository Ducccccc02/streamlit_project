import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy
import pandas
import time

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
#df


# 使用st.map()你可以在地图上显示数据点。
map_data = pandas.DataFrame(
    numpy.random.randn(100,2) / [50,50] + [31.23,-121.47],
    columns=['lat','lon']
)
#st.map(map_data)


#复选框
if st.checkbox('Show dataframe'):
    chart_data = pandas.DataFrame(
        numpy.random.randn(20,3),
        columns=['a','b','c']
    )
    st.line_chart(chart_data)


# 列表选择框
option = st.selectbox(
    'Which number do you like best?',
    df['first_column'])
#st.write('You selected: ', option)


# 将组件放在侧栏
side_option = st.sidebar.selectbox(
    'Which number do you like best?',
    df['first_column'])


# 进度条
st.write('Starting a long computation...')
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

st.write('Done!')


