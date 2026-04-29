class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(cleaned_text)
        palindrome = cleaned_text[::-1]
        print(palindrome)
        if cleaned_text == palindrome:
            return True
        return False