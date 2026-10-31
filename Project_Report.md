# FINAL AI/ML PROJECT REPORT

## Student Performance Prediction System

### 1. Introduction
The Student Performance Prediction System is a Machine Learning project designed to predict students' final academic grades using academic and personal study-related information.

### 2. Objective
- Analyze student academic performance.
- Identify factors affecting final grades.
- Build and compare Machine Learning models.
- Predict final grades using student information.
- Develop an interactive web application.

### 3. Dataset Description
The project uses the Student Performance Dataset (`student-mat.csv`), containing 395 student records and 33 attributes.

Important features include age, study time, past failures, absences, first-period grades (G1), and second-period grades (G2). The target variable is the final grade (G3).

### 4. Technologies Used
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Flask
- Jupyter Notebook

### 5. Data Preprocessing
The dataset was loaded using Pandas with semicolon separation. The relevant features were selected, and the dataset was divided into training and testing sets using an 80:20 ratio.

### 6. Machine Learning Models
Two regression models were developed:
1. Linear Regression
2. Random Forest Regressor

Both models were trained using the selected academic features.

### 7. Model Evaluation
The models were evaluated using:
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R-squared (R²) Score

The evaluation results were used to compare model performance.

### 8. Web Application
A Flask-based web application was developed. Users can enter student details, including age, study time, past failures, absences, and previous grades. The trained Random Forest model predicts the student's final grade out of 20.

### 9. Conclusion
The project demonstrates the use of Machine Learning for student performance prediction. It combines data analysis, visualization, model training, evaluation, and web application development in one complete project.

### 10. Future Scope
- Include more student-related features.
- Improve prediction accuracy through further model optimization.
- Add student performance reports.
- Deploy the application online for wider access.