# Python Django Titanic Survival Prediction Model

This project is a web application built with Python and Django that predicts the survival chances of passengers aboard the Titanic. It utilizes a machine learning model trained on historical passenger data to make predictions based on input features such as age, gender, and ticket class.

## Features

- **User Input Form**: Enter passenger details like age, gender, class, etc.
- **Survival Prediction**: Receive a prediction on whether the passenger would have survived.
- **Model Training Script**: Includes scripts to train and update the machine learning model.


## Video Execution



https://github.com/user-attachments/assets/f5335139-93db-47b6-8ba0-fd19eca01b89

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rahulthakare04/Python-Django-Titanic-Survival-Prediction-Model.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd Python-Django-Titanic-Survival-Prediction-Model
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

After completing these steps, the application should be running locally, and you can access it via your web browser.

## Usage

1. Open your browser and navigate to `http://127.0.0.1:8000/`.
2. Fill in the passenger details in the input form.
3. Submit the form to receive a prediction about the passenger's survival chances.

## Project Structure

- `titanic/`: Main Django project directory.
- `predictor/`: Django app handling prediction logic.
- `templates/`: HTML templates for the web pages.
- `static/`: Static files (CSS, JavaScript, images).
- `model_training/`: Scripts and notebooks for training the machine learning model.

## Dataset

The model is trained on the Titanic dataset, which includes features such as:

- `Pclass`: Passenger class (1st, 2nd, 3rd).
- `Sex`: Gender of the passenger.
- `Age`: Age of the passenger.
- `SibSp`: Number of siblings/spouses aboard.
- `Parch`: Number of parents/children aboard.
- `Fare`: Ticket fare.
- `Embarked`: Port of embarkation (C = Cherbourg; Q = Queenstown; S = Southampton).

For more details on the dataset, refer to the [Kaggle Titanic Dataset](https://www.kaggle.com/c/titanic/data).

## Model Training

The machine learning model is trained using a Jupyter Notebook located in the `model_training/` directory. The notebook includes steps for data preprocessing, feature engineering, model selection, and evaluation.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

