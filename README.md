# CartDrop

Real-Time Cart Abandonment Predictor

## Overview

CartDrop predicts whether a customer is:

- Abandoning
- Researching
- Ready To Buy

using clickstream behaviour.

## Tech Stack

- Python
- Random Forest
- Flask
- Streamlit
- Pandas
- Scikit-Learn

## Features

- Real-Time Predictions
- Feature Engineering
- Monotonic Deque
- Dashboard
- REST API

## Run

Generate data

```bash
python data/generate_data.py
```

Train

```bash
python training/train_model.py
```

Run API

```bash
python api/app.py
```

Run Dashboard

```bash
streamlit run dashboard/dashboard.py
```