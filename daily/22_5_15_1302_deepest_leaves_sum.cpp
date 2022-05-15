/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int sum = 0;
    int max_level = -1;
    
    void DFS(TreeNode* root, int level) {
        if (root == NULL)
            return;
        
        if (level > max_level) {
            max_level = level;
            sum = root -> val;
        } else if (level == max_level) {
            sum += root -> val;
        }
        
        DFS(root -> left, level + 1);
        DFS(root -> right, level + 1);
    }
    
    int deepestLeavesSum(TreeNode* root) {
        DFS(root, 1);
        return sum;
    }
};