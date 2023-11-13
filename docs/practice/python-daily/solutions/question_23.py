#Input: ["bat", "tab", "cat", "tac"]
#Output: [("bat", "tab"), ("cat", "tac")]

class CheckPalindrome:

    def __init__(self, list_of_strings: [str]):
        new_list = []

        for word in list_of_strings:
            word = str(word).lower()
            new_list.append(word)

        self.output = []
        self.temp = []

        for i in range(len(new_list)):
            for j in range(i+1,len(new_list)):
                k = len(new_list[i])
                l = len(new_list[j])
                m = 0
                if len(new_list[i][k-1]) != len(new_list[j][m]):
                    continue
                else:

                    while new_list[i][k-1] == new_list[j][m] and m <= l-1:
                        if m == l-1:
                            self.temp.append(new_list[i])
                            self.temp.append(new_list[j])
                            item = tuple(self.temp)
                            self.output.append(item)

                            break
                        self.temp = []


                        m += 1
                        k -= 1

        print(self.output)

CheckPalindrome(["bat", "tab", "cat", "tac"])



































