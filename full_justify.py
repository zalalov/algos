def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def line_justify(words, max_width):
            import math
            
            words_count = len(words)
            words_len = sum((len(x) for x in words))
            spaces_count = max_width - words_len
            
            if words_count == 1:
                return '{}{}'.format(words[0], ' ' * (max_width - words_len))
            elif words_count == 2:
                return '{}{}{}'.format(
                    words[0], 
                    ' ' * (max_width - words_len),
                    
                    words[1]
                )
            else:
                words_count_for_spaces = words_count - 1
                
                spaces = [math.floor(spaces_count/(words_count_for_spaces or 1))] * (words_count - 2)
                spaces += [math.ceil(spaces_count/(words_count_for_spaces or 1))]
                
            line = ''
            
            for word in words:
                line = '{}{}'.format(line, '{}{}'.format(word, ' ' * spaces.pop() if word != words[-1] else ''))
                
            return line
            
        result = []
        line_words = []
        line_length = 0
        
        for word in words:
            if line_length + len(word) + 1 < maxWidth:
                line_words.append(word)
                line_length += len(word)
            else:
                result.append(line_justify(line_words, maxWidth))
                line_words = [word]
                line_length = len(word)
                
        if line_length > 0:
            result.append(line_justify(line_words, maxWidth))
                    
        return result
