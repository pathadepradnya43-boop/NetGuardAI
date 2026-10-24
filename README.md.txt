qNetGuardAI

AI-Driven Network Traffic Analysis and Intrusion Detection System

1. Project Overview

NetGuardAI is a Python-based cybersecurity project designed to analyze network traffic records and identify potentially suspicious activity. It provides a simple dashboard where users can upload traffic data in CSV format, review connection counts, and download the analysis results.

The project is being developed as a learning prototype for defensive cybersecurity and network traffic analysis.

2. Objectives

- Analyze network traffic records from a CSV file.
- Identify records that may require further investigation.
- Display analysis results in an interactive dashboard.
- Help users understand suspicious traffic patterns.
- Explore future integration of machine learning for intrusion detection.

3. Current Features

- CSV file upload.
- Traffic record analysis using connection counts.
- Basic rule-based suspicious activity flagging.
- Summary metrics for normal, suspicious, and review-needed records.
- Filtering of analysis results.
- Downloadable CSV analysis report.

4. Technologies Used

- Python: Application programming language.
- Streamlit: Interactive web dashboard.
- Pandas: CSV processing and data analysis.
- Scikit-learn: Planned library for future machine-learning experiments.

5. Project Structure

NetGuardAI/
├── app.py
├── requirements.txt
├── README.md
└── sample_traffic.csv

6. Installation

1. Install Python on your computer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Install the required libraries:

pip install -r requirements.txt

7. Running the Application

Run the following command from the project folder:

python -m streamlit run app.py

The application will open in your web browser.

8. How to Use

1. Start the application.
2. Upload a compatible CSV file containing network traffic records.
3. Review the analysis summary.
4. Examine records flagged for further review.
5. Filter the displayed results as needed.
6. Download the analysis results as a CSV file.

The current version expects a connection-count field to apply its basic detection rule.

9. Current Limitations

- The current prototype uses a demonstration threshold to flag high connection counts.
- A high connection count does not necessarily indicate an attack.
- Detection quality depends on the available data and its format.
- The current rule is not a validated intrusion detection model.
- Machine-learning-based classification and formal performance evaluation are planned improvements.

10. Future Improvements

- Add additional network traffic features.
- Support labeled datasets for normal and attack traffic.
- Explore machine-learning-based intrusion classification.
- Add visual charts and traffic summaries.
- Evaluate accuracy, precision, recall, and false positives using suitable test data.
- Improve explanations for suspicious records.

11. Ethical Use

NetGuardAI is intended for defensive cybersecurity learning and analysis of authorized or sample traffic data. Testing should be performed only with systems and datasets that the user is authorized to use.

12. Limitations
The results depend on the available traffic fields and configured thresholds. Legitimate activity may be flagged, and attacks that do not match the rules may be missed. Testing with simulated records does not established real-world detection accuracy. 

12. Project Status

Status: Working prototype under development.

Features and documentation will be updated as development and testing progress.
