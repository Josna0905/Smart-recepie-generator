import streamlit as st

# Simple recipe dataset
recipes = {
    "French Toast": ["bread", "egg", "milk"],
    "Veg Sandwich": ["bread", "tomato", "onion"],
    "Egg Fried Rice": ["rice", "egg", "onion"]
}

# Title
st.title("🍳 Smart Recipe Generator")

# User input
user_input = st.text_input("Enter ingredients (comma separated):")

# Button
if st.button("Generate Recipe"):
    ingredients = [i.strip().lower() for i in user_input.split(",")]

    found = False

    for name, items in recipes.items():
        if all(item in ingredients for item in items):
            st.success(f"✅ You can make: {name}")
            st.write("Ingredients needed:", ", ".join(items))
            found = True

    if not found:
        st.warning("❌ No recipe found. Try adding more ingredients!")

# Footer
st.write("💡 Tip: Try entering 'bread, egg, milk'")
