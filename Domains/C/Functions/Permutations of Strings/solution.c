/**
 * Note: Taka a look at the "Generation in lexicographic order" algorithm and summary in:
 * 		https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
 * 
 * 
 * This is the algorithm:
 * 1 - Find the largest index k such that a[k] < a[k+1]. If no such index exists,
 * 		the permutation is the last permutation.
 * 2 - Find that largest index l greater than k such that a[k] < a[l].
 * 3 - Swap the value of a[k] with that of a[l].
 * 4 - Reverse the sequence from a[k+1] up to and including the final element a[n].
 */ 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int next_permutation(int n, char **s) {
	int k = 0, l = 0, perm_exists = 0;
	char * temp = calloc(11, sizeof(char));

	//// Find k
	for (int i=0; i+1<n; ++i) {
		if (strcmp(s[i], s[i+1]) < 0) {
			perm_exists = 1;
			k = i;
		}
	}

	//// Exit if k not found
	if (!perm_exists) {
		free(temp);

		return 0;
	}

	//// Find l
	for (int i=0; i<n; ++i) {
		if (strcmp(s[k], s[i]) < 0) {
			l = i;
		}
	}

	//// Swap values
	strcpy(temp, s[l]);
	strcpy(s[l], s[k]);
	strcpy(s[k], temp);

	//// Reverse sequence from (k+1)th position to the last element
	for (int i=0; i<(int)(n-k)/2; ++i) {
		strcpy(temp, s[i+k+1]);
		strcpy(s[i+k+1], s[n-i-1]);
		strcpy(s[n-i-1], temp);
	}

	free(temp);

	return perm_exists;
}

int main()
{
	char **s;
	int n;
	scanf("%d", &n);
	s = calloc(n, sizeof(char*));
	for (int i = 0; i < n; i++)
	{
		s[i] = calloc(11, sizeof(char));
		scanf("%s", s[i]);
	}
	do
	{
		for (int i = 0; i < n; i++)
			printf("%s%c", s[i], i == n - 1 ? '\n' : ' ');
	} while (next_permutation(n, s));
	for (int i = 0; i < n; i++)
		free(s[i]);
	free(s);
	return 0;
}