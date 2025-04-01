# 🧭 Computational Geometry Projects

This repository contains a collection of computational geometry algorithms implemented in Python, mainly focused on convex hulls and range queries. It was developed as part of academic coursework.

## 📁 Project Structure

- `main.py`  
  Implementation of the **Jarvis March** algorithm for computing the convex hull. It reads 2D points from `ksztalt_3.txt`, calculates the convex hull, and visualizes it using Matplotlib.

- `main2.py`  
  Implementation of the **Graham Scan** algorithm for convex hull calculation. It loads data from `ksztalt_1.txt`, sorts points by angle, constructs the convex hull, and displays the result.

- `lab1_GO.ipynb`  
  Jupyter Notebook that provides a visual and interactive demonstration of geometric algorithms, used for experiments, testing and visualization of point sets.

- `rangeTree2D.py.py`  
  Python script implementing a **2D Range Tree**, a data structure used to efficiently query subsets of 2D points within a rectangular region.

## 📌 Algorithms Covered

- Convex Hull: Jarvis March (Gift Wrapping)
- Convex Hull: Graham Scan
- Range Tree (2D)

## 📊 Requirements

- Python 3.x
- NumPy
- Matplotlib
- Jupyter Notebook (for `.ipynb` files)
