def main():
    file_name = input("ENTER NAME: ")
    file_content = input("""ENTER CONTENT: """)

    f = open(file_name + ".txt", "a")
    f.write(file_content)
    f.close()

    f = open(file_name + ".txt", "r")
    print(f.read())

    restart = input("AGAIN?(yes/no): ")

    if restart == "yes":
        main()
    else:
        exit()

main()
