class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded_string = "";
        for (string i : strs) {
            string length_str = to_string(i.length());
            encoded_string.append(length_str).append("#").append(i);
        }
        return encoded_string;
    }

    vector<string> decode(string s) {
        vector<string> result;
        int i = 0;
        while (i < s.length()) {
            int hash_pos = s.find("#", i);
            int len = stoi(s.substr(i, hash_pos - i));
            string content = s.substr(hash_pos + 1, len);
            result.push_back(content);
            i = i + (hash_pos - i) + 1 + len;
        }
        return result;
    }
};
