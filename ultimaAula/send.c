#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int calculate_v(int *entry, int n){
	int i;
	int j;
	char flag = 0;
	int *as = malloc(pow(2,n)*sizeof(int));
	memcpy(as, entry,pow(2,n)*sizeof(int));
	for (i = n; i > 0; i--){
		for (j = 0; j < pow(2, i); j += 2){
			if (flag == 0){
				as[j]= (as[j]) | (as[j+(int) pow(2,n-i)]);
			}else{
				as[j]= (as[j]) ^ (as[j+(int)pow(2,n-i)]);
			}
		}
		flag = !flag;
	}
	return as[0];

}

int main(){
	int n, m;
	scanf("%d %d", &n, &m);

	int *as = malloc(pow(2,n)*sizeof(int));

	int i;
	for (i = 0; i < pow(2,n); i++){
		scanf("%d", &(as[i]));
	}
	int a, b;
	for (i = 0; i < m; i++){
		scanf("%d %d", &a, &b);
		as[a-1] = b;
		
		printf("%d\n",calculate_v(as, n));
	}
	return 0;
	
}
