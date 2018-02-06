import datetime
# import glob2

filename = datetime.datetime.now()

filenames = ['file1.txt', 'file2.txt', 'file3.txt']
# filenames = glob2.glob("*.txt")


def create_file():
    with open(filename.strftime("%Y-%m-%d-%H-%M-%f") + ".txt", "w") as outfile:
        for fname in filenames:
            with open(fname) as infile:
                outfile.write(infile.read())
		# for filename in filenames:
			# with open(filename,"r") as f:
            # 	file.write(f.read()+"\n")

create_file()

"""
1. Please download the three text files attached in this lecture and put them in a folder. The first text file contains the text Content1 . The second contains Content2 and the third Content3 .

2. You should create a Python script that generates a new text file which should contain the content of all three text files. So the generated file should have this content:

Content1 
Content2 
Content3 

In other words, your Python script should merge the three text files. 

3. Also, the name of the output file should be the current timestamp. Example:2017-11-01-13-57-39-170965.txt 

You have some tips in the next lecture and the solution in the lecture after that.

1. Consider using the glob2 third-party library to generate a list of filenames to iterate through.

2. Use a "with" statement to create a new text file and then iterate through the file list inside that "with" statement and open and read existing file contents in each iteration and write them to new text file.
"""