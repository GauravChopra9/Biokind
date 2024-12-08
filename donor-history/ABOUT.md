# Intro

This directory called `Donor History` hosts everything needed to understand and learn about this dashboard. 

Given a dataset $D$ such that $d \in D$ represents a `.csv` file, 
This directory will have the following $\forall d \in D$: 

1. `d.csv` - the data used for the dashboard
2. `eda.py` - the code used on the data
3. `app.py` - the code used to run the dashboard
4. `requirements.txt` - the necessary imports to run the dashboard



# $\Gamma$

Denote $\mathbb{C}$ as the classes space. 

For class $c \in \mathbb{C}$, $||c||$ is the number of credits. 

Let $\omega: \mathbb{C} \to \mathbb{R}^\geq $ so that: 

$$
\omega(c \in \mathbb{C}) = \cases {
0  \text{ grade is F}\\
1  \text{ grade is D}\\
2  \text{ grade is C}\\
2.5  \text{ grade is BC}\\
3  \text{ grade is B}\\
3.5  \text{ grade is AB}\\
4  \text{ grade is A}
}
$$

Having established $\omega$ we can then define $\Gamma$ as follows;

For student $s$ having taken $n$ classes in total: 

$$
\Gamma(s, n) = \frac{\sum_n{(||c_i||} \times \omega(c_i))}{\sum_n{||c_i||}}
$$
