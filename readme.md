# P2P File Transfer System
![Project Logo](static/cloud.png)

## Overview
This P2P File Transfer System is a decentralized file sharing application designed to facilitate fast and efficient file transfers within a local area network. This project aims to optimize data usage by allowing users to share files directly with each other, bypassing the need for external servers. But the initial days of this project would be a cloud service where people upload their files to a server. I created this application for Covenant University students to be able to send files to each other without eating on their monthly available data.

## Installation & Usage

First clone the repository
```sh
git clone https://github.com/adebola-duf/P2P-transfers-or-cloud-services.git
```

Set up the virtual environment
```sh
python3 -m venv env
env/Scripts/activate  # for Windows
source env/bin/activate  # for Unix or MacOS
```

Install the dependencies
```sh
pip install -r requirements.txt
```

Run the server
```sh
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

