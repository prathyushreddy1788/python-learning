class AnagramCheck:
    def __init__(self, input_str1: str, input_str2: str):
        self.input_str1 = input_str1.lower()
        self.input_str2 = input_str2.lower()
        self.output_str1 = ""
        self.output_str2 = ""

        for char in self.input_str1:
            ascii_value = ord(char)
            if ascii_value in range(97, 123):
                self.output_str1 += char
        for char in self.input_str2:
            ascii_value = ord(char)
            if ascii_value in range(97, 123):
                self.output_str2 += char
        if len(self.output_str1) != len(self.output_str2):
            print("it is not an anagram")
        else:
            j = len(self.output_str1)
            for i in self.output_str1:

                if i in self.output_str2:
                    if i == self.output_str1[j-1]:
                        print(" it is an anagram")
                        break

                    continue
                else:
                    print("not an anagram")
                    break

anagramcheck = AnagramCheck("listen","silent")


