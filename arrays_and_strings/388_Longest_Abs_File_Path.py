class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # Add a newline at the end for easy parsing of last file/dir
        input += "\n"

        stack = [] # Current absolute path
        strBuilder = ""
        ind = 0
        res = 0
      
        # O(n) runtime
        while ind < len(input):
            if input[ind] != "\n":
                # build up the string
                strBuilder += input[ind]
                ind += 1
            else:
                # add current built string to the stack
                stack.append(strBuilder)

                # do logic for checking for file and absolute length
                if "." in list(strBuilder):
                    currPathLength = 0
                    for name in stack:
                        currPathLength += len(name)
                    # make sure to account for the /'s in the file path
                    res = max(res, currPathLength + len(stack) - 1)
                
                # reset string
                strBuilder = ""

                # iterate over the \n
                ind += 1

                # once we break out, we'll be back to a directory or file name
                tabs = 0
                while ind < len(input) and input[ind] == "\t":
                    tabs += 1
                    ind += 1

                # pop off the stack if tabs for next thing to add and length of stack don't match
                while ind < len(input) and tabs < len(stack):
                    stack.pop()
        return res
