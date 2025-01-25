# Topsis-Dishav-102217004

A Python package to implement the **TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution) method, a multi-criteria decision-making approach.

---

## Overview

The **TOPSIS** method is used for ranking alternatives based on their closeness to the ideal solution. It is widely used in decision-making scenarios where multiple criteria are considered.

This package simplifies the process of implementing the TOPSIS method by providing a command-line interface and an easy-to-use Python API.

---

## Features

- Handles multi-criteria decision-making problems.
- Works with weighted criteria and both beneficial (`+`) and non-beneficial (`-`) impacts.
- Outputs a ranked list of alternatives with TOPSIS scores.

---

## Installation

Install the package directly from PyPI:

```bash
pip install Topsis-Dishav-102217004
```

## Usage

Command Line Usage

```bash
topsis <InputFile> <Weights> <Impacts> <ResultFile>
```

Python API Usage

```bash
from Topsis_Dishav_102217004 import topsis
```
