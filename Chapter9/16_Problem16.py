with open("1st.txt") as f:
    content1 = f.read()

with open("2nd.txt") as f:
    content2 = f.read()

    if(content1 == content2):
        print("Yes Files are identical")
    else:
        print("No Files are not identical")