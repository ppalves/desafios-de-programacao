#include <stdio.h>
#include <stdlib.h>


int main(){
	int n, w;
	int i, j;
	scanf("%d %d", &n, &w);
	int *bears = malloc(n*sizeof(int));
	int tmp;
	for (i = 0; i < n; i++){
		scanf("%d", &tmp);
		bears[i] = tmp;
	}
	int *elephant = malloc(w*sizeof(int));
	for (i = 0; i < w; i++){
		scanf("%d", &tmp);
		elephant[i] = tmp;
	}
	int menor = elephant[0];
	for (i = 0; i < w; i++){
		menor = (elephant[i]<menor)?elephant[i]:menor;	
	}

	for (i = 0; i < w; i++){
		elephant[i] -= menor;
	}

	int numero = 0;
	char contem = 1;
	for (i = 0; i < n - w + 1; i++){
		contem = 1;
		for (j = 0; j < w - 1; j++){			
			if (!(bears[i + j] >= elephant[j] && ((bears[i + j + 1] - bears[i + j]) == (elephant[j + 1] - elephant[j])) && bears[i + j + 1] >= elephant[j + 1])){
				contem = 0;
				break;
			}
		}
		if (contem == 1){
			numero += 1;
		}
	}

	printf("%d\n", numero);
	
	return 0;
}
