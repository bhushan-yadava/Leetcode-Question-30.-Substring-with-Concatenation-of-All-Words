class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        # Count the frequency of each word in the 'words' list
        word_count = Counter(words)
        total_length = len(s)
        num_words = len(words)
        word_length = len(words[0])
      
        # This will hold the start indices of the substrings
        start_indices = []
      
        # Check every word_length characters to find valid substrings
        for offset in range(word_length):
            left = right = offset  # Initialize two pointers
            window_word_count = Counter()
            total_matched_words = 0
          
            # Move the window rightwards in the string 's' by word_length
            while right + word_length <= total_length:
                word = s[right: right + word_length]
                right += word_length
              
                # If the word is not in our word_count, reset window
                if word not in word_count:
                    left = right
                    window_word_count.clear()
                    total_matched_words = 0
                    continue
              
                # Increase the count for the new word in our window
                window_word_count[word] += 1
                total_matched_words += 1
              
                # If there are more instances of the word than needed, shrink window
                while window_word_count[word] > word_count[word]:
                    word_to_remove = s[left: left + word_length]
                    left += word_length
                    window_word_count[word_to_remove] -= 1
                    total_matched_words -= 1
              
                # If the window contains exactly 'num_words' words, we found a substring starting at 'left'
                if total_matched_words == num_words:
                    start_indices.append(left)
      
        return start_indices
