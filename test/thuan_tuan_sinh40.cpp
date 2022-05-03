#include <iostream>
#include <string>
#include <math.h>
#include <cstring>
#include <algorithm>
using namespace std;
long long Dec2Bin(int decimalNumber) // Ctrl H => find & replace
{
    long long binaryNumber = 0;
    int p = 0;
    while (decimalNumber > 0)
    {
        binaryNumber += (decimalNumber % 2) * pow(10, p);
        ++p;
        decimalNumber /= 2;
    }
    return binaryNumber;
}
int main()
{
int n;
    string xau="",check="",add_chuoi="0";
    scanf("%d",&n);
    for(int i=0;i<=pow(2,n)-1;i++){
            int bin=Dec2Bin(i);
        xau=to_string(bin);
        while(xau.length()<n){
            xau=add_chuoi+xau;
        }
        check=xau;

        reverse(check.begin(), check.end());
        if(strcmp(check.c_str(),xau.c_str())==0){
                /*Ngăn cách chuỗi bởi dấu cách*/
        for(std::string::iterator it = xau.begin(); it != xau.end(); ++it) {
        cout <<(*it);
        cout << " ";
        /* Kết thúc ngăn cách chuỗi bởi dấu cách*/
        }
        cout << "\n";
        }
    }

    return 0;
}