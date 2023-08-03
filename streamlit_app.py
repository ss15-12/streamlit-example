# from collections import namedtuple
# import altair as alt
# import math
# import pandas as pd
# import streamlit as st

# """
# # Welcome to Streamlit!

# Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

# If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
# forums](https://discuss.streamlit.io).

# In the meantime, below is an example of what you can do with just a few lines of code:
# """


# with st.echo(code_location='below'):
#     total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
#     num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

#     Point = namedtuple('Point', 'x y')
#     data = []

#     points_per_turn = total_points / num_turns

#     for curr_point_num in range(total_points):
#         curr_turn, i = divmod(curr_point_num, points_per_turn)
#         angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
#         radius = curr_point_num / total_points
#         x = radius * math.cos(angle)
#         y = radius * math.sin(angle)
#         data.append(Point(x, y))



    # st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
    #     .mark_circle(color='#0068c9', opacity=0.5)
    #     .encode(x='x:Q', y='y:Q'))
import streamlit as st
tab1, tab2, tab3 = st.tabs(["Disease Identification", "Crop prediction", "Terrace farmin advisory"])
with tab1:
    st.header("Disease Identification")
with tab2:
    st.header("Crop prediction") 
with tab3:
    vegetable_data = {
        "Tinda": {
            "Ideal Temp. C": 25,
            "Range Temp C": "20-30",
            "Growing_way": "Direct",
            "North India": "Feb-Mar/Jun-Jul",
            "South India": "Feb-Mar/Jun-Jul"
        },
        "Beet": {
            "Ideal Temp. C": 20,
            "Range Temp C": "10-30",
            "Growing_way": "Direct",
            "North India": "Oct-Nov",
            "South India": "Aug-Nov"
        },
        "Bittergourd": {
            "Ideal Temp. C": 25,
            "Range Temp C": "20-30",
            "Growing_way": "Direct",
            "North India": "Feb-March/June-July",
            "South India": "Nov-Dec/Dec-JanJun-July"
        },
        "Tomato":{
            "Ideal Temp. C": 25,
            "Range Temp C": "20-30",
            "Growing_way": "Direct",
            "North India": "Feb-March/June-July",
            "South India": "Nov-Dec/Dec-JanJun-July"
        },
        "Potato":{
            "Ideal Temp. C": 25,
            "Range Temp C": "20-30",
            "Growing_way": "Direct",
            "North India": "Feb-March/June-July",
            "South India": "Nov-Dec/Dec-JanJun-July"
        },
        "Brinjal":{
            "Ideal Temp. C": 25,
            "Range Temp C": "20-30",
            "Growing_way": "Direct",
            "North India": "Feb-March/June-July",
            "South India": "Nov-Dec/Dec-JanJun-July"
        }
        # Add more vegetables here...
    }
    
    def display_characteristics(vegetable_name):
        if vegetable_name in vegetable_data:
            return vegetable_data[vegetable_name]
        else:
            return None
    
    # Streamlit app
    def main():
        st.title("Vegetable Characteristics Viewer")
    
        st.write("Select a vegetable to view its characteristics:")
    
        # User input for vegetable selection
        selected_vegetable = st.selectbox("Select a vegetable", list(vegetable_data.keys()))
    
        if st.button("Display Characteristics"):
            characteristics = display_characteristics(selected_vegetable)
            if characteristics:
                st.write(f"Characteristics of {selected_vegetable}:")
                for key, value in characteristics.items():
                    st.write(f"{key}: {value}")
            else:
                st.error(f"{selected_vegetable} not found in the database.")
    
    if __name__ == "__main__":
        main()
