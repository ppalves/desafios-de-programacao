#include<bits/stdc++.h>

using namespace std;

int menor_mov(int linha_atual, int n_linhas, int n_colunas, vector<string> linhas, vector<int> ls)
{
    if (linha_atual >= n_linhas)
    {
        //magia
        int comum = 0;
        for (int i = 0; i < n_colunas; i++)
        {
            if (ls[i] > ls[comum])
                comum = i;
        }
        int mov_total = 0;
        for (int i = 0; i < n_colunas; i++)
        {
            ls[i]-=comum;
            mov_total+= abs(ls[i]);
        }
        return mov_total;
    }
    int qtdd = -1;
    bool deu = false;
    for (int i = 0; i < n_colunas; i++)
    {
        if (linhas[linha_atual][i] == '1')
        {
            ls[i]++;
            int temp = menor_mov(linha_atual+1, n_linhas, n_colunas, linhas, ls);
            ls[i]--;
            if (!deu)
            {
                qtdd = temp;
                deu = true;
            }
            else
            {
                if (temp < qtdd)
                    qtdd = temp;
            }
        }
    }
    return qtdd;
}

int main()
{
    int R, C;
    cin >> R >> C;
    vector<string> linhas;
    vector<int> left_shifts(C,0);
    for (int i  = 0; i < R; i++)
    {
        string a;
        cin >> a;
        linhas.push_back(a);
    }
    cout << menor_mov(0, R, C, linhas, left_shifts) << endl;
    return 0;
}
