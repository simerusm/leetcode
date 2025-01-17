class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                # extract the sequence to repeat
                build_seq = ""
                while stack[-1] != "[":
                    build_seq = stack.pop() + build_seq

                # get rid of "["
                stack.pop()

                # extract the number
                build_num = ""
                while stack and stack[-1].isnumeric():
                    build_num = stack.pop() + build_num
                build_num = int(build_num)

                stack.append(build_num * build_seq)

        return "".join(stack)
