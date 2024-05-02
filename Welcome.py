import pandas as pd
import streamlit as st

# Create a sample DataFrame
initial_values = {'Number on Shelf': [10, 12, 10, 8, 10, 10, 2, 2, 6, 4, 6, 5, 6]}
df = pd.DataFrame(initial_values)

# Set the index of the DataFrame
df.index = ['Cheese Danish🧀', 
            'Butter Croissant 🥐', 'Chocolate Croissant🍫', 
            'Bananna Loaf🍌',  'Lemon Loaf🍋',
             'Pumpkin Loaf🎃', 'Blueberry Muffin🫐',
             'Petite Vanilla Bean Scone🍦',
             'Coffee Cake☕', 'Cookies & Cream Cake Pop🍭',
             'Birthday Cake Pop🎂', 'Chocolate Cake Pop🍰', 
            'Chocolate Chip Cookie🍪'
             ]

st.title("Starbucks Pulls☕")

user_inputs = {}
for i, item in enumerate(df.index):
    container = st.container()
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"<div style='line-height: 1.5;'>{item}</div>", unsafe_allow_html=True)
    with col2:
        number_input = st.number_input("", min_value=0, step=1, key=i, label_visibility="hidden")
        user_inputs[i] = number_input

if st.button("Submit"):
    # Update the DataFrame with the remaining values
    for i, value in user_inputs.items():
        df.iloc[i, 0] = initial_values['Number on Shelf'][i] - int(value)
    
    st.write("How Much You Need to Pull:")
    st.write(df)
