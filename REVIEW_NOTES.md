# 復習必須問題リスト

## 🔄 Two Pointers & Sliding Window

### 560. Subarray Sum Equals K
**本質理解の判断基準:**
- なぜ最初に考えたSliding Windowアプローチが使えなかったか
- Prefix Sum + ハッシュマップの組み合わせが必要な理由
- 実装時のチェック→記録の順番が重要な理由
- 初期値の設定理由

### 567. Permutation in String  
**本質理解の判断基準:**
- アナグラム問題を効率的に解くアプローチ
- 固定サイズウィンドウでの差分更新手法
- 辞書比較のタイミング

### 283. Move Zeroes
**本質理解の判断基準:**
- Write Pointerパターンとは何か
- 最初に試したアプローチの計算量問題
- in-place操作での正しい実装方法
9/15 X

### 88. Merge Sorted Array
### 80. Remove Duplicates from Sorted Array II
### 189. Rotate Array
### 121. Best Time to Buy and Sell Stock
### 205. Isomorphic Strings

## 🔗 Linked List

### 19. Remove Nth Node From End of List  
**本質理解の判断基準:**
- Fast/Slowポインタの位置関係理論
- dummy nodeが必要になるケース
- while条件で境界を正しく処理する方法

### 234. Palindrome Linked List
**本質理解の判断基準:**
- Fast/Slowで中央を検出する仕組み
- 奇数長リストでの中央ノードの扱い
- なぜ後半を反転するのか
- 奇偶判定の効率的な方法できる）
- dp初期化の重要性（0円=0枚、他は∞）


## 📊 Array & Intervals

### 228. Summary Ranges
**時間切れ理由:**
- 12分間「欠落のない配列を生成して比較」という複雑解法に固執
- 正解は「隣り合う要素を比較」(Two Pointers的アプローチ)だった
- 残り5分でパニック実装 → 型の整合性無視(List vs str)

**本質理解の判断基準:**
- 問題文の「list of ranges」「exactly cover」の正確な理解
- 連続判定は`nums[i+1] != nums[i] + 1`で十分だと気づけるか
- 最後の範囲処理(ループ外)を忘れずに実装できるか
- 単独要素 vs 範囲の文字列フォーマット("3" vs "0->2")

**根本課題:**
- 英語読解力不足(問題文60%理解、サンプル40%推測)
- パターン認識力不足(基本的な隣接比較に12分で気づけない)

*Generated: 2025-01-XX*