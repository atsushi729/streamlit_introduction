from PIL import Image
import streamlit as st
import time

st.title('streamli introduction!!!')

st.write('progress bar')
'start'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.01)

if st.checkbox('Show Image'):
    img = Image.open('test_img.jpg')
    st.image(img, caption='test image', use_column_width=True)

option = st.selectbox(
    'plz input your favorite number',
    list(range(1, 11))
)
'your favorite number is', option
if option == 8:
    'your are luckly person ever!!!!!!!!!'


text = st.text_input('whot is your hobby?')
condition = st.slider('how is your condition now?', 0, 100, 50)

'your hobby  is', text
'your currently condition is', condition

left_column, right_column = st.columns(2)

button = left_column.button('show text right column')
if button:
    right_column.write('this is wight column')

expander1 = st.expander('inquary')
expander1.write('this is answer for FAQ1')
expander2 = st.expander('inquary')
expander2.write('this is answer for FAQ2')
expander3 = st.expander('inquary')
expander3.write('this is answer for FAQ3')

# df = pd.DataFrame(
#     np.random.rand(100, 2) / [50, 50] + [35.69, 139.79],
#     columns=['lat', 'lon']
# )
#
# st.map(df)

# st.dataframe(df.style.highlight_max(axis=1), width=100, height=100)
# st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)
# st.table(df.style.highlight_max(axis=0))


st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
