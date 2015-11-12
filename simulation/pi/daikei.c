#include <stdio.h>
#include <math.h>

int main(void)
{
  long int N = 5000000000;
  double h;
  double a = 0;
  double x;
  double y_tmp;
  double y_sum = 0;
  double r = 100000000000;
  double S;
  long int i;

  h = (r-a)/N;
  printf("h = %lf\n",h);
  for(i = 0; i < N; i++){
    x = a + i*h;
    y_tmp = sqrt(pow(r,2)-pow(x,2));
    if(i == 0 || i == N-1){
      y_sum += y_tmp;
    }else {
      y_sum += y_tmp*2;
    }
  }

  S = y_sum / 2 * h;

  printf("%.20lf\n",4*S/pow(r,2));
}
