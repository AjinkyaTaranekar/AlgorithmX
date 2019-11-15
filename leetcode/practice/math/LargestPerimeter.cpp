class Solution {
public:
    int largestPerimeter(vector<int>& A) {
        
        sort(A.begin(), A.end(), greater<int>()); 
  
        int maxi = 0; 
        for (int i = 0; i < A.size()-2; i++){ 
            if (A[i] < A[i+1] + A[i+2]){ 
                maxi = max(maxi, A[i] + A[i+1] + A[i+2]); 
                break; 
            } 
        } 
        if (maxi) 
            return maxi;
        return 0;
    }
};
