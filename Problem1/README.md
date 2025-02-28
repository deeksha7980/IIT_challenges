# 🟢 Sum of Boundary and Diagonal Elements  

## 📌 Problem Statement  
Given an \( n \times n \) matrix, compute the sum of all **boundary** and **diagonal** elements. Ensure that elements appearing in both categories are counted only once.  

## 🔢 Input Format  
1. The first line contains an integer \( n \) (number of rows and columns).  
2. The next \( n \) lines contain \( n \) space-separated integers representing the matrix elements.  

## 🎯 Constraints  
- \( 1 \leq n \leq 1000 \)  
- Each element in the matrix \( \leq 10000 \)  

## 📝 Output Format  
Print a single integer representing the sum of boundary and diagonal elements.  

## 🏆 Example  

### **Input**  
```
5  
1 2 3 4 5  
6 7 8 9 1  
2 3 4 5 6  
7 8 9 1 2  
3 4 5 6 7  
```
### **Output**  
```
93
```

### **Explanation**  
**Boundary Elements**:  
`1, 2, 3, 4, 5, 1, 6, 2, 7, 6, 5, 4, 3, 7, 2, 6`  

**Diagonal Elements (excluding already counted boundary elements)**:  
`7, 4, 1, 9, 4, 8`  

Total Sum = `93` ✅  

---

## 📜 License  
This program is for educational and competitive programming purposes.  
