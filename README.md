# 🚀 Insurance Premium Prediction API

A Machine Learning powered API that predicts the **Insurance Premium Category** of a user based on health, lifestyle, and demographic information.

This project demonstrates a **complete ML deployment pipeline** using:

* FastAPI (Backend API)
* Scikit-learn (Machine Learning Model)
* Pydantic (Data Validation)
* Streamlit (Frontend UI)
* Docker (Containerization)
* AWS EC2 (Deployment)

---

# 📌 Project Architecture

User → Streamlit UI → FastAPI API → ML Model → Prediction Response

---

# ⚙️ Features

* Predicts insurance premium category (**Low / Medium / High**)
* Calculates **BMI automatically**
* Determines **Lifestyle Risk**
* Categorizes **City Tier**
* Returns **prediction confidence and probabilities**
* Dockerized for easy deployment
* Hosted on **AWS EC2**

---

# 📂 Project Structure

```
insurance-premium-api/
│
├── config/
│   └── city_tier.py
│
├── model/
│   ├── model.pkl
│   └── predict.py
│
├── schema/
│   ├── user_input.py
│   └── prediction_response.py
│
├── app.py
├── requirements.txt
├── Dockerfile
├── streamlit_app.py
└── README.md
```

---

# 🧠 Model Features

The model uses the following features:

* Age
* BMI (calculated)
* Lifestyle Risk
* City Tier
* Income (LPA)
* Occupation

Additional engineered features:

* **BMI = weight / height²**
* **Age Group**
* **Lifestyle Risk**
* **City Tier**

---

# 🔧 Installation (Local Setup)

### 1️⃣ Clone the Repository

```bash
https://github.com/mahadev19/Insurance-primium-FastAPI-small-project.git
cd insurance-premium-api
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv myenv
```

Activate it

Windows:

```bash
myenv\Scripts\activate
```

Linux / Mac:

```bash
source myenv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run FastAPI Server

```bash
uvicorn app:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

Swagger API documentation:

```
http://127.0.0.1:8000/docs
```

---

# 🧪 Example API Request

POST `/predict`

```json
{
 "age": 35,
 "weight": 72,
 "height": 1.75,
 "income_lpa": 12,
 "smoker": false,
 "city": "Pune",
 "occupation": "private_job"
}
```

---

# 📊 Example API Response

```json
{
 "predicted_category": "Medium",
 "confidence": 0.82,
 "class_probabilities": {
  "Low": 0.10,
  "Medium": 0.82,
  "High": 0.08
 }
}
```

---

# 🐳 Run with Docker

Build image

```bash
docker build -t insurance-premium-api .
```

Run container

```bash
docker run -p 8000:8000 insurance-premium-api
```

---

# ☁️ AWS EC2 Deployment

### Install Docker

```bash
sudo apt-get update
sudo apt-get install docker.io
sudo systemctl start docker
```

### Pull Docker Image

```bash
docker pull tweakster24/insurance-premium-api:latest
```

### Run Container

```bash
docker run -d -p 8000:8000 tweakster24/insurance-premium-api
```

---

# 🌐 API Endpoint

```
http://<your-ec2-public-ip>:8000
```

Swagger Docs:

```
http://<your-ec2-public-ip>:8000/docs
```

---

# 🖥️ Streamlit Frontend

Run the UI

```bash
streamlit run streamlit_app.py
```

The UI collects user input and sends requests to the FastAPI backend.

---

# 📦 Tech Stack

| Tool         | Purpose          |
| ------------ | ---------------- |
| FastAPI      | API framework    |
| Scikit-learn | Machine learning |
| Pydantic     | Data validation  |
| Streamlit    | Frontend UI      |
| Docker       | Containerization |
| AWS EC2      | Deployment       |

---

# 👨‍💻 Author

## 📬 Contact

Contact : gmail:- pandmahadev120@gmail.com

linkedin :- https://www.linkedin.com/in/mahadev-data-scientist/

twitter : - https://x.com/Mahadev_Py

link- https://www.mahadev.me/
---

# ⭐ If you like this project

Give it a **star ⭐ on GitHub**
