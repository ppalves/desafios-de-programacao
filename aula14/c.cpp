#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, w;
    scanf("%d", &n);
    scanf("%d", &w);
    int bears[n];
    int elephant[w];
    for (int i = 0; i < n; i++){
        scanf("%d", &bears[i]);
    }
    for (int i = 0; i < w; i++){
        scanf("%d", &elephant[i]);
    }
    int *menor;
    menor = min_element(elephant, elephant + w);
    printf("%d\n", *menor);
    for (int i = 0; i < w; i++){
        elephant[i] = elephant[i] - *menor;
    }
    for (int i = 0; i < w; i++){
        printf("%d ", elephant[i]);
    }
    printf("\n");
    int numero;
    numero = 0;
    for (int i = 0; i < n - w + 1; i++){
        int contem = 1;
        for (int j = 0; j < w - 1; j++){
            if(!(bears[i + j] >= elephant[j] && ((bears[i + j + 1] - bears[i + j]) == (elephant[j + 1] - elephant[j])) && bears[i + j + 1] >= elephant[j + 1])){
                contem = 0;
                break;
            }
        }
        if(contem){
            numero++;
        }
    }
    printf("%d\n", numero);
    return 0;
}