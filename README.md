# Salary Prediction Using Linear Regression

## About the Project

This project uses Simple Linear Regression to understand the relationship between years of work experience and salary.
The model is trained using salary data and learns how salary changes with experience. It then predicts salaries for unseen data and visualizes the results using graphs.
I built this project to understand the basics of machine learning, including data preprocessing, model training, prediction, and visualization.

## Technologies Used

- **Python** – Programming language
- **Pandas** – Loading and handling the dataset
- **NumPy** – Numerical operations
- **Matplotlib** – Visualizing the data and regression line
- **Scikit-learn** – Training and testing the Linear Regression model

## How It Works

1. Load the salary dataset using Pandas.
2. Separate the independent variable (years of experience) and dependent variable (salary/CTC).
3. Split the dataset into training and testing sets.
4. Train a Linear Regression model using the training data.
5. Predict salaries for the test data.
6. Visualize the actual data points and the regression line.

## Model Used

**Simple Linear Regression**

Linear Regression models the relationship between an input variable and a target variable using a straight line.
The equation is:

`Salary = m × Experience + c`

Where:
- `m` is the slope of the regression line.
- `Experience` is the number of years of work experience.
- `c` is the intercept.

## Visualizations

The project plots the training and testing data points and displays the regression line to show how well the model represents the relationship between experience and salary.

## Dataset

The project uses a CSV file named `Salary_Data.csv`, which contains the data required to train and test the model.

The dataset should include years of experience and the corresponding salary or CTC values.

## What I Learned

- Understanding Simple Linear Regression.
- Working with datasets using Pandas and NumPy.
- Splitting data into training and testing sets.
- Training a machine learning model with Scikit-learn.
- Making predictions using a trained model.
- Visualizing data and regression results using Matplotlib.

