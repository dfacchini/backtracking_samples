#include <stdio.h>
#include <stdlib.h>

int M[9][9]={{5,0,0,4,0,7,0,6,0},
             {0,9,0,0,5,0,0,1,0},
             {1,0,7,0,0,0,0,0,0},
             {2,0,0,7,0,0,0,4,1},
             {0,0,0,0,0,0,0,0,0},
             {8,7,0,0,0,2,0,0,6},
             {0,0,0,0,0,0,4,0,8},
             {0,6,0,0,4,0,0,3,0},
             {0,5,0,9,0,1,0,0,2}};

int busca_vazia(int *L,int *C) {
    for ((*L)=0;(*L)<9;(*L)++)
       for ((*C)=0;(*C)<9;(*C)++)
          if (!M[*L][*C]) {/*printf("Vazia em %d %d\n",*L,*C);*/return 1;}
    return 0;
}

void mostra() {
    int i,j;
    for (i=0;i<9;i++) {
       for (j=0;j<9;j++)
          printf("%d ",M[i][j]);
       printf("\n");
    }
    printf("\n");
}

int valida(int N,int L,int C) {
    int i,j;
    for (i=0;i<9;i++)
       if (N==M[L][i]|| N==M[i][C]) return 0;
    int LG=L/3*3;
    int CG=C/3*3;
    for (i=LG;i<=LG+2;i++)
       for (j=CG;j<=CG+2;j++)
          if (M[i][j]==N) return 0;
    //printf("Pode colocar %d em %d %d\n",N,L,C);
    return 1;
}

void su() {
    int L,C,i;
    if (!busca_vazia(&L,&C)) {
        mostra();return;
    }
    for (i=1;i<=9;i++)
       if (valida(i,L,C))
          {M[L][C]=i;su();M[L][C]=0;}
}

int main() {
    su();
    system("pause");
}
