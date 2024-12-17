import streamlit as st
import pickle
import numpy as np

def lowercase_freq(x):
    return np.round(len([char for char in x if char.islower()])/len(x) , 3)

def uppercase_freq(x):
    return np.round(len([char for char in x if char.isupper()])/len(x) ,3 )

def number_freq(x):
    return np.round(len([char for char in x if char.isnumeric()])/len(x) , 3)
def specialchar_freq(x):
    l = 0
    for char in x:
        l += char.isalnum()
    return np.round((len(x)-l)/len(x) , 3)

def predict(password):
    sample_array = np.array([password])
    sample_matrix = vectorizer.transform(sample_array)
    length = len(password)
    lowercase = lowercase_freq(password)
    uppercase = uppercase_freq(password)
    numbers = number_freq(password)
    specialchar = specialchar_freq(password)
    new_mat = np.append(sample_matrix.toarray() , (length , lowercase , uppercase , numbers , specialchar))
    new_mat = new_mat.reshape(1,104)
    result = clf.predict(new_mat)

    if result==0:
        return 'Password is weak'
    elif result==1:
        return 'Password is normal'
    else:
        return 'Password is strong'
    
# Load trained model and vectorizer
clf = pickle.load(open("model.pkl" , 'rb'))   # Replace with your model path
vectorizer = pickle.load(open("vectorizer.pkl" , 'rb'))   # Replace with your vectorizer path

# Streamlit App Layout
def main():
    st.title("🔐 Password Strength Predictor")
    st.write("Check if your password is Weak, Normal, or Strong!")

    # Input field for password
    user_password = st.text_input("Enter your password", type="password")

    # Predict button
    if st.button("Predict Strength"):
        if user_password:
            prediction = predict(user_password)
            st.write(prediction)
        else:
            st.warning("⚠️ Please enter a password to check its strength!")

    # Footer
    st.write("---")
    st.write("Developed by **Vishwamohan Singh Negi**")

# Run Streamlit app
if __name__ == "__main__":
    main()
