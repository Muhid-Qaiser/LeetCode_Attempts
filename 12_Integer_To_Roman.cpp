class Solution {
public:
    string intToRoman(int num) {
        string temp="", res = "", temp_str="";
        int mult = 10, digit = 0, val=0, temp_num;
        
        digit = (num == 0) ? 1 : (int)log10(abs(num)) + 1;

        for (int i=0; i<digit; i++)
        {
            temp = "";
            val = ( num % mult ) - ( num % ( mult / 10 ) );
            mult *= 10;
            while (val > 0)
            {
            auto [temp_str,temp_num] = getSymbol(val);
            temp += temp_str;
            val -= temp_num;
            }
            res = temp + res;
        }
        return res;
    }

    pair<string, int> getSymbol(int num) {
    if (num >= 1000) return {"M", 1000};
    else if (num >= 900) return {"CM", 900};
    else if (num >= 500) return {"D", 500};
    else if (num >= 400) return {"CD", 400};
    else if (num >= 100) return {"C", 100};
    else if (num >= 90) return {"XC", 90};
    else if (num >= 50) return {"L", 50};
    else if (num >= 40) return {"XL", 40};
    else if (num >= 10) return {"X", 10};
    else if (num >= 9) return {"IX", 9};
    else if (num >= 5) return {"V", 5};
    else if (num >= 4) return {"IV", 4};
    else if (num >= 1) return {"I", 1};
    else return {"", 0};
}


};