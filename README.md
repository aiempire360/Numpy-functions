# NumPy Array Creation and Aggregate Functions

This project demonstrates essential NumPy functions for creating arrays and performing aggregate (summary) operations on data.

## Topics Covered

### Array Creation Functions

#### Zeros Array

Create arrays filled with zeros.

```python
np.zeros((2, 3, 4))
```

#### Ones Array

Create arrays filled with ones.

```python
np.ones((2, 3, 4))
```

#### Full Array

Create arrays filled with a specific value.

```python
np.full((2, 3, 4), 7)
```

#### Identity Matrix

Create an identity matrix.

```python
np.eye(4)
```

### Sequence Generation

#### arange()

Generate evenly spaced values within a given range.

```python
np.arange(1, 100)
```

#### linspace()

Generate a specified number of evenly spaced values between two numbers.

```python
np.linspace(2, 30, 10)
```

## Aggregate Functions

Aggregate functions summarize data and return meaningful statistics.

### Sum

```python
np.sum(arr7)
```

### Mean (Average)

```python
np.mean(arr7)
```

### Minimum Value

```python
np.min(arr7)
```

### Maximum Value

```python
np.max(arr7)
```

### Index of Minimum Value

```python
np.argmin(arr7)
```

### Index of Maximum Value

```python
np.argmax(arr7)
```

### Row-wise Sum Using Axis

```python
np.sum(arr7, axis=1)
```

## Learning Objectives

By completing this project, you will learn:

* How to create arrays using NumPy utility functions
* The difference between zeros, ones, full, and identity matrices
* How to generate numerical sequences
* How to calculate statistical summaries
* How aggregate functions work on multidimensional arrays
* How to use the `axis` parameter for row-wise and column-wise operations

## Technologies Used

* Python
* NumPy

## Skills Practiced

* Array creation
* Numerical sequence generation
* Statistical analysis
* Data summarization
* Multidimensional array operations
* Working with aggregate functions

This project is designed for beginners learning NumPy fundamentals and provides hands-on examples of array generation and data analysis operations.
