# Data Engineering Toolkit

An engineering toolkit of reusable scripts and functions for common data engineering tasks such as cleaning, transforming, and loading data.

---

## Documentation: Learning Git and GitHub

This project also serves as a hands-on way to **learn Git and GitHub**.  
Topics we’ll practice include:
- Initializing and cloning repositories  
- Using `.gitignore` files  
- Working with branches 
- Making commits   
- Opening Pull Requests (PRs) and handling code reviews  
- Merging branches  

Helpful resources:  
- [GitHub Docs](https://docs.github.com/)  
- [Git & GitHub Tutorial for Beginners (YouTube)](https://www.youtu.be/tRZGeaHPoaw?si=ejYyApyAoFSwWIW)  

---

## Code Examples
```python
import pandas as pd

df = pd.DataFrame({
    "name": ["John", "James", "Peace"],
    "value": [10, 5, 10]
})

print(df)

```

## Contribution Guide

We welcome contributions!

- Use **Gitflow branching** (`feature/<branch-name>`) for new scripts or features.  
- Commit frequently with **descriptive commit messages**.  
- Submit **Pull Requests (PRs)** to the `devtest` branch.  
- Ensure all code is tested before merging.  
