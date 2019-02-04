class textToLights:
    def __init__(self, text, font_size):
        self.text = text
        self.font_size = font_size

    def convert(self):
        """

        H

        *   *       *       *  
        * * *     * * *     * *
        *   *    *     *    * *
        """
        for character in self.text:
            number = ord(character) - 96
            y = self.get_letter(number)

            

    def get_letter(self, letter_num):
        list_letters = [" * 
                         *** 
                        *   *", "*  ** ** "]
        return list_letters[letter_num]
