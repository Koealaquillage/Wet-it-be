# Wet-it-be
"Forecast. Advise. Nourish."

Project Description:

"And Wet It Be" is a smart irrigation assistant designed to empower farmers with daily, data-driven insights to optimize watering for crops like wheat and rice. By seamlessly combining weather data, machine learning, and user-friendly communication via WhatsApp, we make precision agriculture accessible to everyone.

Whether you're a small-scale farmer or managing expansive fields, "And Wet It Be" takes the guesswork out of irrigation, helping you save water, boost yields, and cultivate healthier crops. With features like personalized watering recommendations and real-time weather updates, it’s like having a trusted farming partner right in your pocket.

Key Features:

    Weather Intelligence: Daily updates based on real-time forecasts.
    Irrigation Advice: Predictive recommendations tailored to your crop and location.
    WhatsApp Integration: Receive notifications and interact with the assistant directly.
    Sustainability Focus: Optimize water use for a greener, more efficient farm.

Mission Statement: Our mission is to help farmers grow smarter, conserve resources, and embrace technology that works in harmony with nature.

---

## 🚀 Features

- **Weather Integration**: Fetches daily weather data using external APIs.
- **ML Predictions**: Provides watering recommendations based on historical and real-time data.
- **WhatsApp Notifications**: Sends personalized messages with weather updates and irrigation advice.
- **Admin Dashboard**: Manage users and monitor system performance.

---

## 🏗️ Project Structure

- **Backend**: API server built with [FastAPI](https://fastapi.tiangolo.com/).
- **Frontend**: User-friendly web app built with [React](https://reactjs.org/) or [Next.js](https://nextjs.org/).
- **ML Model**: Predicts soil watering needs based on historical data, built with [scikit-learn](https://scikit-learn.org/) or [TensorFlow](https://www.tensorflow.org/).
- **Docs**: Contains design documents, API specs, and other documentation.

---

## 📦 Installation

### Prerequisites

- Python 3.8+
- Node.js 16+
- Docker (optional, for containerization)

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/smart-irrigation-assistant.git
    cd smart-irrigation-assistant
    ```

2. **Backend Setup**:
    ```bash
    cd backend
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    uvicorn app.main:app --reload
    ```

3. **Frontend Setup**:
    ```bash
    cd frontend
    npm install
    npm run dev
    ```

4. **ML Model Setup**:
    ```bash
    cd ml-model
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

---

## 🛠️ Usage

1. **Run the Backend**:
    ```bash
    cd backend
    uvicorn app.main:app --reload
    ```

2. **Run the Frontend**:
    ```bash
    cd frontend
    npm run dev
    ```

3. **Send WhatsApp Messages**:
    - Configure your Twilio/WhatsApp API settings.
    - Run the bot script (to be developed in the backend).

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🌐 Contact

- **Author**: Guillaume Koenig
- **Email**: gkoenig.lamon@gmail.com
- **GitHub**: [Koealaquillage](https://github.com/Koealaquillage)
