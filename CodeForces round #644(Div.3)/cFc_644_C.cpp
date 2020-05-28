//Question --> C. Similar Pairs

#include<bits/stdc++.h>
#define FASTIO ios::sync_with_stdio(false);cin.tie(NULL);
using namespace std;
int32_t main()
{
    int t;
    cin>>t;
    lbl:
    while(t--)
    {
        int n,x;
        cin>>n;
        vector<long long>v;
        vector<long long>even;
        vector<long long>odd;
        int en = 0;
        for(int i=0;i<n;i++)
        {
            cin>>x;
            if(x%2==0)
            {
                even.push_back(x);
                en++;
            }
            odd.push_back(x);
            v.push_back(x);
        }
        if(en%2==0)
        {
            cout<<"YES"<<endl;
            goto lbl;
        }
        else if(en%2!=0)
        {
            int k=0;
            for(int i=0;i<even.size();i++)
            {
                for(int j=0;j<odd.size();j++)
                {
                    int c = abs(even[i]-odd[j]);
                    if(c==1)
                    {
                        k=1;
                        break;
                    }
                }
            }
            if(k==0)
            {
                cout<<"NO"<<endl;
            }
            else
            {
                cout<<"YES"<<endl;
            }
        }
        
    }
    return 0;
}