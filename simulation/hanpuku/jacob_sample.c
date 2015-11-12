#include <stdio.h>

#define N 3
#define T 20

int main(void)
{
  double a[N][N+1] = {
    {7,1,2,10},
    {1,8,3,8},
    {2,3,9,6} };
  
  double x[N], xd[N];
  double s;
  int i,j;
  int t;

  for (i=0; i<N; i++) {
    x[i] = 0;
  }

  for (t=0; t<T; t++) {

    printf("[%2d] ", t);
    for (i=0; i<N; i++) {
      printf("%f ", x[i]);
    }
    printf("\n");

    for (i=0; i<N; i++) {
      /* Write your code here. (hint: one line) */
      for (j=0; j<N; j++) {
	/* Write your code here. */
      }
      /* Write your code here. (hint: one line) */
    }

    for (i=0; i<N; i++) {
      x[i] = xd[i];
    }


  }

  
  return 0;
}
