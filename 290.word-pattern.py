#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        判定：パターン文字列と単語列が1対1対応（全単射）しているか

        Args:
            pattern: パターン文字列 (例: "abba")
            s: スペース区切りの単語列 (例: "dog cat cat dog")

        Returns:
            パターンと単語が完全に1対1対応していればTrue
        """
        words = s.split()

        # 長さが異なれば対応不可能
        if len(pattern) != len(words):
            return False

        # 双方向のマッピングを保持
        pattern_to_word_mapping = {}
        word_to_pattern_mapping = {}

        for pattern_char, word in zip(pattern, words):
            # パターン文字→単語の一貫性チェック
            if not self._is_consistent_mapping(
                pattern_char, word, pattern_to_word_mapping
            ):
                return False

            # 単語→パターン文字の一貫性チェック（逆方向）
            if not self._is_consistent_mapping(
                word, pattern_char, word_to_pattern_mapping
            ):
                return False

        return True

    def _is_consistent_mapping(
        self,
        key: str,
        value: str,
        mapping: dict[str, str]
    ) -> bool:
        """
        マッピングの一貫性を検証し、新規の場合は登録する

        Args:
            key: マッピングのキー
            value: マッピングする値
            mapping: 既存のマッピング辞書

        Returns:
            一貫性が保たれていればTrue、矛盾があればFalse
        """
        if key in mapping:
            # 既存のマッピングと一致するか確認
            return mapping[key] == value
        else:
            # 新規マッピングを登録
            mapping[key] = value
            return True


# @lc code=end

Solution().wordPattern(pattern = "abba", s = "dog cat cat dog")
# true

Solution().wordPattern(pattern = "abba", s = "dog cat cat fish")
# false

Solution().wordPattern(pattern = "aaaa", s = "dog cat cat dog")
# false