chunksize = 200000

# Example: Reading a large file in chunks
with open('large_file.txt', 'r') as file:
    while True:
        chunk = file.read(chunksize)
        if not chunk:
            break
        # Process the chunk
        print(chunk)
