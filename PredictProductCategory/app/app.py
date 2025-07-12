from flask import Flask, render_template, request, redirect, url_for, session
import numpy as np
import joblib
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# ✅ Use absolute path for models
MODEL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'models'))
scaler = joblib.load(os.path.join(MODEL_DIR, 'scaler.pkl'))
knn_model = joblib.load(os.path.join(MODEL_DIR, 'knn_model.pkl'))
kmeans_model = joblib.load(os.path.join(MODEL_DIR, 'kmeans_model.pkl'))

category_map = {0: "Electronics", 1: "Clothing", 2: "Furniture"}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username'].strip()
        password = request.form['password'].strip()
        if user == 'admin' and password == '1234':
            session['user'] = user
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error_message="Invalid username or password.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'user' not in session:
        return redirect(url_for('login'))
    try:
        age = float(request.form['age'])
        gender = int(request.form['gender'])
        purchase_amount = float(request.form['purchase_amount'])
        review_rating = float(request.form['review_rating'])
        shopping_experience = int(request.form['shopping_experience'])
        subscription_status = int(request.form['subscription_status'])
        discount_applied = int(request.form['discount_applied'])

        features = np.array([[age, gender, purchase_amount, review_rating,
                              shopping_experience, subscription_status, discount_applied]])
        features_scaled = scaler.transform(features)

        cluster = int(kmeans_model.predict(features_scaled)[0])
        prediction = int(knn_model.predict(features_scaled)[0])
        predicted_category = category_map.get(prediction, "Unknown")

        cluster_labels = ['Cluster 0', 'Cluster 1', 'Cluster 2']
        cluster_counts = [40, 30, 30]

        return render_template('result.html',
                               cluster=cluster,
                               category=predicted_category,
                               cluster_labels=cluster_labels,
                               cluster_counts=cluster_counts)
    except Exception as e:
        return render_template('index.html', error_message=f"Prediction failed: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
