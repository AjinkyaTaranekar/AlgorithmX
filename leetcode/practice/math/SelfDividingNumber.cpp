class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> SDN;

        for (int i = left; i <= right; i++)
        if (IsSelfDividingNumber(i)) 
            SDN.push_back(i);
        return SDN;
    }
private:
    bool IsSelfDividingNumber(int n){
        int temp = n;
        while (temp > 0){
            int d = temp % 10;
            if (d == 0 || n % d != 0) 
                return false;
            temp /= 10;
        }
        return true;
    }
};
