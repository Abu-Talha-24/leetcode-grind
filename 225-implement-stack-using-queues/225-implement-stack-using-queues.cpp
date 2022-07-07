class MyStack {
public:
    queue<int> q2;
    
    MyStack() {

    }
    
    void push(int x) {
        if (q2.empty())  {
            q2.push(x);
        }
        else {
            // remove all elements from q2 , push x then remaining
            int n = q2.size(); // Always take the size in a variable and use it .
            vector<int> arr(n);
            int i = 0;
            while(!q2.empty()) {
                arr[i] = q2.front();
                q2.pop();
                i++;
            }
            q2.push(x);
            for (int i = 0; i < n; i++) {
                q2.push(arr[i]);
            }
        }
         
    }
    
    int pop() {
        int res = q2.front();
        q2.pop();
        return res;
        
    }
    
    int top() {
        return q2.front();
        
    }
    
    bool empty() {
        return q2.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */