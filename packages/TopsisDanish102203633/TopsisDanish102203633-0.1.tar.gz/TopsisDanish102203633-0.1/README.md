
# **TopsisDanish102203633: Voice-Controlled TOPSIS Decision-Making Tool**

Welcome to **TopsisDanish102203633**, a groundbreaking package that combines the power of the **TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)** algorithm with **voice-controlled functionality**. This package is designed to streamline decision-making tasks by offering both traditional coding and voice-assisted interfaces.

Whether you're a data scientist, an analyst, or a developer, this tool provides you with the flexibility to run TOPSIS analysis easily and efficiently using either a script or a voice interface. The unique features of this package are designed to maximize productivity, minimize effort, and provide a user-friendly experience.

---

## **Table of Contents**

- **Installation**
- **Features and Showstoppers**
- **Usage**
  - Normal Usage
  - Voice-Controlled Usage
- **Functions**
  - `fill_missing_data()`
  - `topsis()`
  - `VoiceControl Class`
- **Examples**
  - Normal Usage Example
  - Voice-Controlled Usage Example
- **Conclusion**

---

## **Installation**

To install **TopsisDanish102203633**, simply use `pip` from PyPI. This package is available to install via:

```bash
pip install TopsisDanish102203633
```

No need to clone the repository manually! Once installed, you can start using the package right away.

---

## **Features & Showstoppers**

### **1. The TOPSIS Algorithm: Advanced Decision-Making**
At the core of this package is the **TOPSIS algorithm**, widely used for ranking alternatives based on multiple criteria. What sets **TopsisDanish102203633** apart is its versatility:

- **Customizable Distance Metrics**: We provide options to use various distance metrics, such as **Euclidean**, **Manhattan**, **Chebyshev**, and more. This flexibility allows you to tailor the decision process based on the nature of your data.
- **Ideal Solution Proximity**: The algorithm ranks alternatives by their proximity to an ideal solution, ensuring you get the best possible ranking.

### **2. Voice-Controlled Interface**
The standout feature of this package is the **VoiceControl Class**, which enables hands-free interaction with the package. Whether you’re coding or working on a complex project, you can control the flow of analysis without lifting a finger.

Key highlights of the **VoiceControl** system:
- **Voice Commands**: Start the analysis, upload data, and exit the application with simple voice commands.
- **Text-to-Speech Feedback**: Get real-time voice feedback on the actions being performed (e.g., confirmation of file uploads or analysis results).
- **Interactive Workflow**: Instead of typing, you can control every aspect of the system via voice, making it incredibly accessible and efficient for hands-free operation.

### **3. Advanced Missing Data Handling**
Handling missing data is a breeze with **TopsisDanish102203633**. We’ve implemented several strategies to ensure that missing data doesn’t hinder your analysis:
- **Mean, Median, Mode**: Fill missing data using common statistical strategies.
- **Forward Fill, Backward Fill**: Propagate data from adjacent cells to fill gaps.
- **Interpolation**: Use linear or polynomial interpolation to estimate missing values.
- **Customizable Strategies**: You can select different strategies for different columns if needed.

### **4. Integrated with Pandas DataFrames**
The package seamlessly integrates with **Pandas DataFrames**, ensuring smooth data manipulation and ease of use:
- **Direct Data Import**: Easily import CSV or Excel files for analysis.
- **Output Rankings**: The final rankings and decisions are conveniently returned as DataFrames, making it easy to visualize and use them in further analysis or reporting.

---

## **Usage**

### **Normal Usage**

If you prefer using the library through a script, follow these simple steps to start performing TOPSIS analysis.

#### **Steps**:
1. Install the package using `pip install TopsisDanish102203633`.
2. Import the necessary functions and run the analysis as follows:

#### **Example**:

```python
import pandas as pd
from topsis import topsis

# Load your data into a DataFrame
data = pd.read_csv('data.csv')

# Define weights for each criterion (e.g., cost, benefit, etc.)
weights = [0.3, 0.2, 0.5]

# Define impacts (whether higher values are better or worse for each criterion)
impacts = ['+', '-', '+']

# Perform the TOPSIS analysis
topsis(data, weights, impacts)
```

