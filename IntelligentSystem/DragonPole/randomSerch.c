#include <stdio.h>
#include "dragonPole.h"
#include <math.h>

void dragonpoleMain();
int calcBattlePoint(int *selection);

int main(void)
{
  int i,j;
  int point;
  int selection[ITEM];
  int max = 0;

  /* システム初期化 */
  dragonpoleMain();
  
  
  /* 初期化 (技をすべて0にする) */
  for (i=0; i<ITEM; i++) {
    selection[i] = 0;
  }
  for (i = 0; i < pow(2,30); i++) {
    for(j = ITEM-1; j >= 0; j--) {
      if(selection[j] > 1) {
	selection[j] = 0;
	selection[j-1]++;
      }
    }
    
    /* 戦闘力を計測 (スカウターのこと) */
    point = calcBattlePoint(selection);
     if(max <point) {
      max = point;
      for(j = 0; j < ITEM; j++) {
	printf("%d",selection[j]);
      }
      puts("");
      printf("更新：戦闘力は%d\n", point);
      }
    selection[ITEM-1]++;
  }


  

  return 0;
}
