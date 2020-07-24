#include<bits/stdc++.h>

using namespace std;

int main()
{
    int N, H, L;
    cin >> N >> H >> L;
    vector<int> lista(N, 2000000);
    vector<vector<int>>adj(N, vector<int>(0,0));
    queue<int> fila;
    for (int i = 0; i < H; i++)
    {
        int a;
        cin >> a;
        lista[a] = 0;
        fila.push(a);
    }
    for (int i = 0; i < L; i++)
    {
        int a,b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    while(!fila.empty())
    {
        int index = fila.front();
        fila.pop();
        for (int vizinho : adj[index])
        {
            if (lista[index]+1 < lista[vizinho])
            {
                lista[vizinho] = lista[index]+1;
                fila.push(vizinho);
            }
        }
    }
    int maior  = 0;
    for(int i = 0; i < N; i++)
    {
        if (lista[i] > lista[maior])
            maior = i;
    }
    cout << maior << endl;
    return 0;
}
