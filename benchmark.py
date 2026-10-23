import time
import random

def data_generator(datapoints):

    dataset = []

    for i in range(datapoints):
        userid = "user" + str(i)
        score = random.randint(1, 100000)

        dataset.append((userid, score))

    random.shuffle(dataset)

    return dataset

def sort_bench():

    print("Generating dataset...")

    dataset = data_generator(15_000_000)

    print("Dataset generated.")
    print("Starting sort...")

    tstart = time.time()

    sorted_dataset = sorted(
        dataset,
        key=lambda x: x[1]
    )

    tend = time.time()

    print(f"Execution Time: {tend - tstart:.2f} seconds")
    print(f"Records Sorted: {len(sorted_dataset)}")

if __name__ == "__main__":
    sort_bench()
