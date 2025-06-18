def write_to_queue(content):
    with open("code_queue.txt", "w") as f:
        f.write(content)
