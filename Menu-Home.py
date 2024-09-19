import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Crisolo Cookbook",
    page_icon="🍽️",
    layout="centered",  # Options: "centered", "wide"
    initial_sidebar_state="expanded"  # Options: "auto", "expanded", "collapsed"
)

# Title of the app
st.title("Crisolo Cookbook")

# Sidebar for navigation
st.sidebar.title("Navigation")
menu_options = ["Home", "Breakfast", "Lunch", "Dinner", "Desserts", "Add/Update Recipe"]
choice = st.sidebar.selectbox("Go to", menu_options)

# Home page content
if choice == "Home":
    st.header("Welcome!")
    st.write("Use the sidebar to navigate through different meal categories.")

    # Display food options in a card-like format
    st.subheader("Available Recipes")

    # Example recipes (replace with your actual recipes)
    recipes = [
        {"name": "Pancakes", "description": "Fluffy pancakes with syrup"},
        {"name": "Grilled Cheese Sandwich", "description": "Cheesy and crispy sandwich"},
        {"name": "Spaghetti Bolognese", "description": "Classic Italian pasta dish"},
        {"name": "Chocolate Cake", "description": "Rich and moist chocolate cake"}
    ]

    # CSS for card-like display
    st.markdown("""
        <style>
        .card {
            background-color: #f9f9f9;
            padding: 20px;
            margin: 10px;
            border-radius: 10px;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
            transition: 0.3s;
        }
        .card:hover {
            box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
        }
        .container {
            padding: 2px 16px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Display each recipe in a card
    for recipe in recipes:
        st.markdown(f"""
            <div class="card">
                <div class="container">
                    <h4><b>{recipe['name']}</b></h4>
                    <p>{recipe['description']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

# Placeholder for other pages
elif choice == "Breakfast":
    st.header("Breakfast Recipes")
    st.write("This is the Breakfast page. Content will be added here later.")
elif choice == "Lunch":
    st.header("Lunch Recipes")
    st.write("This is the Lunch page. Content will be added here later.")
elif choice == "Dinner":
    st.header("Dinner Recipes")
    st.write("This is the Dinner page. Content will be added here later.")
elif choice == "Desserts":
    st.header("Dessert Recipes")
    st.write("This is the Desserts page. Content will be added here later.")
elif choice == "Add/Update Recipe":
    st.header("Add or Update Recipes")
    st.write("This is the Add/Update Recipe page. Content will be added here later.")

# Running the app
if __name__ == "__main__":
    st.write("Streamlit app is running")