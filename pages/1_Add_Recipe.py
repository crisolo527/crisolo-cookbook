import streamlit as st

# Title of the page
st.title("Add or Update Recipes")

# Form to add or update recipes
with st.form("recipe_form"):
    recipe_name = st.text_input("Recipe Name")
    recipe_description = st.text_area("Recipe Description")
    recipe_tags = st.text_input("Tags (comma-separated)")

    # Submit button
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write(f"Recipe Name: {recipe_name}")
        st.write(f"Description: {recipe_description}")
        st.write(f"Tags: {recipe_tags}")
        st.success("Recipe added/updated successfully!")

# Running the app
if __name__ == "__main__":
    st.write("Streamlit app is running")