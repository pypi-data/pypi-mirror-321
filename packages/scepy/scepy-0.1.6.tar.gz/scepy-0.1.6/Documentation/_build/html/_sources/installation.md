# Installation

This guide provides step-by-step instructions to install the **SCEPY** package using different methods. Depending on your preference or requirement, you can choose to install it from PyPI or GitHub.



### **Installing from PyPI**

The easiest way to install the latest stable version of **SCEPY** is via PyPI using pip.

1. Open your terminal or command prompt.
2. Run the following command:

```bash
pip install scepy
```



### **Installing from GitHub**

If you prefer to install the development version or access the latest updates directly from the source code, you can install it from the GitHub repository.

#### **Method 1: Using pip**

1. Ensure you have Git installed on your system. If not, download and install it from [git-scm.com](https://git-scm.com/).
2. Run the following command in your terminal or command prompt:

```bash
pip install git+https://github.com/ahsankhodami/scepy.git
```



#### **Method 2: Clone and Install**

1. Clone the repository to your local system:

```bash
git clone https://github.com/ahsankhodami/scepy.git
```

2. Navigate to the cloned directory:

```bash
cd scepy
```

3. Install the package using pip:

```bash
pip install .
```



### **Verifying Installation**

After installation, verify that **SCEPY** is installed correctly by checking its version:

```bash
python -c "import scepy; print(scepy.__version__)"
```