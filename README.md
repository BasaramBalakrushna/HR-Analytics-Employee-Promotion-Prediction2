<h1>🚀 HR Analytics – Employee Promotion Prediction</h1>

<p><strong>Author:</strong> Basaram Balakrushna</p>

---

<h2>🧠 Problem Statement</h2>
<p>
Organizations want to <strong>identify employees (manager & below) who are suitable for promotion</strong>.  
Currently, promotions are evaluated only at the end of training & appraisal, which causes delays and may overlook deserving employees.  
This project builds a machine learning model to <strong>predict promotions earlier</strong>, helping HR teams make faster, fairer, and more data-driven decisions.  
</p>

---

<h2>📂 Project Structure</h2>
<ul>
  <li><strong>app.py</strong> – Interactive Streamlit app for promotion predictions</li>
  <li><strong>xgb_model.pkl</strong> – Trained XGBoost model (add this file manually)</li>
  <li><em>notebooks/HR_Promotion.ipynb</em> – Notebook with data cleaning, EDA, and model training</li>
  <li><em>assets/</em> – Charts & visuals (EDA plots, cover image)</li>
  <li><strong>requirements.txt</strong> – Dependencies list</li>
</ul>

---

<h2>🔍 Key Features</h2>
<ul>
  <li>📊 Exploratory Data Analysis (EDA) on 54,000+ employee records</li>
  <li>🧹 Data cleaning & feature engineering</li>
  <li>🤖 Model comparison: Logistic Regression, Random Forest, XGBoost</li>
  <li>🎯 Deployment-ready Streamlit web app for HR teams</li>
  <li>📈 Business insights on factors driving promotions</li>
</ul>

---

<h2>🛠️ Technologies Used</h2>
<ul>
  <li>🐍 Python 3</li>
  <li>📦 Pandas, NumPy</li>
  <li>📊 Matplotlib, Seaborn</li>
  <li>⚙️ scikit-learn</li>
  <li>🌲 XGBoost</li>
  <li>💻 Streamlit</li>
  <li>💾 Joblib</li>
</ul>

---

<h2>⚙️ How to Run the Project</h2>
<ol>
  <li>Clone this repository:
    <pre><code>git clone &lt;your-repo-url&gt;
cd &lt;your-repo-folder&gt;</code></pre>
  </li>
  <li>Create and activate a virtual environment:
    <pre><code>python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # macOS/Linux</code></pre>
  </li>
  <li>Install dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Add the trained model file <code>xgb_model.pkl</code> at the project root</li>
  <li>Run the Streamlit app:
    <pre><code>streamlit run app.py</code></pre>
  </li>
</ol>

---

<h2>📊 Dataset Overview</h2>
<ul>
  <li><strong>Rows/Columns:</strong> ~54,000 employees × 14 features</li>
  <li><strong>Target Variable:</strong> <code>is_promoted</code> (1 = promoted, 0 = not promoted)</li>
  <li><strong>Features include:</strong>
    <ul>
      <li>Department, Region, Education, Gender</li>
      <li>Recruitment Channel, No. of Trainings, Age</li>
      <li>Previous Year Rating, Length of Service</li>
      <li>KPI &gt;80%, Awards Won, Avg Training Score</li>
    </ul>
  </li>
</ul>

---

<h2>📈 Insights from EDA</h2>
<ul>
  <li>🏆 Employees with <strong>KPI > 80%</strong> and <strong>Awards Won</strong> are 2–3x more likely to be promoted</li>
  <li>📚 <strong>Average Training Score > 70</strong> strongly correlates with promotions</li>
  <li>👩‍💻 <strong>Gender and Education</strong> show minimal impact compared to performance metrics</li>
  <li>🔗 Referral hires tend to show better promotion outcomes</li>
</ul>



---

<h2>🤖 Model Performance</h2>

<table>
<tr><th>Model</th><th>Accuracy</th><th>Precision (Class=1)</th><th>Recall (Class=1)</th><th>F1</th></tr>
<tr><td>Logistic Regression</td><td>0.932</td><td>0.867</td><td>0.208</td><td>0.34</td></tr>
<tr><td>Random Forest</td><td>0.937</td><td>0.83</td><td>0.31</td><td>0.45</td></tr>
<tr><td><strong>XGBoost</strong></td><td>0.839</td><td>0.31</td><td><strong>0.72</strong></td><td>0.43</td></tr>
</table>

<p>
✨ <strong>XGBoost selected</strong> for deployment because recall is crucial in HR – it’s better to capture more potential promotion candidates, even if a few false positives occur.
</p>

---

<h2>🖥️ Streamlit App Demo</h2>
<p>
The interactive web app collects inputs:
</p>
<ul>
  <li>Department, Region, Education, Gender, Recruitment Channel</li>
  <li>No. of Trainings, Age, Previous Year Rating, Service Length</li>
  <li>Average Training Score, KPI &gt;80%, Awards Won</li>
</ul>
<p>
And outputs:
</p>
<ul>
  <li>✅ <strong>Likely to be PROMOTED</strong></li>
  <li>❌ <strong>Not likely to be promoted</strong></li>
</ul>

---

<h2>📦 Requirements</h2>
<pre><code>streamlit
pandas
numpy
scikit-learn
xgboost
joblib
matplotlib
seaborn
</code></pre>




---

<h2>📊 Dataset Source</h2>
<p>
The dataset comes from a public HR Analytics competition (anonymized employee records).
</p>