#### **Key Parameters**:
- `df`: The input data (Pandas DataFrame).
- `weights`: List of weights for each criterion.
- `impacts`: List of impacts (`+` for benefit, `-` for cost).
- `distance_metric`: Choose between distance metrics like **Euclidean**, **Manhattan**, etc.
- `missing_data_strategy`: Choose a strategy for handling missing data (**mean**, **median**, etc.).

---

### **Voice-Controlled Usage**

For hands-free control, **VoiceControl Class** lets you operate the package entirely via voice. This provides an interactive, intuitive, and efficient way to run your analysis.

#### **Steps**:
1. Install the package using `pip install TopsisDanish102203633`.
2. Import the `VoiceControl` class and run the system:

#### **Example**:

```python
from voice_control import VoiceControl

# Create an instance of VoiceControl
voice_control = VoiceControl()

# Run the voice control system
voice_control.run()
```

#### **Voice Commands**:
- **"start topsis"**: Starts the TOPSIS analysis.
- **"upload file"**: Allows you to upload a file (CSV or Excel).
- **"exit"**: Exits the system.
- **"help"**: Provides instructions on how to use the system.

### **Functions in VoiceControl**:
- **listen_for_command()**: Listens for and returns voice commands.
- **process_data_input()**: Collects and processes file paths, weights, and impacts.
- **load_data(file_path)**: Loads data from the specified file.
- **process_weights(weights)**: Processes weights provided via voice commands.
- **process_impacts(impacts)**: Processes impacts provided via voice commands.
- **execute_command(command)**: Executes the recognized command (e.g., run TOPSIS, upload file).
- **upload_file_process()**: Handles file uploads based on voice commands.

---

## **Functions**

### **`fill_missing_data(df, strategy='mean')`**
This function fills missing data in the DataFrame using a specified strategy.

**Parameters**:
- `df`: The input pandas DataFrame.
- `strategy`: The strategy for filling missing data (default: 'mean'). Options: **'mean'**, **'median'**, **'mode'**, **'ffill'**, **'bfill'**, **'interpolate_linear'**, **'interpolate_polynomial'**.

**Example**:

```python
df = fill_missing_data(df, strategy='median')
```

### **`topsis(df, weights, impacts, distance_metric='euclidean', missing_data_strategy='mean')`**
This function performs the TOPSIS analysis.

**Parameters**:
- `df`: The input pandas DataFrame.
- `weights`: List of weights for each criterion.
- `impacts`: List of impacts for each criterion (`+` or `-`).
- `distance_metric`: The distance metric for comparison (default: 'euclidean'). Options: **'euclidean'**, **'manhattan'**, **'chebyshev'**.
- `missing_data_strategy`: Strategy for handling missing data (default: 'mean').

**Example**:

```python
topsis(df, weights=[0.3, 0.2, 0.5], impacts=['+', '-', '+'])
```

---

## **Examples**

### **Normal Usage Example**

```python
import pandas as pd
from topsis import topsis

# Load the dataset
df = pd.read_csv('data.csv')

# Define weights and impacts for the TOPSIS analysis
weights = [0.3, 0.2, 0.5]
impacts = ['+', '-', '+']

# Fill missing data (optional)
df = fill_missing_data(df, strategy='mean')

# Run the TOPSIS analysis
topsis(df, weights, impacts)
```

### **Voice-Controlled Usage Example**

Run the following code to start the voice-controlled interface:

```python
from voice_control import VoiceControl

# Initialize voice control system
voice_control = VoiceControl()

# Start the voice control system
voice_control.run()
```

---

## **Conclusion**

With **TopsisDanish102203633**, you're not just using a decision-making algorithm—you're elevating your entire workflow. Whether you're a data analyst looking for hands-on control via code or someone who prefers a hands-free experience, this package delivers unparalleled flexibility and ease of use.

Take advantage of **customizable distance metrics**, **advanced missing data handling**, and **interactive voice control** to enhance your decision-making process. Simplify your work with the power of **TOPSIS** and **VoiceControl** combined.

For any further questions or issues, feel free to open an issue on GitHub or reach out for support.

---

This README is designed to ensure that even a complete beginner can easily understand how to install, use, and fully leverage the power of **TopsisDanish102203633**.
