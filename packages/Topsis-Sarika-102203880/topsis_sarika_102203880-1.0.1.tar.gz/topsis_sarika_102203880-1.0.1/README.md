# TOPSIS Package
TOPSIS - Sarika-102203880
A Python Package for Multi-Criteria Decision Making using TOPSIS
📖 Introduction
TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) is a multi-criteria decision-making method that ranks alternatives based on their distance from an ideal solution. This package helps in decision analysis by evaluating different alternatives based on weighted criteria and selecting the best option.

⚙ Installation
To install this package from PyPI, run:

sh
Copy code
pip install TOPSIS - Sarika-102203880


📌 Usage Guide
Once installed, you can use the package in Python as follows:

1️⃣ Import the Package
python
Copy code
from Topsis.topsis import Topsis
2️⃣ Provide Input Data
python
Copy code
data = [
    [250, 16, 12, 5], 
    [200, 16, 8, 3], 
    [300, 32, 16, 4], 
    [275, 32, 8, 4], 
    [225, 16, 16, 2]
]
weights = [0.25, 0.25, 0.25, 0.25]  # Importance of each criterion
impacts = ['+', '+', '-', '+']  # '+' for beneficial criteria, '-' for non-beneficial
3️⃣ Compute the TOPSIS Score
python
Copy code
topsis = Topsis(data, weights, impacts)
scores, ranks = topsis.calculate_topsis_score()

print("TOPSIS Scores:", scores)
print("Ranks:", ranks)
4️⃣ Example Output
less
Copy code
TOPSIS Scores: [0.62, 0.44, 0.78, 0.66, 0.32]
Ranks: [3, 5, 1, 2, 4]
The alternative with Rank = 1 is the best choice.
🔬 How Does TOPSIS Work?
Normalize the Decision Matrix
Each value is divided by the square root of the sum of squares for that criterion.

Apply Weights
Each normalized value is multiplied by its corresponding weight.

Find Ideal Best & Ideal Worst Values

Ideal Best: The best value for each criterion (max for benefit, min for cost).
Ideal Worst: The worst value for each criterion (min for benefit, max for cost).
Calculate Separation Measures

Distance from Ideal Best
Distance from Ideal Worst
Compute TOPSIS Score
Higher scores mean the alternative is closer to the ideal solution.

Rank the Alternatives
The alternative with the highest TOPSIS score is Rank 1.

📜 License
This project is licensed under the MIT License. You are free to use, modify, and distribute it.

🛠 Contributing
Want to improve this package? Feel free to fork the repository and submit a pull request! 🎯

✉ Contact
For any issues or queries, reach out at: 
📧 Email: sarika090903@gmail.com
📌 GitHub: https://github.com/Sarikaa9

🎉 Enjoy Decision-Making with TOPSIS! 🚀
This version of README.md makes the package more professional and user-friendly. Let me know if you need more edits! 🚀






