## ✅ 📄 **User Guideline — How to Use This Project**

Hello!
This project is a **complete Machine Learning web application** that predicts which product category a customer is most likely to buy. It’s designed for non-technical users to test, run, and see how a predictive model works in a real-world scenario.

Here’s a simple step-by-step guide to get started:

---

### ✅ 1️⃣ What this does

* Segments customers into groups using **K-Means Clustering**.
* Predicts the likely product category using **K-Nearest Neighbors (KNN)**.
* Provides a clean, modern **web interface** built with **Flask** and **Bootstrap 5**.
* Includes a **login page** to restrict access to predictions.
* Displays a **pie chart** showing customer segments visually.

---

### ✅ 2️⃣ How to run it

1. **Install Python**: Make sure you have **Python 3.x** installed.

2. **Install the required packages**:
   Open your terminal, navigate to the project folder, and run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Make sure your models are ready**:
   Ensure the folder `/models` contains:

   * `scaler.pkl`
   * `knn_model.pkl`
   * `kmeans_model.pkl`

   If these are missing, run your training script first.

4. **Run the web app**:
   In your terminal, run:

   ```bash
   python app.py
   ```

   By default, the app will run locally at **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

5. **Login to the system**:

   * **Username:** `admin`
   * **Password:** `1234`
     (You can change these in `app.py` if you want.)

---

### ✅ 3️⃣ How to make a prediction

* After logging in, fill out the **Customer Info Form** with:

  * Age
  * Gender
  * Purchase Amount
  * Review Rating
  * Shopping Experience (# Purchases)
  * Subscription Status
  * Discount Applied

* Click **Predict Now**.

* The result page will show:

  * The customer’s cluster segment.
  * The likely product category they will buy.
  * A pie chart showing the overall customer segmentation.

---

### ✅ 4️⃣ Good to know

* If you enter wrong login details, you’ll see a red error message.
* If there’s an issue with your input, you’ll get a clear error message (toast notification).
* The footer **“© 2025 PredictProductCategory System | Designed by Nethru Randev Wickramasekara ❤️”** is visible on every page for a consistent, professional look.
* This is a **demo version** — the login is session-based only, no real database.
  For production, you’d expand this with real user management and a secure database.

---

### ✅ 5️⃣ Need help?

If you run into any trouble:

* Make sure you’re running the correct Python version and virtual environment.
* Double-check your trained model files are saved in the `/models` folder.
* If you see an error about a missing file, it means your `.pkl` files were not generated yet.

---

### ✅ ✅ Thank you for using this project!

This system is a great starting point for understanding how Machine Learning models can be deployed as an interactive web tool to support smarter business decisions.

Feel free to extend, modify, and integrate it with real business data and user authentication for production use.

---

If you have any questions, please let me know!
**Happy predicting!**

