# Sounds Packing Problem

This repository contains implementations and heuristics for solving the **Sounds Packing Problem**, a variant of the **Bin Packing Problem**. The goal is to efficiently group sound files into folders, minimizing the number of folders used while ensuring that the total duration of files in each folder does not exceed a predefined limit.

## Problem Overview

**Given:**

- A set of `N` sound files, each with a specific duration (in seconds).
- A folder capacity, `X` seconds.

**Objective:**

- Assign the sound files to folders such that:
  - The total duration of files in each folder is ≤ `X`.
  - The number of folders used is minimized.

## Implemented Algorithms

The repository explores various heuristics and algorithms, balancing **runtime efficiency** and **solution quality**:

1. **First Fit**
2. **Best Fit**
3. **Worst Fit**
4. **First Fit Decreasing (FFD)**
5. **Best Fit Decreasing (BFD)**
6. **Harmonic Partitioning**

## Features

- Multiple approaches to solve the problem with different trade-offs in speed and accuracy.
- Includes algorithms for both **exact** and **approximate** solutions.
- Easy-to-follow code with comments and explanations for learning and customization.
