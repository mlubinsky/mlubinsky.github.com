#include <vector>
#include <iostream>
using namespace std;
/*
Each cell on grid is either land (1) or water (0).
Your task is to count the number of islands.
An island is surrounded by water and
consists of several pieces of land reachable from each other by moving horizontally or vertically.
Whatever is outside the four edges of the grid is water.
*/
    // The 4 directions
    vector<pair<int,int>> dirs{{1,0}, {-1,0}, {0,1},{0,-1}};

    void dfs(vector<vector<int>>& grid, int i, int j, vector<vector<bool>>& visited)
    {
        if (i < 0 || i >= grid.size() || j < 0 || j >= grid[0].size() || visited[i][j] || grid[i][j] != 1)
            return;

        visited[i][j] = true;

        for (auto& dir : dirs)
        {
            dfs(grid, i+dir.first, j+dir.second, visited);
        }
    }

    int numIslands(vector<vector<int>>& grid)
    {
    	if (grid.empty())
            return 0;
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1 && !visited[i][j]) {
                    count++;
                    dfs(grid, i, j, visited);
                }
            }
        }
        return count;
    }


int main(){
   vector< vector<int> > matrix = {
      { 1, 0, 1 },
      { 1, 0, 1 },
      { 1, 0, 1 }
   };

   cout << numIslands (matrix) << endl;


   vector< vector<int> > matrix2 = {
      { 1, 0, 1 },
      { 0, 0, 1 },
      { 1, 0, 0 }
   };
   cout << numIslands (matrix2) << endl;

}