#include<iostream>
using namespace std;

int trailrecsum(int x, int running_total = 0){
    if(x == 0){
        return running_total;
    }
    else{cout<<1;
         return trailrecsum(x-1, running_total+x);
    }

}


int main(){
    int a = trailrecsum(5);

    cout<<trailrecsum(5)<<endl;
    system("pause");
    return 0;
}
