//#pragma GCC optimize("O3")
#include <bits/stdc++.h>
using namespace std;

int main() {
    int a = 41;
    //for (int a = 12; a < 47; ++a)
    for (int b = 0; b < 47; ++b)
    for (int c = 0; c < 47; ++c)
    for (int d = 0; d < 47; ++d)
    for (int e = 0; e < 47; ++e) {
        long long f = (19 - a - b - c - d - e + 47*47) % 47;

        printf("%d %d %d %d %d %lld\n", a, b, c, d, e, f);

        if (
            (a*64 + b*32 + c*16 + d*8 + e*4 + f*2 + 1) % 47 == 35 &&
            (a*729 + b*243 + c*81 + d*27 + e*9 + f*3 + 1) % 47 == 33 &&
            (a*4096 + b*1024 + c*256 + d*64 + e*16 + f*4 + 1) % 47 == 42 &&
            (a*15625 + b*3125 + c*625 + d*125 + e*25 + f*5 + 1) % 47 == 14 &&
            (a*46656 + b*7776 + c*1296 + d*216 + e*36 + f*6 + 1) % 47 == 41
        ) {
            printf("found");
            exit(0);
        }
    }
}
