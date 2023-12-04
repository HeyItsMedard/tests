from multiprocessing import Pool

def square(x):
    return x * x

if __name__ == "__main__":
    # Create a Pool with 4 processes
    with Pool(processes=4) as pool:
        # Define a list of inputs
        inputs = [1, 2, 3, 4, 5]

        # Use map to distribute tasks among processes
        results = pool.map(square, inputs)

    # Print the results
    print(results)