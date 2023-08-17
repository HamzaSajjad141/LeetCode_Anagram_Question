# LeetCode Anagram 

This repository contains a Python solution for the Anagram question on LeetCode. The provided solution utilizes various techniques to determine if two given strings are anagrams of each other.

## Problem Description

The problem is to determine if two strings, `s` and `t`, are anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Solution Approaches

This repository provides multiple solution approaches to solve the anagram problem:

1. **Hash Map Technique**: This approach involves using dictionaries to store character counts for each string. The code iterates through the characters of the strings and increments the character count in the respective dictionaries. It then compares the character counts to determine if the strings are anagrams.

2. **Counter Technique**: This approach leverages the `collections.Counter` class, which counts the occurrences of each element in a collection. By comparing the counters of the two strings, the code can determine if they are anagrams.

3. **Sort Technique**: This approach involves sorting the characters of both strings and then comparing the sorted strings. If the sorted strings are equal, the original strings are anagrams.

## Usage

To use these solution approaches, you can explore the provided Python code and choose the one that suits your preferences or requirements. Each technique has its own advantages and trade-offs, so feel free to experiment and adapt them as needed.

For more information and discussions, you can also refer to the [LeetCode Anagram Question](https://leetcode.com/problems/valid-anagram/) on the LeetCode platform.

## Contribution

Contributions to this repository are welcome! If you find any issues, have improvements to suggest, or want to add more solution approaches, please consider opening a pull request or an issue. Your contributions can help make this repository even more valuable to the community.

## License

This repository is licensed under the [MIT License](LICENSE), which means that you are free to use the provided code for your own projects. However, please be aware of the license terms and provide appropriate attribution when using or distributing the code.

---

Feel free to clone and contribute to this repository or use the provided solution approaches in your projects. If you find any issues or improvements, please consider opening a pull request or an issue. Happy coding!
