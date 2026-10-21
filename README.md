# 🛒 ShopKart | My DevOps Journey 🚀

### 🐳 Containerizing a Flask Application with Docker

Welcome to my **ShopKart DevOps project!** 💻

As part of my journey toward becoming a DevOps Engineer, I'm learning how to containerize applications, troubleshoot deployment issues, and build reliable workflows through hands-on practice.

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Docker Hub](https://img.shields.io/badge/Docker%20Hub-0DB7ED?style=for-the-badge&logo=docker&logoColor=white)

---

## 🎯 Step 1: Pull the Docker Image

📌 **Goal:** Download the ShopKart image from Docker Hub.

```bash
docker pull ghurka/shopkart:1.0
```

## 🚀 Step 2: Run the Container

📌 **Goal:** Launch ShopKart in the background and expose the application on port `8080`.

```bash
docker run -d --name shopkart-container -p 8080:8080 ghurka/shopkart:1.0
```

### 🔍 Understanding the Command

| Option | Purpose |
|---|---|
| `docker run` | Creates and starts a container |
| `-d` | Runs in the background |
| `--name` | Assigns a container name |
| `-p 8080:8080` | Maps host port to container port |
| `ghurka/shopkart:1.0` | Specifies the image and tag |

## ✅ Step 3: Verify the Container

```bash
docker ps
```

🔎 **Expected result:** `shopkart-container` appears with status `Up`.

## 🌐 Step 4: Access the Application

Open ShopKart in your browser:

👉 [http://localhost:8080](http://localhost:<img width="1357" height="759" alt="shopkart" src="https://github.com/user-attachments/assets/28632925-c947-41dc-8985-cd31ef71bec1" />
