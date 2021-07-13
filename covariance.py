def covariance(x: [int or float], y: [int or float]) -> float:
    """
    Given two series of observed values, calculate the covariance
    
    Args:
        x: a collection of integers or float values
        y: a collection of integers or float values
    Returns:
        float value representing the covariance between 
        series x and y.
    """
    # ensure series contain same number of elements
    if len(x) != len(y):
        raise Exception("Series must be of equal length!")
    
    # Calculate the sample means once
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)

    # Calculate the sum of the product between
    # the differences of observed values and their
    # respective sample means.
    cov = 0.0
    for xi, yi in zip(x, y):
        cov += (xi - x_mean) * (yi - y_mean)
    
    return cov / (len(x) - 1)
