// { Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


vector<int> reaching_height(int n, int a[]) ;

int main() {
	int t;
	cin >> t;
	while (t-- > 0) {
	    int n; 
	    cin >> n;
	    int a[n];
	    for (int i = 0; i < n; i++) 
	        cin >> a[i];
	    vector<int> v;
	    v = reaching_height(n,a);
	
	    if(v.size()==1 and v[0] == -1){
	        cout << "Not Possible\n";
	    }
	    else{
	    for(int i:v)
	        cout << i << " ";
	    cout << endl;}
	    
	}
	return 0;
}// } Driver Code Ends


//User function Template for C++

vector<int> reaching_height(int n, int a[]) {
   
   sort(a, a + n);
   int s=0, e=n-1; // start and end index
   vector<int> ans;
   
   for(int i=0;i<n;i++)
   {
      if(i == 0 || i%2 == 0)
      { // if even index push highest element (i.e from back)
          ans.push_back(a[e--]);
      }
      else
      { // if odd index push smallest element (i.e from fornt)
          ans.push_back(a[s++]);
      }
   }
   
   int sum = 0;
   
   for(int i=0;i<n;i++)
   {
      i == 0 || i%2 == 0 ? sum+=ans[i] : sum-=ans[i]; 
   }
   
   if(sum == 0)
      return {-1};
   
   return ans;
}
