# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    value = st.slider('val')  # this is a widget
    st.write(value, 'squared is', value * value)
    my_expander = st.expander(label='Expand me')
    with my_expander:
        'Hello there!'
        clicked = st.button('Click me!')

    def my_widget(key):
        st.subheader('Hello there!')
        return st.button("Click me " + key)

    # This works in the main area
    clicked = my_widget("first")

    # And within an expander
    my_expander = st.expander("Expand", expanded=True)
    with my_expander:
        clicked = my_widget("second")

    # AND in st.sidebar!
    with st.sidebar:
        clicked = my_widget("third")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
