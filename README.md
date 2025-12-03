![maintainer](https://img.shields.io/badge/UniMi-blue)
![Academic project](https://img.shields.io/badge/Academic-Project-orange)

# Coding for Data Science

**Author:** Sami HNAIEN  
**Class:** *First-year Master’s student in Data Science for Economics and Health at UniMi*  

This project explores how tourism activity influences **GDP per capita** in Tunisia using datasets provided by the **World Bank Open Data** platform.  
The analysis is performed in a structured Jupyter Notebook that includes data inspection, visualization, and statistical analysis.

![cover image](https://img.shields.io/badge/unimi-blue "Text to show on mouseover")

---

## Project Structure

```
.
├── analysis.ipynb                     # Main Jupyter Notebook for data analysis
├── conf
│   └── conf.ini                       # Project configuration file
├── data
│   ├── gdp_per_capita.csv             # GDP per capita dataset
│   └── tourism_arrival.csv            # International inbound tourists dataset
├── images                             # Image assets for documentation
│   └── cover.png
└── package
    ├── conf.py                        # Module for loading configuration
    ├── dataset.py                     # Module for loading & preparing datasets
    └── graph.py                       # Module for generating graphs & plots
```

---

## How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/sami-hnaien/Project_data.git
```

### 2. Navigate into the project directory
```bash
cd Project_data
```

### 3. (Optional) Install **virtualenv**
Follow the guide: https://virtualenv.pypa.io/en/latest/installation.html

### 4. (Optional) Create and activate a virtual environment
```bash
virtualenv venv
source venv/bin/activate
```

### 5. Install required dependencies
```bash
pip3 install -r requirements.txt
```

### 6. Start Jupyter Lab
```bash
jupyter lab
```

If the browser does not open automatically, copy/paste the link from the terminal into your browser.

---

## Support & Contributions

If you have any questions, or if you want to make this project better, feel free to reach out at: **samihnaien57@gmail.com**